from rest_framework import serializers
from testapp.models import Employee
"""
# Normal Serializer
class EmployeeSerializer(serializers.Serializer):
    #We can also do custom validtions just by changing max_length parameters or by doing eno = serializers.IntegerField(eno>5000)
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=64)
    esal = serializers.FloatField()
    eaddr = serializers.CharField(max_length=64)
    #Performing the custom validation on a single field i.e. esal. This is called Field level validation
    def validate_esal(self, value):
        if value < 5000:
            raise serializers.ValidationError('Employee salary should be minimum 5000.')
        return value
    #Performing the custom validation on more that a single field we require object level validation
    def validate(self, data):
        ename = data.get('ename')
        esal = data.get('esal')
        if ename.lower() == 'sunny':
            if esal < 50000:
                raise serializers.ValidationError("Sunny salary should be minimum 50000.")
        return data
    # We have to override create method for post method call
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    #We have to override update method for put method call
    def update(self, instance, validated_data):
        instance.eno = validated_data.get('eno', instance.eno)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.esal = validated_data.get('esal', instance.esal)
        instance.eaddr = validated_data.get('eaddr', instance.eaddr)
        instance.save()
        return instance

"""
#Model Serializer
class EmployeeSerializer(serializers.ModelSerializer):

    def validate_esal(self, value):
        if value < 5000:
            raise serializers.ValidationError('Employee Salary should be minimum 5000')
        return value
    class Meta:
        model = Employee
        fields = "__all__"
