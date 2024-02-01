from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from mobi.models import Phone

# Define the labels for the predictions
labels = {
    0: 'Low ,Range= Below 15K',
    1: 'Medium, Range= Upto 30K',
    2: 'High,Range= Upto 50K',
    3: 'Very High,Range= Above 50K'
}

def index(request):
    return render(request, 'index.htm')
def welcome(request):
    return render(request, 'welcome.htm')


def predict(request):
    if request.method == 'POST':
        try:   
            # Get feature values from the form
            battery_power = float(request.POST.get('battery_power'))
            int_memory = float(request.POST.get('int_memory'))
            fc = float(request.POST.get('fc')) 
            n_cores = float(request.POST.get('n_cores')) 
            ram = float(request.POST.get('ram'))
            talk_time = float(request.POST.get('talk_time')) 
            dual_sim= float(request.POST.get('dual_sim'))
            wifi = float(request.POST.get('wifi'))
            pc = float(request.POST.get('pc'))
            mobile_wt = float(request.POST.get('mobile_wt'))
        
        
       

            # Make predictions using the loaded model
            features = [battery_power , int_memory , fc , n_cores , ram ,talk_time, dual_sim , wifi , pc, mobile_wt]
            raw_data=pd.read_csv("C:/Users/ASUS/Desktop/team_ppp/Notebook/Modified.csv")
            X = raw_data.drop('price_range',axis=1)
            y = raw_data['price_range']
            X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=120)
            RF=RandomForestClassifier(n_estimators=300, max_depth=None, random_state=50)
            RF.fit(X_train, y_train)
            prediction = RF.predict([features])[0]

            # Map the numeric prediction to the corresponding label
            prediction_label = labels[prediction]

            return JsonResponse({'prediction': prediction_label})
        except Exception as e:
            # Log the exception for debugging
            import logging
            logging.error(f"Prediction error: {str(e)}")
            return JsonResponse({'error': 'Prediction error'}, status=500)

    return render(request, 'index.htm')

def get_phone_details(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        phone_name = request.GET.get('phone_name')
        try:
            phone = Phone.objects.get(name=phone_name)
            # Prepare a dictionary with phone details
            phone_details = {
                'battery_power': phone.battery_power,
                'int_memory': phone.int_memory,
                'fc': phone.fc,
                'n_cores': phone.n_cores,
                'ram': phone.ram,
                'talk_time': phone.talk_time,
                'dual_sim': phone.dual_sim,
                'wifi': phone.wifi,
                'pc': phone.pc,
                'mobile_wt': phone.mobile_wt,
            }
            return JsonResponse(phone_details)
        except Phone.DoesNotExist:
            return JsonResponse({'error': 'Phone not found'}, status=404)

    return JsonResponse({'error': 'Invalid request'}, status=400)