Summary:	GNU Forth Language
Summary(pl.UTF-8):   Kompilator GNU Forth
Name:		gforth
Version:	0.6.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.gnu.org/gnu/gforth/%{name}-%{version}.tar.gz
# Source0-md5:	869112bd762b07fc4d2038a2d9965148
Patch0:		%{name}-info.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-acfix.patch
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gforth is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history and a powerful locals
facility, and it even has (the beginnings of) a manual. Gforth employs
traditional implementation techniques: its inner interpreter is
indirect or direct threaded. Gforth is distributed under the GNU
General Public License.

%description -l pl.UTF-8
Gforth jest szybką i przenośną implementacją języka ANS Forth. Dobrze
współpracuje z edytorem Emacs, oferując takie cechy jak dopełnianie i
historię wprowadzania ciągów znaków, ma także zaczątki podręcznika.
Gforth wykorzystuje tradycyjne techniki implementacji: jego wewnętrzny
interpreter jest pośrednio lub bezpośrednio wątkowany. Gforth jest
rozpowszechniany na Powszechnej Licencji Publicznej GNU.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -f doc/*.info*

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}

cd doc
makeinfo gforth.ds
makeinfo vmgen.texi

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS BUGS ToDo
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gforth
%dir %{_libdir}/gforth/%{version}
%attr (755,root,root) %{_libdir}/gforth/%{version}/gforth-ditc
%{_libdir}/gforth/%{version}/gforth.fi
%dir %{_libdir}/gforth/site-forth
%{_infodir}/*.info*
%{_mandir}/man1/*
%{_datadir}/gforth
