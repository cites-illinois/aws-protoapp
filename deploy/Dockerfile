FROM	python:2.7

ENV	APP_DIR		/var/app
ENV	WEB_PORT	8080

#	Install system packages and clean up when done.
RUN	set -x \
	&&	apt-get update \
	&&	apt-get install -y --no-install-recommends \
			postgresql-client \
	&&	rm -rf /var/lib/apt/lists/*

#	Provision application directory and user.
RUN	set -x \
	&&	mkdir -p ${APP_DIR} \
	&&	useradd uwsgi -s /bin/false \
	&&	chown -R uwsgi:uwsgi ${APP_DIR}

#	Copy requirements.txt to build directory.
COPY	requirements.txt /

#	Install Python requirements.
RUN	pip install --no-cache-dir -r /requirements.txt

#	Run remaining instructions in application directory.
WORKDIR ${APP_DIR}

#	Create empty Django project for deployment.
RUN	django-admin startproject protoapp_deploy

#	Overwrite settings.py created by django-admin startproject.
COPY	settings.py	${APP_DIR}/protoapp_deploy/protoapp_deploy/

#	Copy scripts into image.
COPY	entrypoint.sh	/
COPY	onetime.sh	/
RUN	chmod +x /entrypoint.sh /onetime.sh

#	Expose web port to outside; must publish at runtime.
EXPOSE	${WEB_PORT}

#	Remaining instructions run as uwsgi user.
USER	uwsgi

#	Specify uwsgi configuration.
#	NOTE:	Requires UWSGI_PROJECT to be set by docker-compose.
ENV	UWSGI_BASE		'/var/app'
ENV	UWSGI_CHDIR		'%(base)/%(project)'
ENV	UWSGI_MODULE		'%(project).wsgi:application'
ENV	UWSGI_HTTP_SOCKET	':8080'
ENV	UWSGI_LISTENERS		'8'
ENV	UWSGI_MASTER		'true'
ENV	UWSGI_MAX_REQUESTS	'5000'
ENV	UWSGI_UID		'uwsgi'
ENV	UWSGI_GID		'uwsgi'
ENV	UWSGI_VACUUM		'true'

#	Specify command to run at container launch.
CMD	[ "/entrypoint.sh" ]
