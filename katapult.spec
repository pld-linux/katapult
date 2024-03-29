Summary:	A tool for KDE to access your applications/documents/bookmarks quickly
Summary(pl.UTF-8):	Narzędzie dla KDE pozwalające na szybki dostęp do aplikacji/dokumentów/zakładek
Name:		katapult
Version:	0.3.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/katapult/%{name}-%{version}.tar.gz
# Source0-md5:	0f9454607a4b030dd00e5b93ebaef5ec
URL:		http://katapult.kde.org/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Katapult is a KDE application that gives you faster access to your
applications, bookmarks, and more! It is plugin-based and can launch
anything it has a plugin for. Its plugin-driven appearance is
completely customizable. Katapult was inspired by Quicksilver for OS
X, and it is written in C++.

%description -l pl.UTF-8
Katapult jest aplikacją dla KDE, która umożliwia szybszy dostęp do
aplikacji, zakładek, i wielu innych. Posiada modularną budowę i może
uruchamiać wszystko, do czego posiada odpowiednią wtyczkę. Dzięki temu
może być w dużym stopniu dostosowany do potrzeb użytkownika. Aplikacja
jest wzorowana na Quicksilver dla OS X. Jest napisana w C++.

%prep
%setup -q

%build
%configure \
	--with-qt-libraries=%{_libdir}/qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unnecessary
rm -rf $RPM_BUILD_ROOT{%{_datadir}/doc,%{_libdir}/*.la,%{_libdir}/kde3/*.la,%{_iconsdir}/*/scalable}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/*/*x*/*/*.png
%{_datadir}/services/katapult_*
%{_datadir}/servicetypes/katapult*
