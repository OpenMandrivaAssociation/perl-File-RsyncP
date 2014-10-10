%define upstream_name	 File-RsyncP
%define upstream_version 0.70

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl Rsync client
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
File::RsyncP is a perl implementation of an Rsync client. It is compatible
with Rsync 2.5.5 (protocol version 26). It can send or receive files, either
by running rsync on the remote machine, or connecting to an rsyncd daemon on
the remote machine.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE='%{optflags}'
make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.700.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.700.0-1mdv2011.0
+ Revision: 561580
- update to 0.70

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.680.0-2mdv2011.0
+ Revision: 555258
- rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.680.0-1mdv2010.0
+ Revision: 407748
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.68-4mdv2009.0
+ Revision: 256997
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.68-2mdv2008.1
+ Revision: 152080
- rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 0.68-1mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.68-1mdv2007.1
+ Revision: 134795
- new version

  + Olivier Thauvin <nanardon@mandriva.org>
    - 0.68
    - 0.64
    - Import perl-File-RsyncP

* Thu May 05 2005 Olivier Thauvin <nanardon@mandriva.org> 0.52-1mdk
- First mandriva spec

