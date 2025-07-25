# TODO:
# - look at MPI support - doesn't work with lam for me :/
# - build with CYCLE COUNTER (required fftw_cycle.h)
#
%define		fversion	%(echo %{version} |tr r -)
%define		mversion	%(echo %{version} |cut -f -1 -d r)
Summary:	FreeMat - an environment for rapid engineering and scientific processing
Summary(pl.UTF-8):	FreeMat - środowisko do szybkiego przetwarzania inżynieryjnego i naukowego
Name:		FreeMat
Version:	3.5
Release:	1
License:	MIT
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/freemat/%{name}-%{fversion}.tar.gz
# Source0-md5:	4cc41c1f9265a86134fd338076d1a65f
Source1:	%{name}.desktop
Patch0:		%{name}-qt4.patch
Patch1:		%{name}-link.patch
URL:		http://freemat.sourceforge.net
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtXml-devel
BuildRequires:	UMFPACK-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	arpack-devel
BuildRequires:	ffcall-devel
BuildRequires:	fftw3-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	gcc-g77
BuildRequires:	lapack-devel
BuildRequires:	ncurses-devel
BuildRequires:	pcre-devel
BuildRequires:	portaudio-devel
BuildRequires:	qt4-build
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeMat is a free environment for rapid entineering and scientific
prototyping and data processing. It is similar to commercial systems
such as MATLAB from Mathworks, and IDL from Research Systems, but is
Open Source. FreeMat includes several novel features such as a
codeless interface to external C/C++/FORTRAN code,
parallel/distributed algorithm development (via MPI), and plotting and
visualiation capabilities.

%description -l pl.UTF-8
FreeMat jest darmowym środowiskiem do szybkiego przetwarzania
prototypów i danych dla inżynierów i naukowców. Jest podobny do
komercyjnych systemów takich jak MATLAB z Mathworks i IDL z Research
Group, ale na licencji Open Source. FreeMat cechuje się między innymi
bezkodowym interfejsem do zewnętrznego kodu C/C++/FORTRAN,
równoległym/rozproszonym algorytmem obliczeń (poprzez MPI), oraz
rysowaniem i wyświetlaniem możliwości.

%prep
%setup -q -n %{name}-%{mversion}
%patch -P0 -p1
%patch -P1 -p1

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
CXXFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-ncurses

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}-%{version}
%{_desktopdir}/%{name}.desktop
