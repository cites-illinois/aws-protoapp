#!	/usr/bin/env bash

#	FIXME:	Find better way to wait for postgresql.
sleep 6;

echo 'Starting uwsgi ...' && uwsgi;

exit 0;
