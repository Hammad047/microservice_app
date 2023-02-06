#!/bin/bash
command ["celery -A celery_task.background_task.celery beat"]
command ["celery -A microservice_background_task.background_task.celery beat"]