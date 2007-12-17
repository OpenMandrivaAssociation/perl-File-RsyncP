%define module	File-RsyncP
%define name	perl-%{module}
%define version	0.68
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl Rsync client
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel

%description
File::RsyncP is a perl implementation of an Rsync client. It is compatible
with Rsync 2.5.5 (protocol version 26). It can send or receive files, either
by running rsync on the remote machine, or connecting to an rsyncd daemon on
the remote machine.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE='%{optflags}'
make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*



