Summary: NethServer configuration for Kopano WebApp
Name: nethserver-kopano-webapp
Version: 0.0.4
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch


Requires: nethserver-kopano
Requires: nethserver-httpd
Requires: kopano-webapp > 3.6.0
Requires: nethserver-rh-php73-php-fpm

BuildRequires: nethserver-devtools

%description
NethServer configuration for Kopano WebApp

%prep
%setup -q

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Mon Jan 11 2021 Mark Verlinde <mark.verlinde@gmail.com>
- move to rh-php73-php-fpm

* Tue Oct 01 2019 Mark Verlinde <mark.verlinde@gmail.com>
- move to rh-php72-php-fpm

* Mon Jun 25 2018 Mark Verlinde <mark.verlinde@gmail.com>
- initial build
