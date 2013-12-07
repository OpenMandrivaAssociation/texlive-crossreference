# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/crossreference
# catalog-date 2007-01-01 17:45:33 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-crossreference
Version:	20070101
Release:	3
Summary:	Crossreferences within documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crossreference
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines cross-references (essentially 'grand' label
references), which may be listed in a table of cross-
references.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/crossreference/crossreference.sty
%doc %{_texmfdistdir}/doc/latex/crossreference/README
%doc %{_texmfdistdir}/doc/latex/crossreference/crossreference.pdf
%doc %{_texmfdistdir}/doc/latex/crossreference/xrefexample.tex
#- source
%doc %{_texmfdistdir}/source/latex/crossreference/crossreference.drv
%doc %{_texmfdistdir}/source/latex/crossreference/crossreference.dtx
%doc %{_texmfdistdir}/source/latex/crossreference/crossreference.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070101-2
+ Revision: 750624
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070101-1
+ Revision: 718165
- texlive-crossreference
- texlive-crossreference
- texlive-crossreference
- texlive-crossreference

