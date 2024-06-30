def profile_picture(request):
    if request.user.is_authenticated:
        return {'profile_picture_url': request.user.profile.profile_picture.url}
    return {}
