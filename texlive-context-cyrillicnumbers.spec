# revision 29905
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-cyrillicnumbers
# catalog-date 2013-04-12 11:27:24 +0200
# catalog-license bsd
# catalog-version undef
Name:		texlive-context-cyrillicnumbers
Version:	20170414
Release:	2
Summary:	Write numbers as cyrillic glyphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-cyrillicnumbers
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-cyrillicnumbers.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-cyrillicnumbers.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The package extends Context's system of number conversion, by
adding numeration using cyrillic letters.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/t-cyrillicnumbers.xml
%{_texmfdistdir}/tex/context/third/cyrillicnumbers/cyrillicnumbers.lua
%{_texmfdistdir}/tex/context/third/cyrillicnumbers/t-cyrillicnumbers.mkii
%{_texmfdistdir}/tex/context/third/cyrillicnumbers/t-cyrillicnumbers.mkvi
%doc %{_texmfdistdir}/doc/context/third/cyrillicnumbers/COPYING
%doc %{_texmfdistdir}/doc/context/third/cyrillicnumbers/README.rst
%doc %{_texmfdistdir}/doc/context/third/cyrillicnumbers/cyrillicnumbers.pdf
%doc %{_texmfdistdir}/doc/context/third/cyrillicnumbers/cyrillicnumbers.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
