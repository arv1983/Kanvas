from rest_framework.permissions import BasePermission

class Estudante2(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.is_superuser == False and user.is_staff == False:
            print('ESTU true')   
            return True
        else:
            print('ESTU false')            
            return False

class Facilitador(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.is_superuser == False and user.is_staff == True:
            print('faci true')   
            return True
        else:
            print('faci false')            
            return False


class Instrutor(BasePermission):
    def has_permission(self, request, view):
        
        user = request.user

        if user.is_superuser == True and user.is_staff == True:
            print('inst true')

            return True
        else:
            print('inst false')
            return False


class CourseAuth(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == "GET":
            return True
        elif user.is_superuser == True | user.is_staff == True:
            return True
        else:
            return False






# Estudante - terá ambos os campos is_staff e is_superuser com o valor False
# Facilitador - terá os campos is_staff == True e is_superuser == False
# Instrutor - terá ambos os campos is_staff e is_superuser com o valor True