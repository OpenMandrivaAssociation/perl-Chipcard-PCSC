%define module_name pcsc-perl
%define version 1.4.11
%define release 2

Summary:	Perl interface to the PC/SC smart card library
Name:		perl-%{module_name}
Version:	%{version}
Release:	%{release}
URL:		http://ludovic.rousseau.free.fr/softwares/pcsc-perl/
Source0:	http://ludovic.rousseau.free.fr/softwares/pcsc-perl/%{module_name}-%{version}.tar.bz2

License:	GPL
Group:		Development/Perl
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:  libpcsclite-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This package contains a Perl wrapper to the PC/SC smartcard library
(pcsc-lite) from MUSCLE together with some small examples.

%prep
%setup -q -n %{module_name}-%{version}

%build
find -name \*.pm | xargs chmod 644
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# this needs a smart card reader configured and with a
# card inserted
#%%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENCE README* examples Changelog
%{_mandir}/*/*
%{perl_vendorlib}/*/Chipcard
%{perl_vendorlib}/*/auto/Chipcard



%changelog
* Sat Jan 01 2011 Anssi Hannula <anssi@mandriva.org> 1.4.11-1mdv2011.0
+ Revision: 627059
- new version

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.10-1mdv2011.0
+ Revision: 602427
- new version

* Wed Sep 23 2009 Frederik Himpe <fhimpe@mandriva.org> 1.4.8-1mdv2010.0
+ Revision: 447922
- Update for new version 1.4.8

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.4.7-3mdv2010.0
+ Revision: 430522
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.4.7-2mdv2009.0
+ Revision: 268923
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.7-1mdv2009.0
+ Revision: 193868
- update to new version 1.4.7

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.4.6-4mdv2008.1
+ Revision: 151397
- rebuild for perl-5.10.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 28 2007 Andreas Hasenack <andreas@mandriva.com> 1.4.6-3mdv2008.0
+ Revision: 32050
- rebuild to see if it gets inside synthesis/hdlist this time

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.4.6-2mdv2008.0
+ Revision: 25188
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.4.6-1mdv2008.0
+ Revision: 23188
- 1.4.6


* Mon Mar 27 2006 Andreas Hasenack <andreas@mandriva.com> 1.4.2-1mdk
- packaged for Mandriva

