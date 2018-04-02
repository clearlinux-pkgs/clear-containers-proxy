#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clear-containers-proxy
Version  : 3.0.23
Release  : 28
URL      : https://github.com/clearcontainers/proxy/archive/3.0.23.tar.gz
Source0  : https://github.com/clearcontainers/proxy/archive/3.0.23.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MIT
Requires: clear-containers-proxy-config
Requires: clear-containers-proxy-autostart
Requires: clear-containers-proxy-bin
BuildRequires : go
BuildRequires : pkgconfig(systemd)
Patch1: 0001-add-fake-configure.ac.patch

%description
[![Build Status](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-proxy-azure-ubuntu-16-04-master/badge/icon)](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-proxy-azure-ubuntu-16-04-master/)
[![Build Status](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-proxy-azure-ubuntu-17-04-master/badge/icon)](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-proxy-azure-ubuntu-17-04-master/)
[![Build Status](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-proxy-fedora-26-master/badge/icon)](http://cc-jenkins-ci.westus2.cloudapp.azure.com/job/clear-containers-proxy-fedora-26-master/)
[![Go Report Card](https://goreportcard.com/badge/github.com/clearcontainers/proxy)](https://goreportcard.com/report/github.com/clearcontainers/proxy)
[![Coverage Status](https://coveralls.io/repos/github/clearcontainers/proxy/badge.svg?branch=master)](https://coveralls.io/github/clearcontainers/proxy?branch=master)
[![GoDoc](https://godoc.org/github.com/clearcontainers/proxy?status.svg)](https://godoc.org/github.com/clearcontainers/proxy/api)

%package autostart
Summary: autostart components for the clear-containers-proxy package.
Group: Default

%description autostart
autostart components for the clear-containers-proxy package.


%package bin
Summary: bin components for the clear-containers-proxy package.
Group: Binaries
Requires: clear-containers-proxy-config

%description bin
bin components for the clear-containers-proxy package.


%package config
Summary: config components for the clear-containers-proxy package.
Group: Default

%description config
config components for the clear-containers-proxy package.


%prep
%setup -q -n proxy-3.0.23
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522699807
%reconfigure --disable-static
make  %{?_smp_mflags} GOPATH="$PWD/vendor"

%install
export SOURCE_DATE_EPOCH=1522699807
rm -rf %{buildroot}
%make_install
## make_install_append content
mv %{buildroot}/usr/lib/systemd/system/cc-proxy.service %{buildroot}/usr/lib/systemd/system/cc3-proxy.service
sed -i -e  's!^\(ExecStart=.*\)!\1 -ksm off!g' %{buildroot}/usr/lib/systemd/system/cc3-proxy.service
mv %{buildroot}/usr/lib/systemd/system/cc-proxy.socket %{buildroot}/usr/lib/systemd/system/cc3-proxy.socket
mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../cc3-proxy.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/cc3-proxy.socket
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/sockets.target.wants/cc3-proxy.socket

%files bin
%defattr(-,root,root,-)
/usr/libexec/clear-containers/cc-proxy

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/sockets.target.wants/cc3-proxy.socket
/usr/lib/systemd/system/cc3-proxy.service
/usr/lib/systemd/system/cc3-proxy.socket
