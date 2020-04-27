from django.shortcuts import render

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

def profile(request):

    return render(request, 'account/profile.html', context={
        'Category': category
    })

