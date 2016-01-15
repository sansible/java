
all: test clean

test:
	cd tests/vagrant; \
	if (vagrant status | grep -E "(running|saved|poweroff)" 1>/dev/null) then \
		vagrant up || exit 1; \
		vagrant provision || exit 1; \
	else \
		vagrant up || exit 1; \
	fi;

clean:
	cd tests/vagrant; \
	vagrant destroy
