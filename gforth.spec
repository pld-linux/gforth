Summary:	GNU Forth Language
Summary(pl):	Kompilator GNU Forth 
Name:		gforth
Version:	0.4.0
Release:	2
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/J�zyki
Source0:	ftp://ftp.complang.tuwien.ac.at/pub/forth/gforth/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gforth is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history and a powerful locals
facility, and it even has (the beginnings of) a manual. Gforth employs
traditional implementation techniques: its inner innerpreter is
indirect or direct threaded. Gforth is distributed under the GNU
General Public license (see COPYING).

%description -l pl
Gforth jest szybk� i przenoszaln� implementacj� j�zyka ANS Forth.
Dobrae wsp�lpracuje z edytorem Emacs oferuj�c takie cechy jak
kompletowanie i histori� wprowadzania ci�g�w znak�w.

%prep
%setup -q
%patch -p1

%build
%configure

%{__make}

(cd doc; makeinfo gforth.ds)

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

rm -f $RPM_BUILD_ROOT%{_bindir}/{gforth,gforthmi}
mv -f $RPM_BUILD_ROOT%{_bindir}/gforth-0.4.0 $RPM_BUILD_ROOT%{_bindir}/gforth
mv -f $RPM_BUILD_ROOT%{_bindir}/gforthmi-0.4.0 $RPM_BUILD_ROOT%{_bindir}/gforthmi

gzip -9nf AUTHORS README NEWS BUGS ToDo

%post
%fix_info_dir

%postun
%fix_info_dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,README,NEWS,BUGS,ToDo}.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/gforth
%{_infodir}/*info*
%{_mandir}/man1/*
%{_datadir}/gforth
