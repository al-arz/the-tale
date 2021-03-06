
import smart_imports

smart_imports.all()


urlpatterns = old_views.resource_patterns(views.GuideResource)

urlpatterns += [django_urls.url(r'^mobs/', django_urls.include((old_views.resource_patterns(mobs_views.GuideMobResource), 'mobs'))),
                django_urls.url(r'^artifacts/', django_urls.include((old_views.resource_patterns(artifacts_views.GuideArtifactResource), 'artifacts'))),
                django_urls.url(r'^cards/', django_urls.include((cards_views.guide_resource.get_urls(), 'cards'))),
                django_urls.url(r'^companions/', django_urls.include((companions_views.resource.get_urls(), 'companions')))]
