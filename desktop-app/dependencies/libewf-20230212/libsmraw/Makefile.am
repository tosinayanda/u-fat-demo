if HAVE_LOCAL_LIBSMRAW
AM_CPPFLAGS = \
	-I$(top_srcdir)/include \
	-I$(top_srcdir)/common \
	@LIBCERROR_CPPFLAGS@ \
	@LIBCTHREADS_CPPFLAGS@ \
	@LIBCDATA_CPPFLAGS@ \
	@LIBCLOCALE_CPPFLAGS@ \
	@LIBCNOTIFY_CPPFLAGS@ \
	@LIBCSPLIT_CPPFLAGS@ \
	@LIBUNA_CPPFLAGS@ \
	@LIBCFILE_CPPFLAGS@ \
	@LIBCPATH_CPPFLAGS@ \
	@LIBBFIO_CPPFLAGS@ \
	@LIBFCACHE_CPPFLAGS@ \
	@LIBFDATA_CPPFLAGS@ \
	@LIBFDATETIME_CPPFLAGS@ \
	@LIBFGUID_CPPFLAGS@ \
	@LIBFVALUE_CPPFLAGS@ \
	@PTHREAD_CPPFLAGS@ 

noinst_LTLIBRARIES = libsmraw.la

libsmraw_la_SOURCES = \
	libsmraw_codepage.h \
	libsmraw_definitions.h \
	libsmraw_error.c libsmraw_error.h \
	libsmraw_extern.h \
	libsmraw_filename.c libsmraw_filename.h \
	libsmraw_handle.c libsmraw_handle.h \
	libsmraw_information_file.c libsmraw_information_file.h \
	libsmraw_io_handle.c libsmraw_io_handle.h \
	libsmraw_libbfio.h \
	libsmraw_libcerror.h \
	libsmraw_libclocale.h \
	libsmraw_libcnotify.h \
	libsmraw_libcthreads.h \
	libsmraw_libfdata.h \
	libsmraw_libfvalue.h \
	libsmraw_libuna.h \
	libsmraw_notify.c libsmraw_notify.h \
	libsmraw_support.c libsmraw_support.h \
	libsmraw_types.h \
	libsmraw_unused.h
endif

MAINTAINERCLEANFILES = \
	Makefile.in

distclean: clean
	/bin/rm -f Makefile

splint:
	@echo "Running splint on libsmraw ..."
	-splint -preproc -redef $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(libsmraw_la_SOURCES)

