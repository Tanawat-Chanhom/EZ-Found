from django.shortcuts import render

# Create your views here.
def index(request):
    category = [
        {"id":1,"value":"Wallet"},
        {"id":2,"value":"Cards"},
        {"id":3,"value":"Bags"},
        {"id":4,"value":"Books"},
        {"id":5,"value":"Stationery"},
        {"id":6,"value":"Glasses"},
        {"id":7,"value":"Jewery"},
        {"id":8,"value":"Other"},
        {"id":9,"value":"Other"},
        {"id":10,"value":"Other"},
        {"id":11,"value":"Other"},
        {"id":12,"value":"Other"},
        {"id":13,"value":"Other"},
        {"id":14,"value":"Other"},
        {"id":15,"value":"Other"},
    ]

    status = [
        {"id":1,"value":"Lost"},
        {"id":2,"value":"Found"},
        {"id":3,"value":"Returned"},
        {"id":4,"value":"Other"},
        {"id":5,"value":"Other"},
        {"id":6,"value":"Other"},
        {"id":7,"value":"Other"},
        
    ]

    locations = [
        {"id":1,"value":"Lost"},
        {"id":2,"value":"Found"},
        {"id":3,"value":"Returned"},
        {"id":4,"value":"Other"},
    ]

    noti = [
        {"id":1,"value":"Lost"},
        {"id":2,"value":"Found"},
        {"id":3,"value":"Returned"},
        {"id":4,"value":"Other"},
        {"id":1,"value":"Lost"},
        {"id":2,"value":"Found"},
        {"id":3,"value":"Returned"},
        {"id":4,"value":"Other"},
        {"id":1,"value":"Lost"},
        {"id":2,"value":"Found"},
        {"id":3,"value":"Returned"},
        {"id":4,"value":"Other"},
    ]
    return render(request, 'posts/index.html', context={
        'Category': category,
        'Status': status,
        'Locations': locations,
        'Noti': noti
    })