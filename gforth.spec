Summary:	GNU Forth Language
Summary(pl):	Kompilator GNU Forth 
Name:		gforth
Version:	0.4.0
Release:	1
License:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
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
Gforth jest szybk± i przenoszaln± implementacj± jêzyka ANS Forth.
Dobrae wspólpracuje z edytorem Emacs oferuj±c takie cechy jak
kompletowanie i historiê wprowadzania ci±gów znaków.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

ln -sf gforth-0.4.0 $RPM_BUILD_ROOT%{_bindir}/gforth
ln -sf gforthmi-0.4.0 $RPM_BUILD_ROOT%{_bindir}/gforthmi

strip $RPM_BUILD_ROOT%{_bindir}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/gforth.info* \
	$RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS README NEWS BUGS ToDo

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

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
