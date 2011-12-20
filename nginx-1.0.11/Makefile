
default:	build

clean:
	rm -rf Makefile objs

build:
	$(MAKE) -f objs/Makefile
	$(MAKE) -f objs/Makefile manpage

install:
	$(MAKE) -f objs/Makefile install

upgrade:
	/opt/local/sbin/ -t

	kill -USR2 `cat /opt/local/logs/nginx.pid`
	sleep 1
	test -f /opt/local/logs/nginx.pid.oldbin

	kill -QUIT `cat /opt/local/logs/nginx.pid.oldbin`
