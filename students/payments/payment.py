from all_imports.all_imports import *


razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def student_pay_fee(request):
    try:
        get_student = student_profile.objects.filter(user=request.user).first()
        get_data = json.loads(request.body)
        get_amount = get_data['amount']
        currency = 'INR'
        amount = get_amount*100
        
        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                        currency=currency,
                                                        payment_capture='0'))
        razorpay_order_id = razorpay_order['id']
        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['student_id'] = get_student.id

        payment_obj = student_payments.objects.filter(student_id=get_student).first()

        chek_last=payment_installments.objects.filter(payment_id=payment_obj).last()
        if chek_last:
            get_number = chek_last.installment_no
        else:
            get_number = 0    
        
        payment_installments.objects.create(
            student_id          = get_student,
            student_payments_id = payment_obj,
            installment_no      = get_number+1,
            order_id            = razorpay_order_id ,
            installment_amount  = get_amount )

        data={
            'status':'success',
            'status_code':200,
            'hasError':False,
            'message':"Order Generated Sucessfully",
            'data':context
        }
        return JsonResponse(data)
    
    
    except Exception as e:
        context={
            'status':'error',
            'status_code':400,
            'hasError':True,
            'message':"something went wrong",
            'data':{},
            'error':str(e)
        }
        return JsonResponse(context)    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication]) 
def paymenthandler(request):
    try:
        # get the required parameters from post request.
        get_student = student_profile.objects.filter(user=request.user).first()
        get_allow_days=payment_allow_days.objects.last()
        
        get_data = json.loads(request.body)
        order_id = get_data['order_id']
        payment_id = get_data['payment_id']
        signature = get_data['signature']

        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature 
        }

        last_installment_pay = payment_installments.objects.filter(student_id = get_student , order_id = order_id).last()

        # verify the payment signature.
   
        result = razorpay_client.utility.verify_payment_signature(params_dict)
        if result is None:
            amount = last_installment_pay.installment_amount * 100 # Rs. 200
            try:
                # capture the payemt
                razorpay_client.payment.capture(payment_id, amount)
                
                payment_installments.objects.filter(student_id = get_student ,order_id = order_id ).update(
                    payment_id = payment_id, 
                    is_paid=True
                )
                payment_obj = student_payments.objects.filter(student_id=get_student).first()
            
                student_payments.objects.filter(student_id = get_student).update(paid_amount = payment_obj.paid_amount + last_installment_pay.installment_amount)
                payment_obj_2 = student_payments.objects.filter(student_id=get_student).first()
                student_payments.objects.filter(student_id = get_student).update(
                    remain_amount = payment_obj_2.remain_amount - last_installment_pay.installment_amount,
                    allow_date =  payment_obj_2.allow_date + datetime.timedelta(days=get_allow_days.allow_days)    
                    )
                # render success page on successful caputre of payment
                data={
                    'status': 'success',
                    'status_code':200 ,
                    'hasError':False,
                    'message':"Payment Successful",
                    'data':{}
                    }
                return JsonResponse(data)
            except:

                # if there is an error while capturing payment.
                data={
                    'status': 'failed',
                    'status_code':400 ,
                    'hasError':True,
                    'message':"Payment Unsuccessful",
                    'data':{}
                    }
                return JsonResponse(data)
        else:

            # if signature verification fails.
            data={
                    'status': 'failed',
                    'status_code':400 ,
                    'hasError':True,
                    'message':"Payment Unsuccessful , signature verification fail",
                    'data':{}
                    }
            return JsonResponse(data)
    except Exception as e:
        data={
            'status':'error',
            'status_code':400,
            'hasError':True,
            'message':f"{e}",
            'data':{},
            
        }
        return JsonResponse(data)
