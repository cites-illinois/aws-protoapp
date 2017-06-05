#!	/usr/bin/env bash

#	This should only be run when deploying in an empty db.

echo 'Setting up Django ...';

cd ${APP_DIR}/protoapp_deploy \
	&&	python manage.py collectstatic --no-input \
	&&	python manage.py migrate --no-input \
       	&&	python manage.py loaddata auth \
       	&&	python manage.py loaddata protoapp; \

exit 0;
