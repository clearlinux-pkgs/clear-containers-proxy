#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clear-containers-proxy
Version  : 3.0.1
Release  : 6
URL      : https://github.com/clearcontainers/proxy/archive/3.0.1.tar.gz
Source0  : https://github.com/clearcontainers/proxy/archive/3.0.1.tar.gz
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
This repository holds supplemental Go packages for low-level interactions with the operating system.

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
%setup -q -n proxy-3.0.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507320170
%reconfigure --disable-static
make V=1  %{?_smp_mflags} GOPATH="$PWD/vendor"

%install
export SOURCE_DATE_EPOCH=1507320170
rm -rf %{buildroot}
%make_install
## make_install_append content
mv %{buildroot}/usr/lib/systemd/system/cc-proxy.service %{buildroot}/usr/lib/systemd/system/cc3-proxy.service
sed -i -e  's!^\(ExecStart=.*\)!\1 -ksm off!g' %{buildroot}/usr/lib/systemd/system/cc3-proxy.service
mv %{buildroot}/usr/lib/systemd/system/cc-proxy.socket %{buildroot}/usr/lib/systemd/system/cc3-proxy.socket
mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
mkdir %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../cc3-proxy.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/cc3-proxy.socket
ln -s ../cc3-proxy.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/cc3-proxy.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/cc3-proxy.service
/usr/lib/systemd/system/sockets.target.wants/cc3-proxy.socket

%files bin
%defattr(-,root,root,-)
/usr/libexec/clear-containers/cc-proxy

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/cc3-proxy.service
%exclude /usr/lib/systemd/system/sockets.target.wants/cc3-proxy.socket
/usr/lib/systemd/system/cc3-proxy.service
/usr/lib/systemd/system/cc3-proxy.socket
