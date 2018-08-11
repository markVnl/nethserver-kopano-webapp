Summary: NethServer configuration for Kopano WebApp
Name: nethserver-kopano-webapp
Version: 0.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch


Requires: nethserver-kopano
Requires: nethserver-httpd
Requires: kopano-webapp

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
* Mon Jun 25 2018 Mark Verlinde mark.verlinde@gmail.com
- initial build
