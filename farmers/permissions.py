
from rest_framework.permissions import BasePermission

class IsFieldExecutiveA(BasePermission):
    def has_permission(self, request, view):
        return request.user.teammember.role == 'Field Executive' and request.user.username == 'A'

class IsFieldExecutiveB(BasePermission):
    def has_permission(self, request, view):
        return request.user.teammember.role == 'Field Executive' and request.user.username == 'B'

class IsManagerC(BasePermission):
    def has_permission(self, request, view):
        return request.user.teammember.role == 'Field Manager' and request.user.username == 'C'

class IsManagerD(BasePermission):
    def has_permission(self, request, view):
        return request.user.teammember.role == 'Field Manager' and request.user.username == 'D'

class IsSeniorManagerE(BasePermission):
    def has_permission(self, request, view):
        return request.user.teammember.role == 'Senior Manager' and request.user.username == 'E'
