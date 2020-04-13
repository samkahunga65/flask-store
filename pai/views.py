from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .serializers import CovidSerializer, RegionSerializer
from .models import Covid, Region
import math


@api_view(['GET'])
def covided(request):
    covid = Covid.objects.all()
    serializer = CovidSerializer(covid, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def covid(request):
#     covid = Region.objects.all()
#     serializer = RegionSerializer(covid, many=True)
#     return Response(serializer.data)


@api_view(['POST'])
def covid(request):
    serializer = CovidSerializer(data=request.data)

    def estimator(data):
        o_data = data
        i_ci = data['reportedCases']*10
        s_ci = data['reportedCases']*50
        i_ibrtd = i_ci*1.6
        i_ibrtw = i_ci*5.6
        i_ibrtm = i_ci*2**10
        s_ibrtd = i_ci*1.6
        s_ibrtw = i_ci*5.6
        s_ibrtm = i_ci*2**10
        i_ibrt = i_ci*0.6*data["timeToElapse"]
        s_ibrt = s_ci*0.6*data["timeToElapse"]
        i_scbrt = i_ibrt*1.15
        s_scbrt = s_ibrt*1.15
        beds = data["totalHospitalBeds"]*0.35
        i_hbrt = beds - i_scbrt
        s_hbrt = beds - s_scbrt
        i_icu = i_ibrt*0.05
        s_icu = s_ibrt*0.05
        i_rep = s_ibrt*0.02
        s_rep = s_ibrt*0.02
        i_dif = (data['region']['avgDailyIncomeInUSD']*data['region']
                 ['avgDailyIncomePopulation']*data['timeToElapse']*i_ibrt)
        s_dif = (data['region']['avgDailyIncomeInUSD']*data['region']
                 ['avgDailyIncomePopulation']*data['timeToElapse']*s_ibrt)
        data = {
            'data': o_data,
            'impact': {'currentlyInfected': i_ci, 'infectionsByRequestedTime': math.trunc(i_ibrt),
                       'severeCasesByRequestedTime': math.trunc(i_scbrt), 'hospitalBedsByRequestedTime': math.trunc(i_hbrt),
                       'casesForICUByRequestedTime': math.trunc(i_icu),
                       'casesForVentilatorsByRequestedTime': math.trunc(i_rep),
                       'dollarsInFlight': math.trunc(i_dif)},
            "severeImpact": {'currentlyInfected': s_ci, 'infectionsByRequestedTime': math.trunc(s_ibrt),
                             'severeCasesByRequestedTime': math.trunc(s_scbrt), 'hospitalBedsByRequestedTime': math.trunc(s_hbrt),
                             'casesForICUByRequestedTime': math.trunc(s_icu),
                             'casesForVentilatorsByRequestedTime': math.trunc(s_rep),
                             'dollarsInFlight': math.trunc(s_dif)}}
        return data

    if serializer.is_valid():
        print('yes')
        serializer.save()
    qq = estimator(serializer.data)

    return Response(qq)


@api_view(['POST'])
@renderer_classes([XMLRenderer])
def covidx(request):

    serializer = CovidSerializer(data=request.data)

    def estimator(data):
        o_data = data
        i_ci = data['reportedCases']*10
        s_ci = data['reportedCases']*50
        i_ibrtd = i_ci*1.6
        i_ibrtw = i_ci*5.6
        i_ibrtm = i_ci*2**10
        s_ibrtd = i_ci*1.6
        s_ibrtw = i_ci*5.6
        s_ibrtm = i_ci*2**10
        i_ibrt = i_ci*0.6*data["timeToElapse"]
        s_ibrt = s_ci*0.6*data["timeToElapse"]
        i_scbrt = i_ibrt*1.15
        s_scbrt = s_ibrt*1.15
        beds = data["totalHospitalBeds"]*0.35
        i_hbrt = beds - i_scbrt
        s_hbrt = beds - s_scbrt
        i_icu = i_ibrt*0.05
        s_icu = s_ibrt*0.05
        i_rep = s_ibrt*0.02
        s_rep = s_ibrt*0.02
        i_dif = (data['region']['avgDailyIncomeInUSD']*data['region']
                 ['avgDailyIncomePopulation']*data['timeToElapse']*i_ibrt)
        s_dif = (data['region']['avgDailyIncomeInUSD']*data['region']
                 ['avgDailyIncomePopulation']*data['timeToElapse']*s_ibrt)
        data = {
            'data': o_data,
            'impact': {'currentlyInfected': i_ci, 'infectionsByRequestedTime': math.trunc(i_ibrt),
                       'severeCasesByRequestedTime': math.trunc(i_scbrt), 'hospitalBedsByRequestedTime': math.trunc(i_hbrt),
                       'casesForICUByRequestedTime': math.trunc(i_icu),
                       'casesForVentilatorsByRequestedTime': math.trunc(i_rep),
                       'dollarsInFlight': math.trunc(i_dif)},
            "severeImpact": {'currentlyInfected': s_ci, 'infectionsByRequestedTime': math.trunc(s_ibrt),
                             'severeCasesByRequestedTime': math.trunc(s_scbrt), 'hospitalBedsByRequestedTime': math.trunc(s_hbrt),
                             'casesForICUByRequestedTime': math.trunc(s_icu),
                             'casesForVentilatorsByRequestedTime': math.trunc(s_rep),
                             'dollarsInFlight': math.trunc(s_dif)}}
        return data

    if serializer.is_valid():
        print('yes')
        serializer.save()
    qq = estimator(serializer.data)

    return Response(qq)
