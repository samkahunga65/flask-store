from django.db import models

# covid = {
#     'region': {
#         'name': "Africa",
#         'avgAge': 19.7,
#         'avgDailyIncomeInUSD': 5,
#         'avgDailyIncomePopulation': 0.71
#     },
#     'periodType': "days",
#     'timeToElapse': 2,
#     'reportedCases': 674,
#     'population': 66622705,
#     'totalHospitalBeds': 1380614
# }


class Region(models.Model):
    name = models.CharField(max_length=120)
    avgAge = models.IntegerField(primary_key=False)
    avgDailyIncomeInUSD = models.IntegerField(primary_key=False)
    avgDailyIncomePopulation = models.IntegerField(primary_key=False)


class Covid(models.Model):
    region = models.ForeignKey(
        Region, related_name='region', on_delete=models.CASCADE)
    periodType = models.CharField(max_length=120)
    timeToElapse = models.IntegerField(primary_key=False)
    reportedCases = models.IntegerField(primary_key=False)
    population = models.IntegerField(primary_key=False)
    populatotalHospitalBedstion = models.IntegerField(primary_key=False)
    totalHospitalBeds = models.IntegerField(primary_key=False)

    def __str__(self):
        return self.region.name
