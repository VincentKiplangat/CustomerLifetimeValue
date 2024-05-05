
#
# @api_view(['POST'])
# def predict(request):
#     try:
#         # Load the XGBoost model
#         print("Loading XGBoost model...")
#         xgb_model = joblib.load("xgb_tuned.pkl")
#
#         # Get the input data from the request
#         print("Getting input data from the request...")
#         mydata = request.data
#
#         # Preprocess the input data if necessary
#         # For example, convert it to a numpy array and reshape it
#         print("Preprocessing input data...")
#         unit = np.array(list(mydata.values())).reshape(1, -1)
#
#         # Make predictions using the XGBoost model
#         print("Making predictions...")
#         y_pred = xgb_model.predict(unit)
#
#         # Determine the response based on the predicted score
#         print("Determining response...")
#         if float(y_pred) > 0.5:
#             response_text = 'High'
#         else:
#             response_text = 'Low'
#
#         # Print the prediction result
#         print("Prediction:", response_text)
#
#         # Return the response
#         return JsonResponse({'prediction': response_text}, status=status.HTTP_200_OK)
#
#     except Exception as e:
#         # Print the error message
#         print("Error:", e)
#
#         # Return an error response if there's any exception
#         return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# @api_view(['POST'])
# def predict(request):
#     data = request.data
#     # Extract form data from the request
#     age = data.get('age')
#     price = data.get('price')
#     lifetime_months = data.get('lifetime_months')
#     channel_email = data.get('channel_email')
#     channel_phone = data.get('channel_phone')
#     reason_signup = data.get('reason_signup')
#     reason_support = data.get('reason_support')
#     gender_female = data.get('gender_female')
#     gender_male = data.get('gender_male')
#     subscription_annual_subscription = data.get('subscription_annual_subscription')
#     subscription_monthly_subscription = data.get('subscription_monthly_subscription')
#     signup_period_Morning = data.get('signup_period_Morning')
#     signup_period_Night = data.get('signup_period_Night')
#     signup_period_Noon = data.get('signup_period_Noon')
#     end_period_Morning = data.get('end_period_Morning')
#     end_period_Night = data.get('end_period_Night')
#     end_period_Noon = data.get('end_period_Noon')
#
#     # Now you have all the form data, you can use it for prediction or any other processing
#     # Example: You can pass this data to your machine learning model for prediction
#
#     # For demonstration purposes, let's assume you just want to echo back the form data as response
#     result = {
#         'age': age,
#         'price': price,
#         'lifetime_months': lifetime_months,
#         'channel_email': channel_email,
#         'channel_phone': channel_phone,
#         'reason_signup': reason_signup,
#         'reason_support': reason_support,
#         'gender_female': gender_female,
#         'gender_male': gender_male,
#         'subscription_annual_subscription': subscription_annual_subscription,
#         'subscription_monthly_subscription': subscription_monthly_subscription,
#         'signup_period_Morning': signup_period_Morning,
#         'signup_period_Night': signup_period_Night,
#         'signup_period_Noon': signup_period_Noon,
#         'end_period_Morning': end_period_Morning,
#         'end_period_Night': end_period_Night,
#         'end_period_Noon': end_period_Noon
#     }
#     return Response(result)


from rest_framework.response import Response
# @api_view(['POST'])
# def predict(request):
#     try:
#         # Load the XGBoost model
#         xgb_model = joblib.load("xgb_tuned.pkl")
#
#         # Extract form data from the request
#         data = request.data
#         age = float(data.get('age', 0))  # Convert age to float
#         price = float(data.get('price', 0))  # Convert price to float
#         lifetime_months = float(data.get('lifetime_months', 0))  # Convert lifetime_months to float
#         channel_email = int(data.get('channel_email', 0))  # Convert channel_email to int
#         channel_phone = int(data.get('channel_phone', 0))  # Convert channel_phone to int
#         reason_signup = int(data.get('reason_signup', 0))  # Convert reason_signup to int
#         reason_support = int(data.get('reason_support', 0))  # Convert reason_support to int
#         gender_female = int(data.get('gender_female', 0))  # Convert gender_female to int
#         gender_male = int(data.get('gender_male', 0))  # Convert gender_male to int
#         subscription_annual_subscription = int(data.get('subscription_annual_subscription', 0))  # Convert subscription_annual_subscription to int
#         subscription_monthly_subscription = int(data.get('subscription_monthly_subscription', 0))  # Convert subscription_monthly_subscription to int
#         signup_period_Morning = int(data.get('signup_period_Morning', 0))  # Convert signup_period_Morning to int
#         signup_period_Night = int(data.get('signup_period_Night', 0))  # Convert signup_period_Night to int
#         signup_period_Noon = int(data.get('signup_period_Noon', 0))  # Convert signup_period_Noon to int
#         end_period_Morning = int(data.get('end_period_Morning', 0))  # Convert end_period_Morning to int
#         end_period_Night = int(data.get('end_period_Night', 0))  # Convert end_period_Night to int
#         end_period_Noon = int(data.get('end_period_Noon', 0))  # Convert end_period_Noon to int
#
#         # Create a numpy array with the extracted data
#         input_data = np.array([
#             age, price, lifetime_months, channel_email, channel_phone, reason_signup, reason_support,
#             gender_female, gender_male, subscription_annual_subscription, subscription_monthly_subscription,
#             signup_period_Morning, signup_period_Night, signup_period_Noon, end_period_Morning,
#             end_period_Night, end_period_Noon
#         ]).reshape(1, -1)
#
#         # Make predictions using the XGBoost model
#         y_pred = xgb_model.predict(input_data)
#
#         # Determine the response based on the predicted score
#         response_text = 'High' if float(y_pred) > 0.5 else 'Low'
#
#         # Return the prediction result as a JSON response
#         return Response({'prediction': response_text})
#
#     except Exception as e:
#         # Return an error response if there's any exception
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def predict(request):
#     try:
#         # Load the XGBoost model
#         xgb_model = joblib.load("xgb_tuned.pkl")
#
#         # Extract form data from the request
#         data = request.data
#
#         CustomerID = data.get('customerID')
#         # Convert checkbox values to integers
#         channel_email = 1 if data.get('channel_email') == 'on' else 0
#         channel_phone = 1 if data.get('channel_phone') == 'on' else 0
#         reason_signup = 1 if data.get('reason_signup') == 'on' else 0
#         reason_support = 1 if data.get('reason_support') == 'on' else 0
#         gender_female = 1 if data.get('gender_female') == 'on' else 0
#         gender_male = 1 if data.get('gender_male') == 'on' else 0
#         subscription_annual_subscription = 1 if data.get('subscription_annual_subscription') == 'on' else 0
#         subscription_monthly_subscription = 1 if data.get('subscription_monthly_subscription') == 'on' else 0
#         signup_period_Morning = 1 if data.get('signup_period_Morning') == 'on' else 0
#         signup_period_Night = 1 if data.get('signup_period_Night') == 'on' else 0
#         signup_period_Noon = 1 if data.get('signup_period_Noon') == 'on' else 0
#         end_period_Morning = 1 if data.get('end_period_Morning') == 'on' else 0
#         end_period_Night = 1 if data.get('end_period_Night') == 'on' else 0
#         end_period_Noon = 1 if data.get('end_period_Noon') == 'on' else 0
#
#         # Extract other numerical data
#         age = float(data.get('age', 0))
#         price = float(data.get('price', 0))
#         lifetime_months = float(data.get('lifetime_months', 0))
#
#         # Create a numpy array with the extracted data
#         input_data = np.array([
#             age, price, lifetime_months, channel_email, channel_phone, reason_signup, reason_support,
#             gender_female, gender_male, subscription_annual_subscription, subscription_monthly_subscription,
#             signup_period_Morning, signup_period_Night, signup_period_Noon, end_period_Morning,
#             end_period_Night, end_period_Noon
#         ]).reshape(1, -1)
#
#         # Make predictions using the XGBoost model
#         y_pred = xgb_model.predict(input_data)
#
#         # Determine the response based on the predicted score
#         response_text = y_pred
#
#         # Return the prediction result as a JSON response
#         return Response({'prediction': response_text})
#
#     except Exception as e:
#         # Return an error response if there's any exception
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
# *****************************************************************************************************************************

# from django.http import HttpResponse
#
# @api_view(['POST'])
# def predict(request):
#     try:
#         # Load the XGBoost model
#         xgb_model = joblib.load("xgb_tuned.pkl")
#
#         # Extract form data from the request
#         data = request.data
#
#         # Extract form data and convert checkbox values to integers
#         CustomerID = data.get('customerID')
#         channel_email = 1 if data.get('channel_email') == 'on' else 0
#         channel_phone = 1 if data.get('channel_phone') == 'on' else 0
#         reason_signup = 1 if data.get('reason_signup') == 'on' else 0
#         reason_support = 1 if data.get('reason_support') == 'on' else 0
#         gender_female = 1 if data.get('gender_female') == 'on' else 0
#         gender_male = 1 if data.get('gender_male') == 'on' else 0
#         subscription_annual_subscription = 1 if data.get('subscription_annual_subscription') == 'on' else 0
#         subscription_monthly_subscription = 1 if data.get('subscription_monthly_subscription') == 'on' else 0
#         signup_period_Morning = 1 if data.get('signup_period_Morning') == 'on' else 0
#         signup_period_Night = 1 if data.get('signup_period_Night') == 'on' else 0
#         signup_period_Noon = 1 if data.get('signup_period_Noon') == 'on' else 0
#         end_period_Morning = 1 if data.get('end_period_Morning') == 'on' else 0
#         end_period_Night = 1 if data.get('end_period_Night') == 'on' else 0
#         end_period_Noon = 1 if data.get('end_period_Noon') == 'on' else 0
#
#         # Extract other numerical data
#         age = float(data.get('age', 0))
#         price = float(data.get('price', 0))
#         lifetime_months = float(data.get('lifetime_months', 0))
#
#         # Create a numpy array with the extracted data
#         input_data = np.array([
#             age, price, lifetime_months, channel_email, channel_phone, reason_signup, reason_support,
#             gender_female, gender_male, subscription_annual_subscription, subscription_monthly_subscription,
#             signup_period_Morning, signup_period_Night, signup_period_Noon, end_period_Morning,
#             end_period_Night, end_period_Noon
#         ]).reshape(1, -1)
#
#         # Make predictions using the XGBoost model
#         y_pred = xgb_model.predict(input_data)
#
#         # Render HTML response
#         response_html = f"""
#             <!DOCTYPE html>
#             <html lang="en">
#             <head>
#                 <meta charset="UTF-8">
#                 <meta name="viewport" content="width=device-width, initial-scale=1.0">
#                 <title>Prediction Result</title>
#             </head>
#             <body>
#                 <h1>Prediction Result</h1>
#                 <p>The predicted value is: <strong>{y_pred}</strong></p>
#             </body>
#             </html>
#         """
#
#         return HttpResponse(response_html)
#
#     except Exception as e:
#         # Return an error response if there's any exception
#         return HttpResponse(f"<h1>Error: {e}</h1>", status=400)

# ***************************************************************************************************

from django.shortcuts import render
from django.http import HttpResponse

# @api_view(['POST'])
# def predict(request):
#     try:
#         # Load the XGBoost model
#         xgb_model = joblib.load("xgb_tuned.pkl")
#
#         # Extract form data from the request
#         data = request.data
#
#         # Extract form data and convert checkbox values to integers
#         CustomerID = data.get('customerID')
#         channel_email = 1 if data.get('channel_email') == 'on' else 0
#         channel_phone = 1 if data.get('channel_phone') == 'on' else 0
#         reason_signup = 1 if data.get('reason_signup') == 'on' else 0
#         reason_support = 1 if data.get('reason_support') == 'on' else 0
#         gender_female = 1 if data.get('gender_female') == 'on' else 0
#         gender_male = 1 if data.get('gender_male') == 'on' else 0
#         subscription_annual_subscription = 1 if data.get('subscription_annual_subscription') == 'on' else 0
#         subscription_monthly_subscription = 1 if data.get('subscription_monthly_subscription') == 'on' else 0
#         signup_period_Morning = 1 if data.get('signup_period_Morning') == 'on' else 0
#         signup_period_Night = 1 if data.get('signup_period_Night') == 'on' else 0
#         signup_period_Noon = 1 if data.get('signup_period_Noon') == 'on' else 0
#         end_period_Morning = 1 if data.get('end_period_Morning') == 'on' else 0
#         end_period_Night = 1 if data.get('end_period_Night') == 'on' else 0
#         end_period_Noon = 1 if data.get('end_period_Noon') == 'on' else 0
#
#         # Extract other numerical data
#         age = float(data.get('age', 0))
#         price = float(data.get('price', 0))
#         lifetime_months = float(data.get('lifetime_months', 0))
#
#         # Create a numpy array with the extracted data
#         input_data = np.array([
#             age, price, lifetime_months, channel_email, channel_phone, reason_signup, reason_support,
#             gender_female, gender_male, subscription_annual_subscription, subscription_monthly_subscription,
#             signup_period_Morning, signup_period_Night, signup_period_Noon, end_period_Morning,
#             end_period_Night, end_period_Noon
#         ]).reshape(1, -1)
#
#         # Make predictions using the XGBoost model
#         y_pred = xgb_model.predict(input_data)
#
#         # Render api.html template with prediction result
#         return render(request, 'api.html', {'prediction': y_pred})
#
#     except Exception as e:
#         # Return an error response if there's any exception
#         return HttpResponse(f"<h1>Error: {e}</h1>", status=400)
