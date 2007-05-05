%define module_name pcsc-perl
%define version 1.4.6
%define release %mkrel 1

Summary:	Perl interface to the PC/SC smart card library
Name:		perl-%{module_name}
Version:	%{version}
Release:	%{release}
URL:		http://search.cpan.org/dist/%{module_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/W/WH/WHOM/%{module_name}-%{version}.tar.bz2
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


