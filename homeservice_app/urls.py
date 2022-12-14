from django.urls import path

from homeservice_app import views, adminviews, workerviews, customerviews,officerviews

urlpatterns = [
    path('', views.home, name='home'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('Nursery_register/', views.Nursery_register, name='Nursery_register'),
    path('farmer_register/', views.farmer_register, name='farmer_register'),
    path('officer_register/', views.officer_register, name='officer_register'),


    path('admin_home/', adminviews.admin_home, name='admin_home'),
    path('view_Nursery/', adminviews.view_Nursery, name='view_Nursery'),
    path('workers_update/<int:id>/', adminviews.workers_update, name='workers_update'),
    path('worker_remove/<int:id>/', adminviews.remove_worker, name='worker_remove'),
    path('customers_view/', adminviews.view_customers, name='customers_view'),
    path('view_officer/', adminviews.view_officer, name='view_officer'),
    path('customers_remove/<int:id>/', adminviews.remove_customers, name='customers_remove'),
    path('work_add/', adminviews.add_work, name='work_add'),
    path('work_view/', adminviews.view_work, name='work_view'),
    path('work_update/<int:id>/', adminviews.update_work, name='work_update'),
    path('work_delete/<int:id>/', adminviews.delete_work, name='work_delete'),
    path('appointment_admin', adminviews.appointment_admin, name='appointment_admin'),
    path('approve_appointment/<int:id>/', adminviews.approve_appointment, name='approve_appointment'),
    path('reject_appointment/<int:id>/', adminviews.reject_appointment, name='reject_appointment'),
    # path('Feedback_admin/', adminviews.Feedback_admin, name='Feedback_admin'),
    # path('reply_Feedback/<int:id>/', adminviews.reply_Feedback, name='reply_Feedback'),
    path('add_bill/', adminviews.bill, name='add_bill'),
    path('view_bill/', adminviews.view_bill, name='view_bill'),
    path('weatherdata/', adminviews.weatherdata, name='weatherdata'),
    path('view_weather/', adminviews.view_weather, name='view_weather'),

    path('worker_home/', workerviews.worker_home, name='worker_home'),
    path('schedule_add/', workerviews.schedule_add, name='schedule_add'),
    path('schedule_views', workerviews.schedule_view, name='schedule_views'),
    path('schedule_update/<int:id>/', workerviews.schedule_update, name='schedule_update'),
    path('schedule_delete/<int:id>/', workerviews.schedule_delete, name='schedule_delete'),
    path('view_bill_worker/', workerviews.view_bill_worker, name='view_bill_worker'),
    path('appointment_view_worker/', workerviews.appointment_view_worker, name='appointment_view_worker'),
    path('stockpage',workerviews.stockpage, name="stockpage"),
    path('seedpage',workerviews.seedpage, name="seedpage"),
    path('plantpage',workerviews.plantpage, name="plantpage"),
    path('fertilizerpage',workerviews.fertilizerpage, name="fertilizerpage"),
    path('view_stock',workerviews.view_stock, name="view_stock"),
    path('weatherdetails2',workerviews.weatherdetails2, name="weatherdetails2"),
    path('update_seed/<int:id>/', workerviews.update_seed, name="update_seed"),
    path('update_plant/<int:id>/', workerviews.update_plant, name="update_plant"),
    path('update_fertilizer/<int:id>/', workerviews.update_fertilizer, name="update_fertilizer"),
    path('remove_plant/<int:id>/', workerviews.remove_plant, name="remove_plant"),
    path('remove_fertilizer/<int:id>/', workerviews.remove_fertilizer, name="remove_fertilizer"),
    path('remove_seed/<int:id>/', workerviews.remove_seed, name="remove_seed"),
    path('view_announcecustomets', workerviews.view_announcecustomets, name="view_announcecustomets"),

    path('customer_home', customerviews.customer_home, name='customer_home'),
    path('farmerviewprofile', customerviews.farmerviewprofile, name='farmerviewprofile'),
    path('view_workers/', customerviews.view_workers_customer, name='view_workers'),
    path('view_Nursery1/', customerviews.view_Nursery1, name='view_Nursery1'),
    path('view_schedule/', customerviews.view_schedule_customer, name='view_schedule'),
    path('take_appointment/<int:id>/', customerviews.take_appointment, name='take_appointment'),
    path('appointment_view', customerviews.appointment_view, name='appointment_view'),
    path('Feedback_add_user', customerviews.Feedback_add_user, name='Feedback_add_user'),
    path('updatefarmer', customerviews.updatefarmer, name='updatefarmer'),
    path('Feedback_view_user', customerviews.Feedback_view_user, name='Feedback_view_user'),
    path('view_bill_user', customerviews.view_bill_user, name='view_bill_user'),
    path('pay_bill/<int:id>/', customerviews.pay_bill, name='pay_bill'),
    # path('face', face_detect.face, name='face'),
    path('pay_in_direct/<int:id>/', customerviews.pay_in_direct, name='pay_in_direct'),
    path('bill_history', customerviews.bill_history, name='bill_history'),
    # path('successfull',customerviews.successful, name='succesfull'),
    path("display_task_page",customerviews.task_load,name="task_load"),
    path("display_task_page1",customerviews.task_load1,name="task_load1"),
    path("load_upload_page",customerviews.load_upload_page,name="load_upload_page"),
    path("load_upload_page1",customerviews.load_upload_page1,name="load_upload_page1"),
    path('view_stock1/<int:id>/',customerviews.view_stock1, name="view_stock1"),
    path('view_announcecustome',customerviews.view_announcecustome, name="view_announcecustome"),


    path('chat_add',customerviews.chat_add,name='chat_add'),
    path('chat_view',customerviews.chat_view,name='chat_view'),

    path('officer_home', officerviews.officer_home, name='officer_home'),
    path('remove_officer/<int:id>/', officerviews.remove_officer, name='remove_officer'),
    path('Feedback_officer', officerviews.Feedback_officer, name='Feedback_officer'),
    path('view_Nursery3', officerviews.view_Nursery3, name='view_Nursery3'),
    path('reply_Feedback/<int:id>/', officerviews.reply_Feedback, name='reply_Feedback'),
    path('weatherdetails/', officerviews.weatherdetails, name='weatherdetails'),
    path('announce', officerviews.announce, name='announce'),
    path('view_announce', officerviews.view_announce, name='view_announce'),

]
