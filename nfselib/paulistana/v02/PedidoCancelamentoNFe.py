#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated  by generateDS.py version 2.36.6.
# Python 3.6.9 (default, Apr 18 2020, 01:56:04)  [GCC 8.4.0]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('--no-dates', '')
#   ('--member-specs', 'list')
#   ('--use-getter-setter', 'none')
#   ('-f', '')
#   ('-o', '/home/luisotavio/Documentos/Projects/produto_12/src/nfselib.paulistana/paulistanalib/v02/PedidoCancelamentoNFe.py')
#
# Command line arguments:
#   /tmp/generated/schemas/paulistana/v02/PedidoCancelamentoNFe_v01.xsd
#
# Command line:
#   /home/luisotavio/Documentos/erpbrasil/bin/generateDS.py --no-namespace-defs --no-dates --member-specs="list" --use-getter-setter="none" -f -o "/home/luisotavio/Documentos/Projects/produto_12/src/nfselib.paulistana/paulistanalib/v02/PedidoCancelamentoNFe.py" /tmp/generated/schemas/paulistana/v02/PedidoCancelamentoNFe_v01.xsd
#
# Current working directory (os.getcwd()):
#   v02
#

from six.moves import zip_longest
import os
import sys
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ImportError:
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from .generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ImportError:
    GenerateDSNamespaceDefs_ = {}
try:
    from .generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ImportError:
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ImportError:

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ImportError:
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError as exp:
    
    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer valuess')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class tpOpcaoSimples(str, Enum):
    """Tipo referente às possíveis opções de escolha pelo Simples."""
    _0='0' # Não-optante pelo Simples Federal nem Municipal.
    _1='1' # Optante pelo Simples Federal (Alíquota de 1,0%).
    _2='2' # Optante pelo Simples Federal (Alíquota de 0,5%).
    _3='3' # Optante pelo Simples Municipal.


class tpStatusNFe(str, Enum):
    """Tipo referente aos possíveis status de NFS-e."""
    N='N' # Normal.
    C='C' # Cancelada.
    E='E' # Extraviada.


class tpTipoRPS(str, Enum):
    """Tipo referente aos possíveis tipos de RPS."""
    RPS='RPS' # Recibo Provisório de Serviços.
    RPSM='RPS-M' # Recibo Provisório de Serviços proveniente de Nota Fiscal Conjugada (Mista).
    RPSC='RPS-C' # Cupom.


class PedidoCancelamentoNFe(GeneratedsSuper):
    """Schema utilizado para PEDIDO de Cancelamento de NFS-e.Este Schema XML é
    utilizado pelos Prestadores de serviços cancelarem NFS-e emitidas por
    eles."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Cabecalho', 'CabecalhoType', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'Cabecalho', 'type': 'CabecalhoType'}, None),
        MemberSpec_('Detalhe', 'DetalheType', 1, 0, {'maxOccurs': '50', 'minOccurs': '1', 'name': 'Detalhe', 'type': 'DetalheType'}, None),
        MemberSpec_('Signature', 'SignatureType', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'Signature', 'ref': 'Signature', 'type': 'Signature'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Cabecalho=None, Detalhe=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Cabecalho = Cabecalho
        self.Cabecalho_nsprefix_ = None
        if Detalhe is None:
            self.Detalhe = []
        else:
            self.Detalhe = Detalhe
        self.Detalhe_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PedidoCancelamentoNFe)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PedidoCancelamentoNFe.subclass:
            return PedidoCancelamentoNFe.subclass(*args_, **kwargs_)
        else:
            return PedidoCancelamentoNFe(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Cabecalho is not None or
            self.Detalhe or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PedidoCancelamentoNFe', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PedidoCancelamentoNFe')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PedidoCancelamentoNFe':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PedidoCancelamentoNFe')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PedidoCancelamentoNFe', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PedidoCancelamentoNFe'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='PedidoCancelamentoNFe', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Cabecalho is not None:
            namespaceprefix_ = self.Cabecalho_nsprefix_ + ':' if (UseCapturedNS_ and self.Cabecalho_nsprefix_) else ''
            self.Cabecalho.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Cabecalho', pretty_print=pretty_print)
        for Detalhe_ in self.Detalhe:
            namespaceprefix_ = self.Detalhe_nsprefix_ + ':' if (UseCapturedNS_ and self.Detalhe_nsprefix_) else ''
            Detalhe_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Detalhe', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            self.Signature.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Cabecalho':
            obj_ = CabecalhoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Cabecalho = obj_
            obj_.original_tagname_ = 'Cabecalho'
        elif nodeName_ == 'Detalhe':
            obj_ = DetalheType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Detalhe.append(obj_)
            obj_.original_tagname_ = 'Detalhe'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'
# end class PedidoCancelamentoNFe


class tpEvento(GeneratedsSuper):
    """Chave para identificação da origem do evento."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Codigo', ['tpCodigoEvento', 'xs:short'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'Codigo', 'type': 'xs:short'}, None),
        MemberSpec_('Descricao', ['tpDescricaoEvento', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Descricao', 'type': 'xs:string'}, None),
        MemberSpec_('ChaveRPS', 'tpChaveRPS', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ChaveRPS', 'type': 'tpChaveRPS'}, 1),
        MemberSpec_('ChaveNFe', 'tpChaveNFe', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ChaveNFe', 'type': 'tpChaveNFe'}, 1),
    ]
    subclass = None
    superclass = None
    def __init__(self, Codigo=None, Descricao=None, ChaveRPS=None, ChaveNFe=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Codigo = Codigo
        self.validate_tpCodigoEvento(self.Codigo)
        self.Codigo_nsprefix_ = None
        self.Descricao = Descricao
        self.validate_tpDescricaoEvento(self.Descricao)
        self.Descricao_nsprefix_ = None
        self.ChaveRPS = ChaveRPS
        self.ChaveRPS_nsprefix_ = None
        self.ChaveNFe = ChaveNFe
        self.ChaveNFe_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpEvento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpEvento.subclass:
            return tpEvento.subclass(*args_, **kwargs_)
        else:
            return tpEvento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpCodigoEvento(self, value):
        result = True
        # Validate type tpCodigoEvento, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCodigoEvento_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCodigoEvento_patterns_, ))
                result = False
        return result
    validate_tpCodigoEvento_patterns_ = [['^([0-9]{3,4})$']]
    def validate_tpDescricaoEvento(self, value):
        result = True
        # Validate type tpDescricaoEvento, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 300:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpDescricaoEvento' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpDescricaoEvento' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.Codigo is not None or
            self.Descricao is not None or
            self.ChaveRPS is not None or
            self.ChaveNFe is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEvento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpEvento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpEvento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpEvento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpEvento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpEvento'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEvento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Codigo is not None:
            namespaceprefix_ = self.Codigo_nsprefix_ + ':' if (UseCapturedNS_ and self.Codigo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigo>%s</%sCodigo>%s' % (namespaceprefix_ , self.gds_format_integer(self.Codigo, input_name='Codigo'), namespaceprefix_ , eol_))
        if self.Descricao is not None:
            namespaceprefix_ = self.Descricao_nsprefix_ + ':' if (UseCapturedNS_ and self.Descricao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDescricao>%s</%sDescricao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Descricao), input_name='Descricao')), namespaceprefix_ , eol_))
        if self.ChaveRPS is not None:
            namespaceprefix_ = self.ChaveRPS_nsprefix_ + ':' if (UseCapturedNS_ and self.ChaveRPS_nsprefix_) else ''
            self.ChaveRPS.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChaveRPS', pretty_print=pretty_print)
        if self.ChaveNFe is not None:
            namespaceprefix_ = self.ChaveNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.ChaveNFe_nsprefix_) else ''
            self.ChaveNFe.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChaveNFe', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Codigo' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Codigo')
            ival_ = self.gds_validate_integer(ival_, node, 'Codigo')
            self.Codigo = ival_
            self.Codigo_nsprefix_ = child_.prefix
            # validate type tpCodigoEvento
            self.validate_tpCodigoEvento(self.Codigo)
        elif nodeName_ == 'Descricao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Descricao')
            value_ = self.gds_validate_string(value_, node, 'Descricao')
            self.Descricao = value_
            self.Descricao_nsprefix_ = child_.prefix
            # validate type tpDescricaoEvento
            self.validate_tpDescricaoEvento(self.Descricao)
        elif nodeName_ == 'ChaveRPS':
            obj_ = tpChaveRPS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChaveRPS = obj_
            obj_.original_tagname_ = 'ChaveRPS'
        elif nodeName_ == 'ChaveNFe':
            obj_ = tpChaveNFe.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChaveNFe = obj_
            obj_.original_tagname_ = 'ChaveNFe'
# end class tpEvento


class tpCPFCNPJ(GeneratedsSuper):
    """Tipo que representa um CPF/CNPJ."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('CPF', ['tpCPF', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CPF', 'type': 'xs:string'}, 2),
        MemberSpec_('CNPJ', ['tpCNPJ', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CNPJ', 'type': 'xs:string'}, 2),
    ]
    subclass = None
    superclass = None
    def __init__(self, CPF=None, CNPJ=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CPF = CPF
        self.validate_tpCPF(self.CPF)
        self.CPF_nsprefix_ = None
        self.CNPJ = CNPJ
        self.validate_tpCNPJ(self.CNPJ)
        self.CNPJ_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpCPFCNPJ)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpCPFCNPJ.subclass:
            return tpCPFCNPJ.subclass(*args_, **kwargs_)
        else:
            return tpCPFCNPJ(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpCPF(self, value):
        result = True
        # Validate type tpCPF, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCPF_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCPF_patterns_, ))
                result = False
        return result
    validate_tpCPF_patterns_ = [['^([0-9]{0}|[0-9]{11})$']]
    def validate_tpCNPJ(self, value):
        result = True
        # Validate type tpCNPJ, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCNPJ_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCNPJ_patterns_, ))
                result = False
        return result
    validate_tpCNPJ_patterns_ = [['^([0-9]{14})$']]
    def hasContent_(self):
        if (
            self.CPF is not None or
            self.CNPJ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpCPFCNPJ', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpCPFCNPJ')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpCPFCNPJ':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpCPFCNPJ')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpCPFCNPJ', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpCPFCNPJ'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpCPFCNPJ', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CPF is not None:
            namespaceprefix_ = self.CPF_nsprefix_ + ':' if (UseCapturedNS_ and self.CPF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCPF>%s</%sCPF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CPF), input_name='CPF')), namespaceprefix_ , eol_))
        if self.CNPJ is not None:
            namespaceprefix_ = self.CNPJ_nsprefix_ + ':' if (UseCapturedNS_ and self.CNPJ_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCNPJ>%s</%sCNPJ>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CNPJ), input_name='CNPJ')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CPF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CPF')
            value_ = self.gds_validate_string(value_, node, 'CPF')
            self.CPF = value_
            self.CPF_nsprefix_ = child_.prefix
            # validate type tpCPF
            self.validate_tpCPF(self.CPF)
        elif nodeName_ == 'CNPJ':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CNPJ')
            value_ = self.gds_validate_string(value_, node, 'CNPJ')
            self.CNPJ = value_
            self.CNPJ_nsprefix_ = child_.prefix
            # validate type tpCNPJ
            self.validate_tpCNPJ(self.CNPJ)
# end class tpCPFCNPJ


class tpChaveNFeRPS(GeneratedsSuper):
    """Tipo que representa a chave de uma NFS-e e a Chave do RPS que a mesma
    substitui."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('ChaveNFe', 'tpChaveNFe', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ChaveNFe', 'type': 'tpChaveNFe'}, None),
        MemberSpec_('ChaveRPS', 'tpChaveRPS', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ChaveRPS', 'type': 'tpChaveRPS'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, ChaveNFe=None, ChaveRPS=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ChaveNFe = ChaveNFe
        self.ChaveNFe_nsprefix_ = None
        self.ChaveRPS = ChaveRPS
        self.ChaveRPS_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpChaveNFeRPS)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpChaveNFeRPS.subclass:
            return tpChaveNFeRPS.subclass(*args_, **kwargs_)
        else:
            return tpChaveNFeRPS(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.ChaveNFe is not None or
            self.ChaveRPS is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpChaveNFeRPS', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpChaveNFeRPS')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpChaveNFeRPS':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpChaveNFeRPS')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpChaveNFeRPS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpChaveNFeRPS'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpChaveNFeRPS', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ChaveNFe is not None:
            namespaceprefix_ = self.ChaveNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.ChaveNFe_nsprefix_) else ''
            self.ChaveNFe.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChaveNFe', pretty_print=pretty_print)
        if self.ChaveRPS is not None:
            namespaceprefix_ = self.ChaveRPS_nsprefix_ + ':' if (UseCapturedNS_ and self.ChaveRPS_nsprefix_) else ''
            self.ChaveRPS.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChaveRPS', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ChaveNFe':
            obj_ = tpChaveNFe.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChaveNFe = obj_
            obj_.original_tagname_ = 'ChaveNFe'
        elif nodeName_ == 'ChaveRPS':
            obj_ = tpChaveRPS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChaveRPS = obj_
            obj_.original_tagname_ = 'ChaveRPS'
# end class tpChaveNFeRPS


class tpChaveNFe(GeneratedsSuper):
    """Chave de identificação da NFS-e."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('InscricaoPrestador', ['tpInscricaoMunicipal', 'xs:long'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'InscricaoPrestador', 'type': 'xs:long'}, None),
        MemberSpec_('NumeroNFe', ['tpNumero', 'xs:long'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'NumeroNFe', 'type': 'xs:long'}, None),
        MemberSpec_('CodigoVerificacao', ['tpCodigoVerificacao', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CodigoVerificacao', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, InscricaoPrestador=None, NumeroNFe=None, CodigoVerificacao=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.InscricaoPrestador = InscricaoPrestador
        self.validate_tpInscricaoMunicipal(self.InscricaoPrestador)
        self.InscricaoPrestador_nsprefix_ = None
        self.NumeroNFe = NumeroNFe
        self.validate_tpNumero(self.NumeroNFe)
        self.NumeroNFe_nsprefix_ = None
        self.CodigoVerificacao = CodigoVerificacao
        self.validate_tpCodigoVerificacao(self.CodigoVerificacao)
        self.CodigoVerificacao_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpChaveNFe)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpChaveNFe.subclass:
            return tpChaveNFe.subclass(*args_, **kwargs_)
        else:
            return tpChaveNFe(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpInscricaoMunicipal(self, value):
        result = True
        # Validate type tpInscricaoMunicipal, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpInscricaoMunicipal_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpInscricaoMunicipal_patterns_, ))
                result = False
        return result
    validate_tpInscricaoMunicipal_patterns_ = [['^([0-9]{8,8})$']]
    def validate_tpNumero(self, value):
        result = True
        # Validate type tpNumero, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpNumero_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpNumero_patterns_, ))
                result = False
        return result
    validate_tpNumero_patterns_ = [['^([0-9]{1,12})$']]
    def validate_tpCodigoVerificacao(self, value):
        result = True
        # Validate type tpCodigoVerificacao, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpCodigoVerificacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpCodigoVerificacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.InscricaoPrestador is not None or
            self.NumeroNFe is not None or
            self.CodigoVerificacao is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpChaveNFe', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpChaveNFe')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpChaveNFe':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpChaveNFe')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpChaveNFe', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpChaveNFe'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpChaveNFe', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.InscricaoPrestador is not None:
            namespaceprefix_ = self.InscricaoPrestador_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoPrestador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoPrestador>%s</%sInscricaoPrestador>%s' % (namespaceprefix_ , self.gds_format_integer(self.InscricaoPrestador, input_name='InscricaoPrestador'), namespaceprefix_ , eol_))
        if self.NumeroNFe is not None:
            namespaceprefix_ = self.NumeroNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.NumeroNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumeroNFe>%s</%sNumeroNFe>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumeroNFe, input_name='NumeroNFe'), namespaceprefix_ , eol_))
        if self.CodigoVerificacao is not None:
            namespaceprefix_ = self.CodigoVerificacao_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoVerificacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoVerificacao>%s</%sCodigoVerificacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CodigoVerificacao), input_name='CodigoVerificacao')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'InscricaoPrestador' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'InscricaoPrestador')
            ival_ = self.gds_validate_integer(ival_, node, 'InscricaoPrestador')
            self.InscricaoPrestador = ival_
            self.InscricaoPrestador_nsprefix_ = child_.prefix
            # validate type tpInscricaoMunicipal
            self.validate_tpInscricaoMunicipal(self.InscricaoPrestador)
        elif nodeName_ == 'NumeroNFe' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumeroNFe')
            ival_ = self.gds_validate_integer(ival_, node, 'NumeroNFe')
            self.NumeroNFe = ival_
            self.NumeroNFe_nsprefix_ = child_.prefix
            # validate type tpNumero
            self.validate_tpNumero(self.NumeroNFe)
        elif nodeName_ == 'CodigoVerificacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CodigoVerificacao')
            value_ = self.gds_validate_string(value_, node, 'CodigoVerificacao')
            self.CodigoVerificacao = value_
            self.CodigoVerificacao_nsprefix_ = child_.prefix
            # validate type tpCodigoVerificacao
            self.validate_tpCodigoVerificacao(self.CodigoVerificacao)
# end class tpChaveNFe


class tpChaveRPS(GeneratedsSuper):
    """Tipo que define a chave identificadora de um RPS."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('InscricaoPrestador', ['tpInscricaoMunicipal', 'xs:long'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'InscricaoPrestador', 'type': 'xs:long'}, None),
        MemberSpec_('SerieRPS', ['tpSerieRPS', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'SerieRPS', 'type': 'xs:string'}, None),
        MemberSpec_('NumeroRPS', ['tpNumero', 'xs:long'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'NumeroRPS', 'type': 'xs:long'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, InscricaoPrestador=None, SerieRPS=None, NumeroRPS=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.InscricaoPrestador = InscricaoPrestador
        self.validate_tpInscricaoMunicipal(self.InscricaoPrestador)
        self.InscricaoPrestador_nsprefix_ = None
        self.SerieRPS = SerieRPS
        self.validate_tpSerieRPS(self.SerieRPS)
        self.SerieRPS_nsprefix_ = None
        self.NumeroRPS = NumeroRPS
        self.validate_tpNumero(self.NumeroRPS)
        self.NumeroRPS_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpChaveRPS)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpChaveRPS.subclass:
            return tpChaveRPS.subclass(*args_, **kwargs_)
        else:
            return tpChaveRPS(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpInscricaoMunicipal(self, value):
        result = True
        # Validate type tpInscricaoMunicipal, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpInscricaoMunicipal_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpInscricaoMunicipal_patterns_, ))
                result = False
        return result
    validate_tpInscricaoMunicipal_patterns_ = [['^([0-9]{8,8})$']]
    def validate_tpSerieRPS(self, value):
        result = True
        # Validate type tpSerieRPS, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpSerieRPS' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpSerieRPS' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpNumero(self, value):
        result = True
        # Validate type tpNumero, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpNumero_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpNumero_patterns_, ))
                result = False
        return result
    validate_tpNumero_patterns_ = [['^([0-9]{1,12})$']]
    def hasContent_(self):
        if (
            self.InscricaoPrestador is not None or
            self.SerieRPS is not None or
            self.NumeroRPS is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpChaveRPS', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpChaveRPS')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpChaveRPS':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpChaveRPS')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpChaveRPS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpChaveRPS'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpChaveRPS', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.InscricaoPrestador is not None:
            namespaceprefix_ = self.InscricaoPrestador_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoPrestador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoPrestador>%s</%sInscricaoPrestador>%s' % (namespaceprefix_ , self.gds_format_integer(self.InscricaoPrestador, input_name='InscricaoPrestador'), namespaceprefix_ , eol_))
        if self.SerieRPS is not None:
            namespaceprefix_ = self.SerieRPS_nsprefix_ + ':' if (UseCapturedNS_ and self.SerieRPS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSerieRPS>%s</%sSerieRPS>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SerieRPS), input_name='SerieRPS')), namespaceprefix_ , eol_))
        if self.NumeroRPS is not None:
            namespaceprefix_ = self.NumeroRPS_nsprefix_ + ':' if (UseCapturedNS_ and self.NumeroRPS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumeroRPS>%s</%sNumeroRPS>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumeroRPS, input_name='NumeroRPS'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'InscricaoPrestador' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'InscricaoPrestador')
            ival_ = self.gds_validate_integer(ival_, node, 'InscricaoPrestador')
            self.InscricaoPrestador = ival_
            self.InscricaoPrestador_nsprefix_ = child_.prefix
            # validate type tpInscricaoMunicipal
            self.validate_tpInscricaoMunicipal(self.InscricaoPrestador)
        elif nodeName_ == 'SerieRPS':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SerieRPS')
            value_ = self.gds_validate_string(value_, node, 'SerieRPS')
            self.SerieRPS = value_
            self.SerieRPS_nsprefix_ = child_.prefix
            # validate type tpSerieRPS
            self.validate_tpSerieRPS(self.SerieRPS)
        elif nodeName_ == 'NumeroRPS' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumeroRPS')
            ival_ = self.gds_validate_integer(ival_, node, 'NumeroRPS')
            self.NumeroRPS = ival_
            self.NumeroRPS_nsprefix_ = child_.prefix
            # validate type tpNumero
            self.validate_tpNumero(self.NumeroRPS)
# end class tpChaveRPS


class tpEndereco(GeneratedsSuper):
    """Tipo Endereço."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('TipoLogradouro', ['tpTipoLogradouro', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'TipoLogradouro', 'type': 'xs:string'}, None),
        MemberSpec_('Logradouro', ['tpLogradouro', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Logradouro', 'type': 'xs:string'}, None),
        MemberSpec_('NumeroEndereco', ['tpNumeroEndereco', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'NumeroEndereco', 'type': 'xs:string'}, None),
        MemberSpec_('ComplementoEndereco', ['tpComplementoEndereco', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ComplementoEndereco', 'type': 'xs:string'}, None),
        MemberSpec_('Bairro', ['tpBairro', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Bairro', 'type': 'xs:string'}, None),
        MemberSpec_('Cidade', ['tpCidade', 'xs:int'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Cidade', 'type': 'xs:int'}, None),
        MemberSpec_('UF', ['tpUF', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'UF', 'type': 'xs:string'}, None),
        MemberSpec_('CEP', ['tpCEP', 'xs:int'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CEP', 'type': 'xs:int'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, TipoLogradouro=None, Logradouro=None, NumeroEndereco=None, ComplementoEndereco=None, Bairro=None, Cidade=None, UF=None, CEP=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TipoLogradouro = TipoLogradouro
        self.validate_tpTipoLogradouro(self.TipoLogradouro)
        self.TipoLogradouro_nsprefix_ = None
        self.Logradouro = Logradouro
        self.validate_tpLogradouro(self.Logradouro)
        self.Logradouro_nsprefix_ = None
        self.NumeroEndereco = NumeroEndereco
        self.validate_tpNumeroEndereco(self.NumeroEndereco)
        self.NumeroEndereco_nsprefix_ = None
        self.ComplementoEndereco = ComplementoEndereco
        self.validate_tpComplementoEndereco(self.ComplementoEndereco)
        self.ComplementoEndereco_nsprefix_ = None
        self.Bairro = Bairro
        self.validate_tpBairro(self.Bairro)
        self.Bairro_nsprefix_ = None
        self.Cidade = Cidade
        self.validate_tpCidade(self.Cidade)
        self.Cidade_nsprefix_ = None
        self.UF = UF
        self.validate_tpUF(self.UF)
        self.UF_nsprefix_ = None
        self.CEP = CEP
        self.validate_tpCEP(self.CEP)
        self.CEP_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpEndereco)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpEndereco.subclass:
            return tpEndereco.subclass(*args_, **kwargs_)
        else:
            return tpEndereco(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpTipoLogradouro(self, value):
        result = True
        # Validate type tpTipoLogradouro, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpTipoLogradouro' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpTipoLogradouro' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpLogradouro(self, value):
        result = True
        # Validate type tpLogradouro, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpLogradouro' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpLogradouro' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpNumeroEndereco(self, value):
        result = True
        # Validate type tpNumeroEndereco, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpNumeroEndereco' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpNumeroEndereco' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpComplementoEndereco(self, value):
        result = True
        # Validate type tpComplementoEndereco, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpComplementoEndereco' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpComplementoEndereco' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpBairro(self, value):
        result = True
        # Validate type tpBairro, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpBairro' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpBairro' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpCidade(self, value):
        result = True
        # Validate type tpCidade, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCidade_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCidade_patterns_, ))
                result = False
        return result
    validate_tpCidade_patterns_ = [['^([0-9]{7})$']]
    def validate_tpUF(self, value):
        result = True
        # Validate type tpUF, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpUF' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpUF' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpCEP(self, value):
        result = True
        # Validate type tpCEP, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCEP_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCEP_patterns_, ))
                result = False
        return result
    validate_tpCEP_patterns_ = [['^([0-9]{7,8})$']]
    def hasContent_(self):
        if (
            self.TipoLogradouro is not None or
            self.Logradouro is not None or
            self.NumeroEndereco is not None or
            self.ComplementoEndereco is not None or
            self.Bairro is not None or
            self.Cidade is not None or
            self.UF is not None or
            self.CEP is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEndereco', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpEndereco')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpEndereco':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpEndereco')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpEndereco', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpEndereco'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEndereco', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TipoLogradouro is not None:
            namespaceprefix_ = self.TipoLogradouro_nsprefix_ + ':' if (UseCapturedNS_ and self.TipoLogradouro_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTipoLogradouro>%s</%sTipoLogradouro>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TipoLogradouro), input_name='TipoLogradouro')), namespaceprefix_ , eol_))
        if self.Logradouro is not None:
            namespaceprefix_ = self.Logradouro_nsprefix_ + ':' if (UseCapturedNS_ and self.Logradouro_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLogradouro>%s</%sLogradouro>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Logradouro), input_name='Logradouro')), namespaceprefix_ , eol_))
        if self.NumeroEndereco is not None:
            namespaceprefix_ = self.NumeroEndereco_nsprefix_ + ':' if (UseCapturedNS_ and self.NumeroEndereco_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumeroEndereco>%s</%sNumeroEndereco>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NumeroEndereco), input_name='NumeroEndereco')), namespaceprefix_ , eol_))
        if self.ComplementoEndereco is not None:
            namespaceprefix_ = self.ComplementoEndereco_nsprefix_ + ':' if (UseCapturedNS_ and self.ComplementoEndereco_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sComplementoEndereco>%s</%sComplementoEndereco>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ComplementoEndereco), input_name='ComplementoEndereco')), namespaceprefix_ , eol_))
        if self.Bairro is not None:
            namespaceprefix_ = self.Bairro_nsprefix_ + ':' if (UseCapturedNS_ and self.Bairro_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sBairro>%s</%sBairro>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Bairro), input_name='Bairro')), namespaceprefix_ , eol_))
        if self.Cidade is not None:
            namespaceprefix_ = self.Cidade_nsprefix_ + ':' if (UseCapturedNS_ and self.Cidade_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCidade>%s</%sCidade>%s' % (namespaceprefix_ , self.gds_format_integer(self.Cidade, input_name='Cidade'), namespaceprefix_ , eol_))
        if self.UF is not None:
            namespaceprefix_ = self.UF_nsprefix_ + ':' if (UseCapturedNS_ and self.UF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUF>%s</%sUF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.UF), input_name='UF')), namespaceprefix_ , eol_))
        if self.CEP is not None:
            namespaceprefix_ = self.CEP_nsprefix_ + ':' if (UseCapturedNS_ and self.CEP_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCEP>%s</%sCEP>%s' % (namespaceprefix_ , self.gds_format_integer(self.CEP, input_name='CEP'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TipoLogradouro':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TipoLogradouro')
            value_ = self.gds_validate_string(value_, node, 'TipoLogradouro')
            self.TipoLogradouro = value_
            self.TipoLogradouro_nsprefix_ = child_.prefix
            # validate type tpTipoLogradouro
            self.validate_tpTipoLogradouro(self.TipoLogradouro)
        elif nodeName_ == 'Logradouro':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Logradouro')
            value_ = self.gds_validate_string(value_, node, 'Logradouro')
            self.Logradouro = value_
            self.Logradouro_nsprefix_ = child_.prefix
            # validate type tpLogradouro
            self.validate_tpLogradouro(self.Logradouro)
        elif nodeName_ == 'NumeroEndereco':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NumeroEndereco')
            value_ = self.gds_validate_string(value_, node, 'NumeroEndereco')
            self.NumeroEndereco = value_
            self.NumeroEndereco_nsprefix_ = child_.prefix
            # validate type tpNumeroEndereco
            self.validate_tpNumeroEndereco(self.NumeroEndereco)
        elif nodeName_ == 'ComplementoEndereco':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ComplementoEndereco')
            value_ = self.gds_validate_string(value_, node, 'ComplementoEndereco')
            self.ComplementoEndereco = value_
            self.ComplementoEndereco_nsprefix_ = child_.prefix
            # validate type tpComplementoEndereco
            self.validate_tpComplementoEndereco(self.ComplementoEndereco)
        elif nodeName_ == 'Bairro':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Bairro')
            value_ = self.gds_validate_string(value_, node, 'Bairro')
            self.Bairro = value_
            self.Bairro_nsprefix_ = child_.prefix
            # validate type tpBairro
            self.validate_tpBairro(self.Bairro)
        elif nodeName_ == 'Cidade' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'Cidade')
            ival_ = self.gds_validate_integer(ival_, node, 'Cidade')
            self.Cidade = ival_
            self.Cidade_nsprefix_ = child_.prefix
            # validate type tpCidade
            self.validate_tpCidade(self.Cidade)
        elif nodeName_ == 'UF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'UF')
            value_ = self.gds_validate_string(value_, node, 'UF')
            self.UF = value_
            self.UF_nsprefix_ = child_.prefix
            # validate type tpUF
            self.validate_tpUF(self.UF)
        elif nodeName_ == 'CEP' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CEP')
            ival_ = self.gds_validate_integer(ival_, node, 'CEP')
            self.CEP = ival_
            self.CEP_nsprefix_ = child_.prefix
            # validate type tpCEP
            self.validate_tpCEP(self.CEP)
# end class tpEndereco


class tpInformacoesLote(GeneratedsSuper):
    """Informações do lote processado."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('NumeroLote', ['tpNumero', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'NumeroLote', 'type': 'xs:long'}, None),
        MemberSpec_('InscricaoPrestador', ['tpInscricaoMunicipal', 'xs:long'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'InscricaoPrestador', 'type': 'xs:long'}, None),
        MemberSpec_('CPFCNPJRemetente', 'tpCPFCNPJ', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CPFCNPJRemetente', 'type': 'tpCPFCNPJ'}, None),
        MemberSpec_('DataEnvioLote', 'xs:dateTime', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'DataEnvioLote', 'type': 'xs:dateTime'}, None),
        MemberSpec_('QtdNotasProcessadas', ['tpQuantidade', 'xs:long'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'QtdNotasProcessadas', 'type': 'xs:long'}, None),
        MemberSpec_('TempoProcessamento', ['tpTempoProcessamento', 'xs:long'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'TempoProcessamento', 'type': 'xs:long'}, None),
        MemberSpec_('ValorTotalServicos', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorTotalServicos', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorTotalDeducoes', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorTotalDeducoes', 'type': 'xs:decimal'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, NumeroLote=None, InscricaoPrestador=None, CPFCNPJRemetente=None, DataEnvioLote=None, QtdNotasProcessadas=None, TempoProcessamento=None, ValorTotalServicos=None, ValorTotalDeducoes=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.NumeroLote = NumeroLote
        self.validate_tpNumero(self.NumeroLote)
        self.NumeroLote_nsprefix_ = None
        self.InscricaoPrestador = InscricaoPrestador
        self.validate_tpInscricaoMunicipal(self.InscricaoPrestador)
        self.InscricaoPrestador_nsprefix_ = None
        self.CPFCNPJRemetente = CPFCNPJRemetente
        self.CPFCNPJRemetente_nsprefix_ = None
        if isinstance(DataEnvioLote, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataEnvioLote, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = DataEnvioLote
        self.DataEnvioLote = initvalue_
        self.DataEnvioLote_nsprefix_ = None
        self.QtdNotasProcessadas = QtdNotasProcessadas
        self.validate_tpQuantidade(self.QtdNotasProcessadas)
        self.QtdNotasProcessadas_nsprefix_ = None
        self.TempoProcessamento = TempoProcessamento
        self.validate_tpTempoProcessamento(self.TempoProcessamento)
        self.TempoProcessamento_nsprefix_ = None
        self.ValorTotalServicos = ValorTotalServicos
        self.validate_tpValor(self.ValorTotalServicos)
        self.ValorTotalServicos_nsprefix_ = None
        self.ValorTotalDeducoes = ValorTotalDeducoes
        self.validate_tpValor(self.ValorTotalDeducoes)
        self.ValorTotalDeducoes_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpInformacoesLote)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpInformacoesLote.subclass:
            return tpInformacoesLote.subclass(*args_, **kwargs_)
        else:
            return tpInformacoesLote(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpNumero(self, value):
        result = True
        # Validate type tpNumero, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpNumero_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpNumero_patterns_, ))
                result = False
        return result
    validate_tpNumero_patterns_ = [['^([0-9]{1,12})$']]
    def validate_tpInscricaoMunicipal(self, value):
        result = True
        # Validate type tpInscricaoMunicipal, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpInscricaoMunicipal_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpInscricaoMunicipal_patterns_, ))
                result = False
        return result
    validate_tpInscricaoMunicipal_patterns_ = [['^([0-9]{8,8})$']]
    def validate_tpQuantidade(self, value):
        result = True
        # Validate type tpQuantidade, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpQuantidade_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpQuantidade_patterns_, ))
                result = False
        return result
    validate_tpQuantidade_patterns_ = [['^([0-9]{1,15})$']]
    def validate_tpTempoProcessamento(self, value):
        result = True
        # Validate type tpTempoProcessamento, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpTempoProcessamento_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpTempoProcessamento_patterns_, ))
                result = False
        return result
    validate_tpTempoProcessamento_patterns_ = [['^([0-9]{1,15})$']]
    def validate_tpValor(self, value):
        result = True
        # Validate type tpValor, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on tpValor' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tpValor' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpValor_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpValor_patterns_, ))
                result = False
        return result
    validate_tpValor_patterns_ = [['^(0|0\\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\\.[0-9]{0,2})?)$']]
    def hasContent_(self):
        if (
            self.NumeroLote is not None or
            self.InscricaoPrestador is not None or
            self.CPFCNPJRemetente is not None or
            self.DataEnvioLote is not None or
            self.QtdNotasProcessadas is not None or
            self.TempoProcessamento is not None or
            self.ValorTotalServicos is not None or
            self.ValorTotalDeducoes is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpInformacoesLote', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpInformacoesLote')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpInformacoesLote':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpInformacoesLote')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpInformacoesLote', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpInformacoesLote'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpInformacoesLote', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.NumeroLote is not None:
            namespaceprefix_ = self.NumeroLote_nsprefix_ + ':' if (UseCapturedNS_ and self.NumeroLote_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumeroLote>%s</%sNumeroLote>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumeroLote, input_name='NumeroLote'), namespaceprefix_ , eol_))
        if self.InscricaoPrestador is not None:
            namespaceprefix_ = self.InscricaoPrestador_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoPrestador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoPrestador>%s</%sInscricaoPrestador>%s' % (namespaceprefix_ , self.gds_format_integer(self.InscricaoPrestador, input_name='InscricaoPrestador'), namespaceprefix_ , eol_))
        if self.CPFCNPJRemetente is not None:
            namespaceprefix_ = self.CPFCNPJRemetente_nsprefix_ + ':' if (UseCapturedNS_ and self.CPFCNPJRemetente_nsprefix_) else ''
            self.CPFCNPJRemetente.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CPFCNPJRemetente', pretty_print=pretty_print)
        if self.DataEnvioLote is not None:
            namespaceprefix_ = self.DataEnvioLote_nsprefix_ + ':' if (UseCapturedNS_ and self.DataEnvioLote_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataEnvioLote>%s</%sDataEnvioLote>%s' % (namespaceprefix_ , self.gds_format_datetime(self.DataEnvioLote, input_name='DataEnvioLote'), namespaceprefix_ , eol_))
        if self.QtdNotasProcessadas is not None:
            namespaceprefix_ = self.QtdNotasProcessadas_nsprefix_ + ':' if (UseCapturedNS_ and self.QtdNotasProcessadas_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sQtdNotasProcessadas>%s</%sQtdNotasProcessadas>%s' % (namespaceprefix_ , self.gds_format_integer(self.QtdNotasProcessadas, input_name='QtdNotasProcessadas'), namespaceprefix_ , eol_))
        if self.TempoProcessamento is not None:
            namespaceprefix_ = self.TempoProcessamento_nsprefix_ + ':' if (UseCapturedNS_ and self.TempoProcessamento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTempoProcessamento>%s</%sTempoProcessamento>%s' % (namespaceprefix_ , self.gds_format_integer(self.TempoProcessamento, input_name='TempoProcessamento'), namespaceprefix_ , eol_))
        if self.ValorTotalServicos is not None:
            namespaceprefix_ = self.ValorTotalServicos_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorTotalServicos_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorTotalServicos>%s</%sValorTotalServicos>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorTotalServicos, input_name='ValorTotalServicos'), namespaceprefix_ , eol_))
        if self.ValorTotalDeducoes is not None:
            namespaceprefix_ = self.ValorTotalDeducoes_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorTotalDeducoes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorTotalDeducoes>%s</%sValorTotalDeducoes>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorTotalDeducoes, input_name='ValorTotalDeducoes'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'NumeroLote' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumeroLote')
            ival_ = self.gds_validate_integer(ival_, node, 'NumeroLote')
            self.NumeroLote = ival_
            self.NumeroLote_nsprefix_ = child_.prefix
            # validate type tpNumero
            self.validate_tpNumero(self.NumeroLote)
        elif nodeName_ == 'InscricaoPrestador' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'InscricaoPrestador')
            ival_ = self.gds_validate_integer(ival_, node, 'InscricaoPrestador')
            self.InscricaoPrestador = ival_
            self.InscricaoPrestador_nsprefix_ = child_.prefix
            # validate type tpInscricaoMunicipal
            self.validate_tpInscricaoMunicipal(self.InscricaoPrestador)
        elif nodeName_ == 'CPFCNPJRemetente':
            obj_ = tpCPFCNPJ.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CPFCNPJRemetente = obj_
            obj_.original_tagname_ = 'CPFCNPJRemetente'
        elif nodeName_ == 'DataEnvioLote':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.DataEnvioLote = dval_
            self.DataEnvioLote_nsprefix_ = child_.prefix
        elif nodeName_ == 'QtdNotasProcessadas' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'QtdNotasProcessadas')
            ival_ = self.gds_validate_integer(ival_, node, 'QtdNotasProcessadas')
            self.QtdNotasProcessadas = ival_
            self.QtdNotasProcessadas_nsprefix_ = child_.prefix
            # validate type tpQuantidade
            self.validate_tpQuantidade(self.QtdNotasProcessadas)
        elif nodeName_ == 'TempoProcessamento' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'TempoProcessamento')
            ival_ = self.gds_validate_integer(ival_, node, 'TempoProcessamento')
            self.TempoProcessamento = ival_
            self.TempoProcessamento_nsprefix_ = child_.prefix
            # validate type tpTempoProcessamento
            self.validate_tpTempoProcessamento(self.TempoProcessamento)
        elif nodeName_ == 'ValorTotalServicos' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorTotalServicos')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorTotalServicos')
            self.ValorTotalServicos = fval_
            self.ValorTotalServicos_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorTotalServicos)
        elif nodeName_ == 'ValorTotalDeducoes' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorTotalDeducoes')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorTotalDeducoes')
            self.ValorTotalDeducoes = fval_
            self.ValorTotalDeducoes_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorTotalDeducoes)
# end class tpInformacoesLote


class tpNFe(GeneratedsSuper):
    """Tipo que representa uma NFS-e"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Assinatura', ['tpAssinatura', 'xs:base64Binary'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Assinatura', 'type': 'xs:base64Binary'}, None),
        MemberSpec_('ChaveNFe', 'tpChaveNFe', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ChaveNFe', 'type': 'tpChaveNFe'}, None),
        MemberSpec_('DataEmissaoNFe', 'xs:dateTime', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'DataEmissaoNFe', 'type': 'xs:dateTime'}, None),
        MemberSpec_('NumeroLote', ['tpNumero', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'NumeroLote', 'type': 'xs:long'}, None),
        MemberSpec_('ChaveRPS', 'tpChaveRPS', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ChaveRPS', 'type': 'tpChaveRPS'}, None),
        MemberSpec_('TipoRPS', ['tpTipoRPS', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'TipoRPS', 'type': 'xs:string'}, None),
        MemberSpec_('DataEmissaoRPS', 'xs:date', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'DataEmissaoRPS', 'type': 'xs:date'}, None),
        MemberSpec_('CPFCNPJPrestador', 'tpCPFCNPJ', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CPFCNPJPrestador', 'type': 'tpCPFCNPJ'}, None),
        MemberSpec_('RazaoSocialPrestador', ['tpRazaoSocial', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'RazaoSocialPrestador', 'type': 'xs:string'}, None),
        MemberSpec_('EnderecoPrestador', 'tpEndereco', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'EnderecoPrestador', 'type': 'tpEndereco'}, None),
        MemberSpec_('EmailPrestador', ['tpEmail', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'EmailPrestador', 'type': 'xs:string'}, None),
        MemberSpec_('StatusNFe', ['tpStatusNFe', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'StatusNFe', 'type': 'xs:string'}, None),
        MemberSpec_('DataCancelamento', 'xs:dateTime', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'DataCancelamento', 'type': 'xs:dateTime'}, None),
        MemberSpec_('TributacaoNFe', ['tpTributacaoNFe', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'TributacaoNFe', 'type': 'xs:string'}, None),
        MemberSpec_('OpcaoSimples', ['tpOpcaoSimples', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'OpcaoSimples', 'type': 'xs:string'}, None),
        MemberSpec_('NumeroGuia', ['tpNumero', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'NumeroGuia', 'type': 'xs:long'}, None),
        MemberSpec_('DataQuitacaoGuia', 'xs:date', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'DataQuitacaoGuia', 'type': 'xs:date'}, None),
        MemberSpec_('ValorServicos', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorServicos', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorDeducoes', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorDeducoes', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorPIS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorPIS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorCOFINS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorCOFINS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorINSS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorINSS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorIR', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorIR', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorCSLL', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorCSLL', 'type': 'xs:decimal'}, None),
        MemberSpec_('CodigoServico', ['tpCodigoServico', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CodigoServico', 'type': 'xs:int'}, None),
        MemberSpec_('AliquotaServicos', ['tpAliquota', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'AliquotaServicos', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorISS', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorISS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorCredito', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorCredito', 'type': 'xs:decimal'}, None),
        MemberSpec_('ISSRetido', 'xs:boolean', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ISSRetido', 'type': 'xs:boolean'}, None),
        MemberSpec_('CPFCNPJTomador', 'tpCPFCNPJ', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CPFCNPJTomador', 'type': 'tpCPFCNPJ'}, None),
        MemberSpec_('InscricaoMunicipalTomador', ['tpInscricaoMunicipal', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'InscricaoMunicipalTomador', 'type': 'xs:long'}, None),
        MemberSpec_('InscricaoEstadualTomador', ['tpInscricaoEstadual', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'InscricaoEstadualTomador', 'type': 'xs:long'}, None),
        MemberSpec_('RazaoSocialTomador', ['tpRazaoSocial', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'RazaoSocialTomador', 'type': 'xs:string'}, None),
        MemberSpec_('EnderecoTomador', 'tpEndereco', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'EnderecoTomador', 'type': 'tpEndereco'}, None),
        MemberSpec_('EmailTomador', ['tpEmail', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'EmailTomador', 'type': 'xs:string'}, None),
        MemberSpec_('CPFCNPJIntermediario', 'tpCPFCNPJ', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CPFCNPJIntermediario', 'type': 'tpCPFCNPJ'}, None),
        MemberSpec_('InscricaoMunicipalIntermediario', ['tpInscricaoMunicipal', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'InscricaoMunicipalIntermediario', 'type': 'xs:long'}, None),
        MemberSpec_('ISSRetidoIntermediario', 'xs:string', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ISSRetidoIntermediario', 'type': 'xs:string'}, None),
        MemberSpec_('EmailIntermediario', ['tpEmail', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'EmailIntermediario', 'type': 'xs:string'}, None),
        MemberSpec_('Discriminacao', ['tpDiscriminacao', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'Discriminacao', 'type': 'xs:string'}, None),
        MemberSpec_('ValorCargaTributaria', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorCargaTributaria', 'type': 'xs:decimal'}, None),
        MemberSpec_('PercentualCargaTributaria', ['tpPercentualCargaTributaria', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'PercentualCargaTributaria', 'type': 'xs:decimal'}, None),
        MemberSpec_('FonteCargaTributaria', ['tpFonteCargaTributaria', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'FonteCargaTributaria', 'type': 'xs:string'}, None),
        MemberSpec_('CodigoCEI', ['tpNumero', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CodigoCEI', 'type': 'xs:long'}, None),
        MemberSpec_('MatriculaObra', ['tpNumero', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'MatriculaObra', 'type': 'xs:long'}, None),
        MemberSpec_('MunicipioPrestacao', ['tpCidade', 'xs:int'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'MunicipioPrestacao', 'type': 'xs:int'}, None),
        MemberSpec_('NumeroEncapsulamento', ['tpNumero', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'NumeroEncapsulamento', 'type': 'xs:long'}, None),
        MemberSpec_('ValorTotalRecebido', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorTotalRecebido', 'type': 'xs:decimal'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Assinatura=None, ChaveNFe=None, DataEmissaoNFe=None, NumeroLote=None, ChaveRPS=None, TipoRPS=None, DataEmissaoRPS=None, CPFCNPJPrestador=None, RazaoSocialPrestador=None, EnderecoPrestador=None, EmailPrestador=None, StatusNFe=None, DataCancelamento=None, TributacaoNFe=None, OpcaoSimples=None, NumeroGuia=None, DataQuitacaoGuia=None, ValorServicos=None, ValorDeducoes=None, ValorPIS=None, ValorCOFINS=None, ValorINSS=None, ValorIR=None, ValorCSLL=None, CodigoServico=None, AliquotaServicos=None, ValorISS=None, ValorCredito=None, ISSRetido=None, CPFCNPJTomador=None, InscricaoMunicipalTomador=None, InscricaoEstadualTomador=None, RazaoSocialTomador=None, EnderecoTomador=None, EmailTomador=None, CPFCNPJIntermediario=None, InscricaoMunicipalIntermediario=None, ISSRetidoIntermediario=None, EmailIntermediario=None, Discriminacao=None, ValorCargaTributaria=None, PercentualCargaTributaria=None, FonteCargaTributaria=None, CodigoCEI=None, MatriculaObra=None, MunicipioPrestacao=None, NumeroEncapsulamento=None, ValorTotalRecebido=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Assinatura = Assinatura
        self.validate_tpAssinatura(self.Assinatura)
        self.Assinatura_nsprefix_ = None
        self.ChaveNFe = ChaveNFe
        self.ChaveNFe_nsprefix_ = None
        if isinstance(DataEmissaoNFe, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataEmissaoNFe, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = DataEmissaoNFe
        self.DataEmissaoNFe = initvalue_
        self.DataEmissaoNFe_nsprefix_ = None
        self.NumeroLote = NumeroLote
        self.validate_tpNumero(self.NumeroLote)
        self.NumeroLote_nsprefix_ = None
        self.ChaveRPS = ChaveRPS
        self.ChaveRPS_nsprefix_ = None
        self.TipoRPS = TipoRPS
        self.validate_tpTipoRPS(self.TipoRPS)
        self.TipoRPS_nsprefix_ = None
        if isinstance(DataEmissaoRPS, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataEmissaoRPS, '%Y-%m-%d').date()
        else:
            initvalue_ = DataEmissaoRPS
        self.DataEmissaoRPS = initvalue_
        self.DataEmissaoRPS_nsprefix_ = None
        self.CPFCNPJPrestador = CPFCNPJPrestador
        self.CPFCNPJPrestador_nsprefix_ = None
        self.RazaoSocialPrestador = RazaoSocialPrestador
        self.validate_tpRazaoSocial(self.RazaoSocialPrestador)
        self.RazaoSocialPrestador_nsprefix_ = None
        self.EnderecoPrestador = EnderecoPrestador
        self.EnderecoPrestador_nsprefix_ = None
        self.EmailPrestador = EmailPrestador
        self.validate_tpEmail(self.EmailPrestador)
        self.EmailPrestador_nsprefix_ = None
        self.StatusNFe = StatusNFe
        self.validate_tpStatusNFe(self.StatusNFe)
        self.StatusNFe_nsprefix_ = None
        if isinstance(DataCancelamento, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataCancelamento, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = DataCancelamento
        self.DataCancelamento = initvalue_
        self.DataCancelamento_nsprefix_ = None
        self.TributacaoNFe = TributacaoNFe
        self.validate_tpTributacaoNFe(self.TributacaoNFe)
        self.TributacaoNFe_nsprefix_ = None
        self.OpcaoSimples = OpcaoSimples
        self.validate_tpOpcaoSimples(self.OpcaoSimples)
        self.OpcaoSimples_nsprefix_ = None
        self.NumeroGuia = NumeroGuia
        self.validate_tpNumero(self.NumeroGuia)
        self.NumeroGuia_nsprefix_ = None
        if isinstance(DataQuitacaoGuia, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataQuitacaoGuia, '%Y-%m-%d').date()
        else:
            initvalue_ = DataQuitacaoGuia
        self.DataQuitacaoGuia = initvalue_
        self.DataQuitacaoGuia_nsprefix_ = None
        self.ValorServicos = ValorServicos
        self.validate_tpValor(self.ValorServicos)
        self.ValorServicos_nsprefix_ = None
        self.ValorDeducoes = ValorDeducoes
        self.validate_tpValor(self.ValorDeducoes)
        self.ValorDeducoes_nsprefix_ = None
        self.ValorPIS = ValorPIS
        self.validate_tpValor(self.ValorPIS)
        self.ValorPIS_nsprefix_ = None
        self.ValorCOFINS = ValorCOFINS
        self.validate_tpValor(self.ValorCOFINS)
        self.ValorCOFINS_nsprefix_ = None
        self.ValorINSS = ValorINSS
        self.validate_tpValor(self.ValorINSS)
        self.ValorINSS_nsprefix_ = None
        self.ValorIR = ValorIR
        self.validate_tpValor(self.ValorIR)
        self.ValorIR_nsprefix_ = None
        self.ValorCSLL = ValorCSLL
        self.validate_tpValor(self.ValorCSLL)
        self.ValorCSLL_nsprefix_ = None
        self.CodigoServico = CodigoServico
        self.validate_tpCodigoServico(self.CodigoServico)
        self.CodigoServico_nsprefix_ = None
        self.AliquotaServicos = AliquotaServicos
        self.validate_tpAliquota(self.AliquotaServicos)
        self.AliquotaServicos_nsprefix_ = None
        self.ValorISS = ValorISS
        self.validate_tpValor(self.ValorISS)
        self.ValorISS_nsprefix_ = None
        self.ValorCredito = ValorCredito
        self.validate_tpValor(self.ValorCredito)
        self.ValorCredito_nsprefix_ = None
        self.ISSRetido = ISSRetido
        self.ISSRetido_nsprefix_ = None
        self.CPFCNPJTomador = CPFCNPJTomador
        self.CPFCNPJTomador_nsprefix_ = None
        self.InscricaoMunicipalTomador = InscricaoMunicipalTomador
        self.validate_tpInscricaoMunicipal(self.InscricaoMunicipalTomador)
        self.InscricaoMunicipalTomador_nsprefix_ = None
        self.InscricaoEstadualTomador = InscricaoEstadualTomador
        self.validate_tpInscricaoEstadual(self.InscricaoEstadualTomador)
        self.InscricaoEstadualTomador_nsprefix_ = None
        self.RazaoSocialTomador = RazaoSocialTomador
        self.validate_tpRazaoSocial(self.RazaoSocialTomador)
        self.RazaoSocialTomador_nsprefix_ = None
        self.EnderecoTomador = EnderecoTomador
        self.EnderecoTomador_nsprefix_ = None
        self.EmailTomador = EmailTomador
        self.validate_tpEmail(self.EmailTomador)
        self.EmailTomador_nsprefix_ = None
        self.CPFCNPJIntermediario = CPFCNPJIntermediario
        self.CPFCNPJIntermediario_nsprefix_ = None
        self.InscricaoMunicipalIntermediario = InscricaoMunicipalIntermediario
        self.validate_tpInscricaoMunicipal(self.InscricaoMunicipalIntermediario)
        self.InscricaoMunicipalIntermediario_nsprefix_ = None
        self.ISSRetidoIntermediario = ISSRetidoIntermediario
        self.ISSRetidoIntermediario_nsprefix_ = None
        self.EmailIntermediario = EmailIntermediario
        self.validate_tpEmail(self.EmailIntermediario)
        self.EmailIntermediario_nsprefix_ = None
        self.Discriminacao = Discriminacao
        self.validate_tpDiscriminacao(self.Discriminacao)
        self.Discriminacao_nsprefix_ = None
        self.ValorCargaTributaria = ValorCargaTributaria
        self.validate_tpValor(self.ValorCargaTributaria)
        self.ValorCargaTributaria_nsprefix_ = None
        self.PercentualCargaTributaria = PercentualCargaTributaria
        self.validate_tpPercentualCargaTributaria(self.PercentualCargaTributaria)
        self.PercentualCargaTributaria_nsprefix_ = None
        self.FonteCargaTributaria = FonteCargaTributaria
        self.validate_tpFonteCargaTributaria(self.FonteCargaTributaria)
        self.FonteCargaTributaria_nsprefix_ = None
        self.CodigoCEI = CodigoCEI
        self.validate_tpNumero(self.CodigoCEI)
        self.CodigoCEI_nsprefix_ = None
        self.MatriculaObra = MatriculaObra
        self.validate_tpNumero(self.MatriculaObra)
        self.MatriculaObra_nsprefix_ = None
        self.MunicipioPrestacao = MunicipioPrestacao
        self.validate_tpCidade(self.MunicipioPrestacao)
        self.MunicipioPrestacao_nsprefix_ = None
        self.NumeroEncapsulamento = NumeroEncapsulamento
        self.validate_tpNumero(self.NumeroEncapsulamento)
        self.NumeroEncapsulamento_nsprefix_ = None
        self.ValorTotalRecebido = ValorTotalRecebido
        self.validate_tpValor(self.ValorTotalRecebido)
        self.ValorTotalRecebido_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpNFe)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpNFe.subclass:
            return tpNFe.subclass(*args_, **kwargs_)
        else:
            return tpNFe(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpAssinatura(self, value):
        result = True
        # Validate type tpAssinatura, a restriction on xs:base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def validate_tpNumero(self, value):
        result = True
        # Validate type tpNumero, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpNumero_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpNumero_patterns_, ))
                result = False
        return result
    validate_tpNumero_patterns_ = [['^([0-9]{1,12})$']]
    def validate_tpTipoRPS(self, value):
        result = True
        # Validate type tpTipoRPS, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['RPS', 'RPS-M', 'RPS-C']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpTipoRPS' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpRazaoSocial(self, value):
        result = True
        # Validate type tpRazaoSocial, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 75:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpRazaoSocial' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpRazaoSocial' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpEmail(self, value):
        result = True
        # Validate type tpEmail, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 75:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpEmail' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpEmail' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpStatusNFe(self, value):
        result = True
        # Validate type tpStatusNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['N', 'C', 'E']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpStatusNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpTributacaoNFe(self, value):
        result = True
        # Validate type tpTributacaoNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpTributacaoNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpTributacaoNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpOpcaoSimples(self, value):
        result = True
        # Validate type tpOpcaoSimples, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['0', '1', '2', '3']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpOpcaoSimples' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpValor(self, value):
        result = True
        # Validate type tpValor, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on tpValor' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tpValor' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpValor_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpValor_patterns_, ))
                result = False
        return result
    validate_tpValor_patterns_ = [['^(0|0\\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\\.[0-9]{0,2})?)$']]
    def validate_tpCodigoServico(self, value):
        result = True
        # Validate type tpCodigoServico, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCodigoServico_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCodigoServico_patterns_, ))
                result = False
        return result
    validate_tpCodigoServico_patterns_ = [['^([0-9]{4,5})$']]
    def validate_tpAliquota(self, value):
        result = True
        # Validate type tpAliquota, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on tpAliquota' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tpAliquota' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tpInscricaoMunicipal(self, value):
        result = True
        # Validate type tpInscricaoMunicipal, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpInscricaoMunicipal_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpInscricaoMunicipal_patterns_, ))
                result = False
        return result
    validate_tpInscricaoMunicipal_patterns_ = [['^([0-9]{8,8})$']]
    def validate_tpInscricaoEstadual(self, value):
        result = True
        # Validate type tpInscricaoEstadual, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpInscricaoEstadual_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpInscricaoEstadual_patterns_, ))
                result = False
        return result
    validate_tpInscricaoEstadual_patterns_ = [['^([0-9]{1,19})$']]
    def validate_tpDiscriminacao(self, value):
        result = True
        # Validate type tpDiscriminacao, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpDiscriminacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpDiscriminacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpPercentualCargaTributaria(self, value):
        result = True
        # Validate type tpPercentualCargaTributaria, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on tpPercentualCargaTributaria' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tpPercentualCargaTributaria' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tpFonteCargaTributaria(self, value):
        result = True
        # Validate type tpFonteCargaTributaria, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpFonteCargaTributaria' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpFonteCargaTributaria' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpCidade(self, value):
        result = True
        # Validate type tpCidade, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCidade_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCidade_patterns_, ))
                result = False
        return result
    validate_tpCidade_patterns_ = [['^([0-9]{7})$']]
    def hasContent_(self):
        if (
            self.Assinatura is not None or
            self.ChaveNFe is not None or
            self.DataEmissaoNFe is not None or
            self.NumeroLote is not None or
            self.ChaveRPS is not None or
            self.TipoRPS is not None or
            self.DataEmissaoRPS is not None or
            self.CPFCNPJPrestador is not None or
            self.RazaoSocialPrestador is not None or
            self.EnderecoPrestador is not None or
            self.EmailPrestador is not None or
            self.StatusNFe is not None or
            self.DataCancelamento is not None or
            self.TributacaoNFe is not None or
            self.OpcaoSimples is not None or
            self.NumeroGuia is not None or
            self.DataQuitacaoGuia is not None or
            self.ValorServicos is not None or
            self.ValorDeducoes is not None or
            self.ValorPIS is not None or
            self.ValorCOFINS is not None or
            self.ValorINSS is not None or
            self.ValorIR is not None or
            self.ValorCSLL is not None or
            self.CodigoServico is not None or
            self.AliquotaServicos is not None or
            self.ValorISS is not None or
            self.ValorCredito is not None or
            self.ISSRetido is not None or
            self.CPFCNPJTomador is not None or
            self.InscricaoMunicipalTomador is not None or
            self.InscricaoEstadualTomador is not None or
            self.RazaoSocialTomador is not None or
            self.EnderecoTomador is not None or
            self.EmailTomador is not None or
            self.CPFCNPJIntermediario is not None or
            self.InscricaoMunicipalIntermediario is not None or
            self.ISSRetidoIntermediario is not None or
            self.EmailIntermediario is not None or
            self.Discriminacao is not None or
            self.ValorCargaTributaria is not None or
            self.PercentualCargaTributaria is not None or
            self.FonteCargaTributaria is not None or
            self.CodigoCEI is not None or
            self.MatriculaObra is not None or
            self.MunicipioPrestacao is not None or
            self.NumeroEncapsulamento is not None or
            self.ValorTotalRecebido is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpNFe', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpNFe')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpNFe':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpNFe')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpNFe', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpNFe'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpNFe', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Assinatura is not None:
            namespaceprefix_ = self.Assinatura_nsprefix_ + ':' if (UseCapturedNS_ and self.Assinatura_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAssinatura>%s</%sAssinatura>%s' % (namespaceprefix_ , self.gds_format_base64(self.Assinatura, input_name='Assinatura'), namespaceprefix_ , eol_))
        if self.ChaveNFe is not None:
            namespaceprefix_ = self.ChaveNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.ChaveNFe_nsprefix_) else ''
            self.ChaveNFe.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChaveNFe', pretty_print=pretty_print)
        if self.DataEmissaoNFe is not None:
            namespaceprefix_ = self.DataEmissaoNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.DataEmissaoNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataEmissaoNFe>%s</%sDataEmissaoNFe>%s' % (namespaceprefix_ , self.gds_format_datetime(self.DataEmissaoNFe, input_name='DataEmissaoNFe'), namespaceprefix_ , eol_))
        if self.NumeroLote is not None:
            namespaceprefix_ = self.NumeroLote_nsprefix_ + ':' if (UseCapturedNS_ and self.NumeroLote_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumeroLote>%s</%sNumeroLote>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumeroLote, input_name='NumeroLote'), namespaceprefix_ , eol_))
        if self.ChaveRPS is not None:
            namespaceprefix_ = self.ChaveRPS_nsprefix_ + ':' if (UseCapturedNS_ and self.ChaveRPS_nsprefix_) else ''
            self.ChaveRPS.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChaveRPS', pretty_print=pretty_print)
        if self.TipoRPS is not None:
            namespaceprefix_ = self.TipoRPS_nsprefix_ + ':' if (UseCapturedNS_ and self.TipoRPS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTipoRPS>%s</%sTipoRPS>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TipoRPS), input_name='TipoRPS')), namespaceprefix_ , eol_))
        if self.DataEmissaoRPS is not None:
            namespaceprefix_ = self.DataEmissaoRPS_nsprefix_ + ':' if (UseCapturedNS_ and self.DataEmissaoRPS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataEmissaoRPS>%s</%sDataEmissaoRPS>%s' % (namespaceprefix_ , self.gds_format_date(self.DataEmissaoRPS, input_name='DataEmissaoRPS'), namespaceprefix_ , eol_))
        if self.CPFCNPJPrestador is not None:
            namespaceprefix_ = self.CPFCNPJPrestador_nsprefix_ + ':' if (UseCapturedNS_ and self.CPFCNPJPrestador_nsprefix_) else ''
            self.CPFCNPJPrestador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CPFCNPJPrestador', pretty_print=pretty_print)
        if self.RazaoSocialPrestador is not None:
            namespaceprefix_ = self.RazaoSocialPrestador_nsprefix_ + ':' if (UseCapturedNS_ and self.RazaoSocialPrestador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRazaoSocialPrestador>%s</%sRazaoSocialPrestador>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RazaoSocialPrestador), input_name='RazaoSocialPrestador')), namespaceprefix_ , eol_))
        if self.EnderecoPrestador is not None:
            namespaceprefix_ = self.EnderecoPrestador_nsprefix_ + ':' if (UseCapturedNS_ and self.EnderecoPrestador_nsprefix_) else ''
            self.EnderecoPrestador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EnderecoPrestador', pretty_print=pretty_print)
        if self.EmailPrestador is not None:
            namespaceprefix_ = self.EmailPrestador_nsprefix_ + ':' if (UseCapturedNS_ and self.EmailPrestador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEmailPrestador>%s</%sEmailPrestador>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EmailPrestador), input_name='EmailPrestador')), namespaceprefix_ , eol_))
        if self.StatusNFe is not None:
            namespaceprefix_ = self.StatusNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.StatusNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStatusNFe>%s</%sStatusNFe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.StatusNFe), input_name='StatusNFe')), namespaceprefix_ , eol_))
        if self.DataCancelamento is not None:
            namespaceprefix_ = self.DataCancelamento_nsprefix_ + ':' if (UseCapturedNS_ and self.DataCancelamento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataCancelamento>%s</%sDataCancelamento>%s' % (namespaceprefix_ , self.gds_format_datetime(self.DataCancelamento, input_name='DataCancelamento'), namespaceprefix_ , eol_))
        if self.TributacaoNFe is not None:
            namespaceprefix_ = self.TributacaoNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.TributacaoNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTributacaoNFe>%s</%sTributacaoNFe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TributacaoNFe), input_name='TributacaoNFe')), namespaceprefix_ , eol_))
        if self.OpcaoSimples is not None:
            namespaceprefix_ = self.OpcaoSimples_nsprefix_ + ':' if (UseCapturedNS_ and self.OpcaoSimples_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sOpcaoSimples>%s</%sOpcaoSimples>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.OpcaoSimples), input_name='OpcaoSimples')), namespaceprefix_ , eol_))
        if self.NumeroGuia is not None:
            namespaceprefix_ = self.NumeroGuia_nsprefix_ + ':' if (UseCapturedNS_ and self.NumeroGuia_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumeroGuia>%s</%sNumeroGuia>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumeroGuia, input_name='NumeroGuia'), namespaceprefix_ , eol_))
        if self.DataQuitacaoGuia is not None:
            namespaceprefix_ = self.DataQuitacaoGuia_nsprefix_ + ':' if (UseCapturedNS_ and self.DataQuitacaoGuia_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataQuitacaoGuia>%s</%sDataQuitacaoGuia>%s' % (namespaceprefix_ , self.gds_format_date(self.DataQuitacaoGuia, input_name='DataQuitacaoGuia'), namespaceprefix_ , eol_))
        if self.ValorServicos is not None:
            namespaceprefix_ = self.ValorServicos_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorServicos_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorServicos>%s</%sValorServicos>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorServicos, input_name='ValorServicos'), namespaceprefix_ , eol_))
        if self.ValorDeducoes is not None:
            namespaceprefix_ = self.ValorDeducoes_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorDeducoes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorDeducoes>%s</%sValorDeducoes>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorDeducoes, input_name='ValorDeducoes'), namespaceprefix_ , eol_))
        if self.ValorPIS is not None:
            namespaceprefix_ = self.ValorPIS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPIS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPIS>%s</%sValorPIS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorPIS, input_name='ValorPIS'), namespaceprefix_ , eol_))
        if self.ValorCOFINS is not None:
            namespaceprefix_ = self.ValorCOFINS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCOFINS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCOFINS>%s</%sValorCOFINS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCOFINS, input_name='ValorCOFINS'), namespaceprefix_ , eol_))
        if self.ValorINSS is not None:
            namespaceprefix_ = self.ValorINSS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorINSS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorINSS>%s</%sValorINSS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorINSS, input_name='ValorINSS'), namespaceprefix_ , eol_))
        if self.ValorIR is not None:
            namespaceprefix_ = self.ValorIR_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorIR_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorIR>%s</%sValorIR>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorIR, input_name='ValorIR'), namespaceprefix_ , eol_))
        if self.ValorCSLL is not None:
            namespaceprefix_ = self.ValorCSLL_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCSLL_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCSLL>%s</%sValorCSLL>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCSLL, input_name='ValorCSLL'), namespaceprefix_ , eol_))
        if self.CodigoServico is not None:
            namespaceprefix_ = self.CodigoServico_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoServico_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoServico>%s</%sCodigoServico>%s' % (namespaceprefix_ , self.gds_format_integer(self.CodigoServico, input_name='CodigoServico'), namespaceprefix_ , eol_))
        if self.AliquotaServicos is not None:
            namespaceprefix_ = self.AliquotaServicos_nsprefix_ + ':' if (UseCapturedNS_ and self.AliquotaServicos_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAliquotaServicos>%s</%sAliquotaServicos>%s' % (namespaceprefix_ , self.gds_format_decimal(self.AliquotaServicos, input_name='AliquotaServicos'), namespaceprefix_ , eol_))
        if self.ValorISS is not None:
            namespaceprefix_ = self.ValorISS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorISS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorISS>%s</%sValorISS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorISS, input_name='ValorISS'), namespaceprefix_ , eol_))
        if self.ValorCredito is not None:
            namespaceprefix_ = self.ValorCredito_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCredito_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCredito>%s</%sValorCredito>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCredito, input_name='ValorCredito'), namespaceprefix_ , eol_))
        if self.ISSRetido is not None:
            namespaceprefix_ = self.ISSRetido_nsprefix_ + ':' if (UseCapturedNS_ and self.ISSRetido_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sISSRetido>%s</%sISSRetido>%s' % (namespaceprefix_ , self.gds_format_boolean(self.ISSRetido, input_name='ISSRetido'), namespaceprefix_ , eol_))
        if self.CPFCNPJTomador is not None:
            namespaceprefix_ = self.CPFCNPJTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.CPFCNPJTomador_nsprefix_) else ''
            self.CPFCNPJTomador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CPFCNPJTomador', pretty_print=pretty_print)
        if self.InscricaoMunicipalTomador is not None:
            namespaceprefix_ = self.InscricaoMunicipalTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipalTomador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipalTomador>%s</%sInscricaoMunicipalTomador>%s' % (namespaceprefix_ , self.gds_format_integer(self.InscricaoMunicipalTomador, input_name='InscricaoMunicipalTomador'), namespaceprefix_ , eol_))
        if self.InscricaoEstadualTomador is not None:
            namespaceprefix_ = self.InscricaoEstadualTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoEstadualTomador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoEstadualTomador>%s</%sInscricaoEstadualTomador>%s' % (namespaceprefix_ , self.gds_format_integer(self.InscricaoEstadualTomador, input_name='InscricaoEstadualTomador'), namespaceprefix_ , eol_))
        if self.RazaoSocialTomador is not None:
            namespaceprefix_ = self.RazaoSocialTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.RazaoSocialTomador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRazaoSocialTomador>%s</%sRazaoSocialTomador>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RazaoSocialTomador), input_name='RazaoSocialTomador')), namespaceprefix_ , eol_))
        if self.EnderecoTomador is not None:
            namespaceprefix_ = self.EnderecoTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.EnderecoTomador_nsprefix_) else ''
            self.EnderecoTomador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EnderecoTomador', pretty_print=pretty_print)
        if self.EmailTomador is not None:
            namespaceprefix_ = self.EmailTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.EmailTomador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEmailTomador>%s</%sEmailTomador>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EmailTomador), input_name='EmailTomador')), namespaceprefix_ , eol_))
        if self.CPFCNPJIntermediario is not None:
            namespaceprefix_ = self.CPFCNPJIntermediario_nsprefix_ + ':' if (UseCapturedNS_ and self.CPFCNPJIntermediario_nsprefix_) else ''
            self.CPFCNPJIntermediario.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CPFCNPJIntermediario', pretty_print=pretty_print)
        if self.InscricaoMunicipalIntermediario is not None:
            namespaceprefix_ = self.InscricaoMunicipalIntermediario_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipalIntermediario_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipalIntermediario>%s</%sInscricaoMunicipalIntermediario>%s' % (namespaceprefix_ , self.gds_format_integer(self.InscricaoMunicipalIntermediario, input_name='InscricaoMunicipalIntermediario'), namespaceprefix_ , eol_))
        if self.ISSRetidoIntermediario is not None:
            namespaceprefix_ = self.ISSRetidoIntermediario_nsprefix_ + ':' if (UseCapturedNS_ and self.ISSRetidoIntermediario_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sISSRetidoIntermediario>%s</%sISSRetidoIntermediario>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ISSRetidoIntermediario), input_name='ISSRetidoIntermediario')), namespaceprefix_ , eol_))
        if self.EmailIntermediario is not None:
            namespaceprefix_ = self.EmailIntermediario_nsprefix_ + ':' if (UseCapturedNS_ and self.EmailIntermediario_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEmailIntermediario>%s</%sEmailIntermediario>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EmailIntermediario), input_name='EmailIntermediario')), namespaceprefix_ , eol_))
        if self.Discriminacao is not None:
            namespaceprefix_ = self.Discriminacao_nsprefix_ + ':' if (UseCapturedNS_ and self.Discriminacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDiscriminacao>%s</%sDiscriminacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Discriminacao), input_name='Discriminacao')), namespaceprefix_ , eol_))
        if self.ValorCargaTributaria is not None:
            namespaceprefix_ = self.ValorCargaTributaria_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCargaTributaria_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCargaTributaria>%s</%sValorCargaTributaria>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCargaTributaria, input_name='ValorCargaTributaria'), namespaceprefix_ , eol_))
        if self.PercentualCargaTributaria is not None:
            namespaceprefix_ = self.PercentualCargaTributaria_nsprefix_ + ':' if (UseCapturedNS_ and self.PercentualCargaTributaria_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPercentualCargaTributaria>%s</%sPercentualCargaTributaria>%s' % (namespaceprefix_ , self.gds_format_decimal(self.PercentualCargaTributaria, input_name='PercentualCargaTributaria'), namespaceprefix_ , eol_))
        if self.FonteCargaTributaria is not None:
            namespaceprefix_ = self.FonteCargaTributaria_nsprefix_ + ':' if (UseCapturedNS_ and self.FonteCargaTributaria_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFonteCargaTributaria>%s</%sFonteCargaTributaria>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.FonteCargaTributaria), input_name='FonteCargaTributaria')), namespaceprefix_ , eol_))
        if self.CodigoCEI is not None:
            namespaceprefix_ = self.CodigoCEI_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoCEI_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoCEI>%s</%sCodigoCEI>%s' % (namespaceprefix_ , self.gds_format_integer(self.CodigoCEI, input_name='CodigoCEI'), namespaceprefix_ , eol_))
        if self.MatriculaObra is not None:
            namespaceprefix_ = self.MatriculaObra_nsprefix_ + ':' if (UseCapturedNS_ and self.MatriculaObra_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMatriculaObra>%s</%sMatriculaObra>%s' % (namespaceprefix_ , self.gds_format_integer(self.MatriculaObra, input_name='MatriculaObra'), namespaceprefix_ , eol_))
        if self.MunicipioPrestacao is not None:
            namespaceprefix_ = self.MunicipioPrestacao_nsprefix_ + ':' if (UseCapturedNS_ and self.MunicipioPrestacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMunicipioPrestacao>%s</%sMunicipioPrestacao>%s' % (namespaceprefix_ , self.gds_format_integer(self.MunicipioPrestacao, input_name='MunicipioPrestacao'), namespaceprefix_ , eol_))
        if self.NumeroEncapsulamento is not None:
            namespaceprefix_ = self.NumeroEncapsulamento_nsprefix_ + ':' if (UseCapturedNS_ and self.NumeroEncapsulamento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumeroEncapsulamento>%s</%sNumeroEncapsulamento>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumeroEncapsulamento, input_name='NumeroEncapsulamento'), namespaceprefix_ , eol_))
        if self.ValorTotalRecebido is not None:
            namespaceprefix_ = self.ValorTotalRecebido_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorTotalRecebido_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorTotalRecebido>%s</%sValorTotalRecebido>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorTotalRecebido, input_name='ValorTotalRecebido'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Assinatura':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Assinatura')
            else:
                bval_ = None
            self.Assinatura = bval_
            self.Assinatura_nsprefix_ = child_.prefix
            # validate type tpAssinatura
            self.validate_tpAssinatura(self.Assinatura)
        elif nodeName_ == 'ChaveNFe':
            obj_ = tpChaveNFe.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChaveNFe = obj_
            obj_.original_tagname_ = 'ChaveNFe'
        elif nodeName_ == 'DataEmissaoNFe':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.DataEmissaoNFe = dval_
            self.DataEmissaoNFe_nsprefix_ = child_.prefix
        elif nodeName_ == 'NumeroLote' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumeroLote')
            ival_ = self.gds_validate_integer(ival_, node, 'NumeroLote')
            self.NumeroLote = ival_
            self.NumeroLote_nsprefix_ = child_.prefix
            # validate type tpNumero
            self.validate_tpNumero(self.NumeroLote)
        elif nodeName_ == 'ChaveRPS':
            obj_ = tpChaveRPS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChaveRPS = obj_
            obj_.original_tagname_ = 'ChaveRPS'
        elif nodeName_ == 'TipoRPS':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TipoRPS')
            value_ = self.gds_validate_string(value_, node, 'TipoRPS')
            self.TipoRPS = value_
            self.TipoRPS_nsprefix_ = child_.prefix
            # validate type tpTipoRPS
            self.validate_tpTipoRPS(self.TipoRPS)
        elif nodeName_ == 'DataEmissaoRPS':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.DataEmissaoRPS = dval_
            self.DataEmissaoRPS_nsprefix_ = child_.prefix
        elif nodeName_ == 'CPFCNPJPrestador':
            obj_ = tpCPFCNPJ.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CPFCNPJPrestador = obj_
            obj_.original_tagname_ = 'CPFCNPJPrestador'
        elif nodeName_ == 'RazaoSocialPrestador':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RazaoSocialPrestador')
            value_ = self.gds_validate_string(value_, node, 'RazaoSocialPrestador')
            self.RazaoSocialPrestador = value_
            self.RazaoSocialPrestador_nsprefix_ = child_.prefix
            # validate type tpRazaoSocial
            self.validate_tpRazaoSocial(self.RazaoSocialPrestador)
        elif nodeName_ == 'EnderecoPrestador':
            obj_ = tpEndereco.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EnderecoPrestador = obj_
            obj_.original_tagname_ = 'EnderecoPrestador'
        elif nodeName_ == 'EmailPrestador':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EmailPrestador')
            value_ = self.gds_validate_string(value_, node, 'EmailPrestador')
            self.EmailPrestador = value_
            self.EmailPrestador_nsprefix_ = child_.prefix
            # validate type tpEmail
            self.validate_tpEmail(self.EmailPrestador)
        elif nodeName_ == 'StatusNFe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'StatusNFe')
            value_ = self.gds_validate_string(value_, node, 'StatusNFe')
            self.StatusNFe = value_
            self.StatusNFe_nsprefix_ = child_.prefix
            # validate type tpStatusNFe
            self.validate_tpStatusNFe(self.StatusNFe)
        elif nodeName_ == 'DataCancelamento':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.DataCancelamento = dval_
            self.DataCancelamento_nsprefix_ = child_.prefix
        elif nodeName_ == 'TributacaoNFe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TributacaoNFe')
            value_ = self.gds_validate_string(value_, node, 'TributacaoNFe')
            self.TributacaoNFe = value_
            self.TributacaoNFe_nsprefix_ = child_.prefix
            # validate type tpTributacaoNFe
            self.validate_tpTributacaoNFe(self.TributacaoNFe)
        elif nodeName_ == 'OpcaoSimples':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OpcaoSimples')
            value_ = self.gds_validate_string(value_, node, 'OpcaoSimples')
            self.OpcaoSimples = value_
            self.OpcaoSimples_nsprefix_ = child_.prefix
            # validate type tpOpcaoSimples
            self.validate_tpOpcaoSimples(self.OpcaoSimples)
        elif nodeName_ == 'NumeroGuia' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumeroGuia')
            ival_ = self.gds_validate_integer(ival_, node, 'NumeroGuia')
            self.NumeroGuia = ival_
            self.NumeroGuia_nsprefix_ = child_.prefix
            # validate type tpNumero
            self.validate_tpNumero(self.NumeroGuia)
        elif nodeName_ == 'DataQuitacaoGuia':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.DataQuitacaoGuia = dval_
            self.DataQuitacaoGuia_nsprefix_ = child_.prefix
        elif nodeName_ == 'ValorServicos' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorServicos')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorServicos')
            self.ValorServicos = fval_
            self.ValorServicos_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorServicos)
        elif nodeName_ == 'ValorDeducoes' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorDeducoes')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorDeducoes')
            self.ValorDeducoes = fval_
            self.ValorDeducoes_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorDeducoes)
        elif nodeName_ == 'ValorPIS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorPIS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorPIS')
            self.ValorPIS = fval_
            self.ValorPIS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorPIS)
        elif nodeName_ == 'ValorCOFINS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCOFINS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCOFINS')
            self.ValorCOFINS = fval_
            self.ValorCOFINS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorCOFINS)
        elif nodeName_ == 'ValorINSS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorINSS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorINSS')
            self.ValorINSS = fval_
            self.ValorINSS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorINSS)
        elif nodeName_ == 'ValorIR' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorIR')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorIR')
            self.ValorIR = fval_
            self.ValorIR_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorIR)
        elif nodeName_ == 'ValorCSLL' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCSLL')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCSLL')
            self.ValorCSLL = fval_
            self.ValorCSLL_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorCSLL)
        elif nodeName_ == 'CodigoServico' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CodigoServico')
            ival_ = self.gds_validate_integer(ival_, node, 'CodigoServico')
            self.CodigoServico = ival_
            self.CodigoServico_nsprefix_ = child_.prefix
            # validate type tpCodigoServico
            self.validate_tpCodigoServico(self.CodigoServico)
        elif nodeName_ == 'AliquotaServicos' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'AliquotaServicos')
            fval_ = self.gds_validate_decimal(fval_, node, 'AliquotaServicos')
            self.AliquotaServicos = fval_
            self.AliquotaServicos_nsprefix_ = child_.prefix
            # validate type tpAliquota
            self.validate_tpAliquota(self.AliquotaServicos)
        elif nodeName_ == 'ValorISS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorISS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorISS')
            self.ValorISS = fval_
            self.ValorISS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorISS)
        elif nodeName_ == 'ValorCredito' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCredito')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCredito')
            self.ValorCredito = fval_
            self.ValorCredito_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorCredito)
        elif nodeName_ == 'ISSRetido':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'ISSRetido')
            ival_ = self.gds_validate_boolean(ival_, node, 'ISSRetido')
            self.ISSRetido = ival_
            self.ISSRetido_nsprefix_ = child_.prefix
        elif nodeName_ == 'CPFCNPJTomador':
            obj_ = tpCPFCNPJ.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CPFCNPJTomador = obj_
            obj_.original_tagname_ = 'CPFCNPJTomador'
        elif nodeName_ == 'InscricaoMunicipalTomador' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'InscricaoMunicipalTomador')
            ival_ = self.gds_validate_integer(ival_, node, 'InscricaoMunicipalTomador')
            self.InscricaoMunicipalTomador = ival_
            self.InscricaoMunicipalTomador_nsprefix_ = child_.prefix
            # validate type tpInscricaoMunicipal
            self.validate_tpInscricaoMunicipal(self.InscricaoMunicipalTomador)
        elif nodeName_ == 'InscricaoEstadualTomador' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'InscricaoEstadualTomador')
            ival_ = self.gds_validate_integer(ival_, node, 'InscricaoEstadualTomador')
            self.InscricaoEstadualTomador = ival_
            self.InscricaoEstadualTomador_nsprefix_ = child_.prefix
            # validate type tpInscricaoEstadual
            self.validate_tpInscricaoEstadual(self.InscricaoEstadualTomador)
        elif nodeName_ == 'RazaoSocialTomador':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RazaoSocialTomador')
            value_ = self.gds_validate_string(value_, node, 'RazaoSocialTomador')
            self.RazaoSocialTomador = value_
            self.RazaoSocialTomador_nsprefix_ = child_.prefix
            # validate type tpRazaoSocial
            self.validate_tpRazaoSocial(self.RazaoSocialTomador)
        elif nodeName_ == 'EnderecoTomador':
            obj_ = tpEndereco.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EnderecoTomador = obj_
            obj_.original_tagname_ = 'EnderecoTomador'
        elif nodeName_ == 'EmailTomador':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EmailTomador')
            value_ = self.gds_validate_string(value_, node, 'EmailTomador')
            self.EmailTomador = value_
            self.EmailTomador_nsprefix_ = child_.prefix
            # validate type tpEmail
            self.validate_tpEmail(self.EmailTomador)
        elif nodeName_ == 'CPFCNPJIntermediario':
            obj_ = tpCPFCNPJ.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CPFCNPJIntermediario = obj_
            obj_.original_tagname_ = 'CPFCNPJIntermediario'
        elif nodeName_ == 'InscricaoMunicipalIntermediario' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'InscricaoMunicipalIntermediario')
            ival_ = self.gds_validate_integer(ival_, node, 'InscricaoMunicipalIntermediario')
            self.InscricaoMunicipalIntermediario = ival_
            self.InscricaoMunicipalIntermediario_nsprefix_ = child_.prefix
            # validate type tpInscricaoMunicipal
            self.validate_tpInscricaoMunicipal(self.InscricaoMunicipalIntermediario)
        elif nodeName_ == 'ISSRetidoIntermediario':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ISSRetidoIntermediario')
            value_ = self.gds_validate_string(value_, node, 'ISSRetidoIntermediario')
            self.ISSRetidoIntermediario = value_
            self.ISSRetidoIntermediario_nsprefix_ = child_.prefix
        elif nodeName_ == 'EmailIntermediario':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EmailIntermediario')
            value_ = self.gds_validate_string(value_, node, 'EmailIntermediario')
            self.EmailIntermediario = value_
            self.EmailIntermediario_nsprefix_ = child_.prefix
            # validate type tpEmail
            self.validate_tpEmail(self.EmailIntermediario)
        elif nodeName_ == 'Discriminacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Discriminacao')
            value_ = self.gds_validate_string(value_, node, 'Discriminacao')
            self.Discriminacao = value_
            self.Discriminacao_nsprefix_ = child_.prefix
            # validate type tpDiscriminacao
            self.validate_tpDiscriminacao(self.Discriminacao)
        elif nodeName_ == 'ValorCargaTributaria' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCargaTributaria')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCargaTributaria')
            self.ValorCargaTributaria = fval_
            self.ValorCargaTributaria_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorCargaTributaria)
        elif nodeName_ == 'PercentualCargaTributaria' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'PercentualCargaTributaria')
            fval_ = self.gds_validate_decimal(fval_, node, 'PercentualCargaTributaria')
            self.PercentualCargaTributaria = fval_
            self.PercentualCargaTributaria_nsprefix_ = child_.prefix
            # validate type tpPercentualCargaTributaria
            self.validate_tpPercentualCargaTributaria(self.PercentualCargaTributaria)
        elif nodeName_ == 'FonteCargaTributaria':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'FonteCargaTributaria')
            value_ = self.gds_validate_string(value_, node, 'FonteCargaTributaria')
            self.FonteCargaTributaria = value_
            self.FonteCargaTributaria_nsprefix_ = child_.prefix
            # validate type tpFonteCargaTributaria
            self.validate_tpFonteCargaTributaria(self.FonteCargaTributaria)
        elif nodeName_ == 'CodigoCEI' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CodigoCEI')
            ival_ = self.gds_validate_integer(ival_, node, 'CodigoCEI')
            self.CodigoCEI = ival_
            self.CodigoCEI_nsprefix_ = child_.prefix
            # validate type tpNumero
            self.validate_tpNumero(self.CodigoCEI)
        elif nodeName_ == 'MatriculaObra' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'MatriculaObra')
            ival_ = self.gds_validate_integer(ival_, node, 'MatriculaObra')
            self.MatriculaObra = ival_
            self.MatriculaObra_nsprefix_ = child_.prefix
            # validate type tpNumero
            self.validate_tpNumero(self.MatriculaObra)
        elif nodeName_ == 'MunicipioPrestacao' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'MunicipioPrestacao')
            ival_ = self.gds_validate_integer(ival_, node, 'MunicipioPrestacao')
            self.MunicipioPrestacao = ival_
            self.MunicipioPrestacao_nsprefix_ = child_.prefix
            # validate type tpCidade
            self.validate_tpCidade(self.MunicipioPrestacao)
        elif nodeName_ == 'NumeroEncapsulamento' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumeroEncapsulamento')
            ival_ = self.gds_validate_integer(ival_, node, 'NumeroEncapsulamento')
            self.NumeroEncapsulamento = ival_
            self.NumeroEncapsulamento_nsprefix_ = child_.prefix
            # validate type tpNumero
            self.validate_tpNumero(self.NumeroEncapsulamento)
        elif nodeName_ == 'ValorTotalRecebido' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorTotalRecebido')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorTotalRecebido')
            self.ValorTotalRecebido = fval_
            self.ValorTotalRecebido_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorTotalRecebido)
# end class tpNFe


class tpRPS(GeneratedsSuper):
    """Tipo que representa um RPS."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Assinatura', ['tpAssinatura', 'xs:base64Binary'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'Assinatura', 'type': 'xs:base64Binary'}, None),
        MemberSpec_('ChaveRPS', 'tpChaveRPS', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ChaveRPS', 'type': 'tpChaveRPS'}, None),
        MemberSpec_('TipoRPS', ['tpTipoRPS', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'TipoRPS', 'type': 'xs:string'}, None),
        MemberSpec_('DataEmissao', 'xs:date', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'DataEmissao', 'type': 'xs:date'}, None),
        MemberSpec_('StatusRPS', ['tpStatusNFe', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'StatusRPS', 'type': 'xs:string'}, None),
        MemberSpec_('TributacaoRPS', ['tpTributacaoNFe', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'TributacaoRPS', 'type': 'xs:string'}, None),
        MemberSpec_('ValorServicos', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorServicos', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorDeducoes', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorDeducoes', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorPIS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorPIS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorCOFINS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorCOFINS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorINSS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorINSS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorIR', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorIR', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorCSLL', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorCSLL', 'type': 'xs:decimal'}, None),
        MemberSpec_('CodigoServico', ['tpCodigoServico', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CodigoServico', 'type': 'xs:int'}, None),
        MemberSpec_('AliquotaServicos', ['tpAliquota', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'AliquotaServicos', 'type': 'xs:decimal'}, None),
        MemberSpec_('ISSRetido', 'xs:boolean', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ISSRetido', 'type': 'xs:boolean'}, None),
        MemberSpec_('CPFCNPJTomador', 'tpCPFCNPJ', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CPFCNPJTomador', 'type': 'tpCPFCNPJ'}, None),
        MemberSpec_('InscricaoMunicipalTomador', ['tpInscricaoMunicipal', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'InscricaoMunicipalTomador', 'type': 'xs:long'}, None),
        MemberSpec_('InscricaoEstadualTomador', ['tpInscricaoEstadual', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'InscricaoEstadualTomador', 'type': 'xs:long'}, None),
        MemberSpec_('RazaoSocialTomador', ['tpRazaoSocial', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'RazaoSocialTomador', 'type': 'xs:string'}, None),
        MemberSpec_('EnderecoTomador', 'tpEndereco', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'EnderecoTomador', 'type': 'tpEndereco'}, None),
        MemberSpec_('EmailTomador', ['tpEmail', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'EmailTomador', 'type': 'xs:string'}, None),
        MemberSpec_('CPFCNPJIntermediario', 'tpCPFCNPJ', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CPFCNPJIntermediario', 'type': 'tpCPFCNPJ'}, None),
        MemberSpec_('InscricaoMunicipalIntermediario', ['tpInscricaoMunicipal', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'InscricaoMunicipalIntermediario', 'type': 'xs:long'}, None),
        MemberSpec_('ISSRetidoIntermediario', 'xs:string', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ISSRetidoIntermediario', 'type': 'xs:string'}, None),
        MemberSpec_('EmailIntermediario', ['tpEmail', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'EmailIntermediario', 'type': 'xs:string'}, None),
        MemberSpec_('Discriminacao', ['tpDiscriminacao', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'Discriminacao', 'type': 'xs:string'}, None),
        MemberSpec_('ValorCargaTributaria', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorCargaTributaria', 'type': 'xs:decimal'}, None),
        MemberSpec_('PercentualCargaTributaria', ['tpPercentualCargaTributaria', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'PercentualCargaTributaria', 'type': 'xs:decimal'}, None),
        MemberSpec_('FonteCargaTributaria', ['tpFonteCargaTributaria', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'FonteCargaTributaria', 'type': 'xs:string'}, None),
        MemberSpec_('CodigoCEI', ['tpNumero', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CodigoCEI', 'type': 'xs:long'}, None),
        MemberSpec_('MatriculaObra', ['tpNumero', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'MatriculaObra', 'type': 'xs:long'}, None),
        MemberSpec_('MunicipioPrestacao', ['tpCidade', 'xs:int'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'MunicipioPrestacao', 'type': 'xs:int'}, None),
        MemberSpec_('NumeroEncapsulamento', ['tpNumero', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'NumeroEncapsulamento', 'type': 'xs:long'}, None),
        MemberSpec_('ValorTotalRecebido', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorTotalRecebido', 'type': 'xs:decimal'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Assinatura=None, ChaveRPS=None, TipoRPS=None, DataEmissao=None, StatusRPS=None, TributacaoRPS=None, ValorServicos=None, ValorDeducoes=None, ValorPIS=None, ValorCOFINS=None, ValorINSS=None, ValorIR=None, ValorCSLL=None, CodigoServico=None, AliquotaServicos=None, ISSRetido=None, CPFCNPJTomador=None, InscricaoMunicipalTomador=None, InscricaoEstadualTomador=None, RazaoSocialTomador=None, EnderecoTomador=None, EmailTomador=None, CPFCNPJIntermediario=None, InscricaoMunicipalIntermediario=None, ISSRetidoIntermediario=None, EmailIntermediario=None, Discriminacao=None, ValorCargaTributaria=None, PercentualCargaTributaria=None, FonteCargaTributaria=None, CodigoCEI=None, MatriculaObra=None, MunicipioPrestacao=None, NumeroEncapsulamento=None, ValorTotalRecebido=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Assinatura = Assinatura
        self.validate_tpAssinatura(self.Assinatura)
        self.Assinatura_nsprefix_ = None
        self.ChaveRPS = ChaveRPS
        self.ChaveRPS_nsprefix_ = None
        self.TipoRPS = TipoRPS
        self.validate_tpTipoRPS(self.TipoRPS)
        self.TipoRPS_nsprefix_ = None
        if isinstance(DataEmissao, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataEmissao, '%Y-%m-%d').date()
        else:
            initvalue_ = DataEmissao
        self.DataEmissao = initvalue_
        self.DataEmissao_nsprefix_ = None
        self.StatusRPS = StatusRPS
        self.validate_tpStatusNFe(self.StatusRPS)
        self.StatusRPS_nsprefix_ = None
        self.TributacaoRPS = TributacaoRPS
        self.validate_tpTributacaoNFe(self.TributacaoRPS)
        self.TributacaoRPS_nsprefix_ = None
        self.ValorServicos = ValorServicos
        self.validate_tpValor(self.ValorServicos)
        self.ValorServicos_nsprefix_ = None
        self.ValorDeducoes = ValorDeducoes
        self.validate_tpValor(self.ValorDeducoes)
        self.ValorDeducoes_nsprefix_ = None
        self.ValorPIS = ValorPIS
        self.validate_tpValor(self.ValorPIS)
        self.ValorPIS_nsprefix_ = None
        self.ValorCOFINS = ValorCOFINS
        self.validate_tpValor(self.ValorCOFINS)
        self.ValorCOFINS_nsprefix_ = None
        self.ValorINSS = ValorINSS
        self.validate_tpValor(self.ValorINSS)
        self.ValorINSS_nsprefix_ = None
        self.ValorIR = ValorIR
        self.validate_tpValor(self.ValorIR)
        self.ValorIR_nsprefix_ = None
        self.ValorCSLL = ValorCSLL
        self.validate_tpValor(self.ValorCSLL)
        self.ValorCSLL_nsprefix_ = None
        self.CodigoServico = CodigoServico
        self.validate_tpCodigoServico(self.CodigoServico)
        self.CodigoServico_nsprefix_ = None
        self.AliquotaServicos = AliquotaServicos
        self.validate_tpAliquota(self.AliquotaServicos)
        self.AliquotaServicos_nsprefix_ = None
        self.ISSRetido = ISSRetido
        self.ISSRetido_nsprefix_ = None
        self.CPFCNPJTomador = CPFCNPJTomador
        self.CPFCNPJTomador_nsprefix_ = None
        self.InscricaoMunicipalTomador = InscricaoMunicipalTomador
        self.validate_tpInscricaoMunicipal(self.InscricaoMunicipalTomador)
        self.InscricaoMunicipalTomador_nsprefix_ = None
        self.InscricaoEstadualTomador = InscricaoEstadualTomador
        self.validate_tpInscricaoEstadual(self.InscricaoEstadualTomador)
        self.InscricaoEstadualTomador_nsprefix_ = None
        self.RazaoSocialTomador = RazaoSocialTomador
        self.validate_tpRazaoSocial(self.RazaoSocialTomador)
        self.RazaoSocialTomador_nsprefix_ = None
        self.EnderecoTomador = EnderecoTomador
        self.EnderecoTomador_nsprefix_ = None
        self.EmailTomador = EmailTomador
        self.validate_tpEmail(self.EmailTomador)
        self.EmailTomador_nsprefix_ = None
        self.CPFCNPJIntermediario = CPFCNPJIntermediario
        self.CPFCNPJIntermediario_nsprefix_ = None
        self.InscricaoMunicipalIntermediario = InscricaoMunicipalIntermediario
        self.validate_tpInscricaoMunicipal(self.InscricaoMunicipalIntermediario)
        self.InscricaoMunicipalIntermediario_nsprefix_ = None
        self.ISSRetidoIntermediario = ISSRetidoIntermediario
        self.ISSRetidoIntermediario_nsprefix_ = None
        self.EmailIntermediario = EmailIntermediario
        self.validate_tpEmail(self.EmailIntermediario)
        self.EmailIntermediario_nsprefix_ = None
        self.Discriminacao = Discriminacao
        self.validate_tpDiscriminacao(self.Discriminacao)
        self.Discriminacao_nsprefix_ = None
        self.ValorCargaTributaria = ValorCargaTributaria
        self.validate_tpValor(self.ValorCargaTributaria)
        self.ValorCargaTributaria_nsprefix_ = None
        self.PercentualCargaTributaria = PercentualCargaTributaria
        self.validate_tpPercentualCargaTributaria(self.PercentualCargaTributaria)
        self.PercentualCargaTributaria_nsprefix_ = None
        self.FonteCargaTributaria = FonteCargaTributaria
        self.validate_tpFonteCargaTributaria(self.FonteCargaTributaria)
        self.FonteCargaTributaria_nsprefix_ = None
        self.CodigoCEI = CodigoCEI
        self.validate_tpNumero(self.CodigoCEI)
        self.CodigoCEI_nsprefix_ = None
        self.MatriculaObra = MatriculaObra
        self.validate_tpNumero(self.MatriculaObra)
        self.MatriculaObra_nsprefix_ = None
        self.MunicipioPrestacao = MunicipioPrestacao
        self.validate_tpCidade(self.MunicipioPrestacao)
        self.MunicipioPrestacao_nsprefix_ = None
        self.NumeroEncapsulamento = NumeroEncapsulamento
        self.validate_tpNumero(self.NumeroEncapsulamento)
        self.NumeroEncapsulamento_nsprefix_ = None
        self.ValorTotalRecebido = ValorTotalRecebido
        self.validate_tpValor(self.ValorTotalRecebido)
        self.ValorTotalRecebido_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpRPS)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpRPS.subclass:
            return tpRPS.subclass(*args_, **kwargs_)
        else:
            return tpRPS(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpAssinatura(self, value):
        result = True
        # Validate type tpAssinatura, a restriction on xs:base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def validate_tpTipoRPS(self, value):
        result = True
        # Validate type tpTipoRPS, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['RPS', 'RPS-M', 'RPS-C']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpTipoRPS' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpStatusNFe(self, value):
        result = True
        # Validate type tpStatusNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['N', 'C', 'E']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpStatusNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpTributacaoNFe(self, value):
        result = True
        # Validate type tpTributacaoNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpTributacaoNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpTributacaoNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpValor(self, value):
        result = True
        # Validate type tpValor, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on tpValor' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tpValor' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpValor_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpValor_patterns_, ))
                result = False
        return result
    validate_tpValor_patterns_ = [['^(0|0\\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\\.[0-9]{0,2})?)$']]
    def validate_tpCodigoServico(self, value):
        result = True
        # Validate type tpCodigoServico, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCodigoServico_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCodigoServico_patterns_, ))
                result = False
        return result
    validate_tpCodigoServico_patterns_ = [['^([0-9]{4,5})$']]
    def validate_tpAliquota(self, value):
        result = True
        # Validate type tpAliquota, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on tpAliquota' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tpAliquota' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tpInscricaoMunicipal(self, value):
        result = True
        # Validate type tpInscricaoMunicipal, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpInscricaoMunicipal_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpInscricaoMunicipal_patterns_, ))
                result = False
        return result
    validate_tpInscricaoMunicipal_patterns_ = [['^([0-9]{8,8})$']]
    def validate_tpInscricaoEstadual(self, value):
        result = True
        # Validate type tpInscricaoEstadual, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpInscricaoEstadual_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpInscricaoEstadual_patterns_, ))
                result = False
        return result
    validate_tpInscricaoEstadual_patterns_ = [['^([0-9]{1,19})$']]
    def validate_tpRazaoSocial(self, value):
        result = True
        # Validate type tpRazaoSocial, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 75:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpRazaoSocial' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpRazaoSocial' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpEmail(self, value):
        result = True
        # Validate type tpEmail, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 75:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpEmail' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpEmail' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpDiscriminacao(self, value):
        result = True
        # Validate type tpDiscriminacao, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpDiscriminacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpDiscriminacao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpPercentualCargaTributaria(self, value):
        result = True
        # Validate type tpPercentualCargaTributaria, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on tpPercentualCargaTributaria' % {"value": value, "lineno": lineno} )
                result = False
            if len(str(value)) >= 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on tpPercentualCargaTributaria' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_tpFonteCargaTributaria(self, value):
        result = True
        # Validate type tpFonteCargaTributaria, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpFonteCargaTributaria' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpFonteCargaTributaria' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpNumero(self, value):
        result = True
        # Validate type tpNumero, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpNumero_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpNumero_patterns_, ))
                result = False
        return result
    validate_tpNumero_patterns_ = [['^([0-9]{1,12})$']]
    def validate_tpCidade(self, value):
        result = True
        # Validate type tpCidade, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCidade_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCidade_patterns_, ))
                result = False
        return result
    validate_tpCidade_patterns_ = [['^([0-9]{7})$']]
    def hasContent_(self):
        if (
            self.Assinatura is not None or
            self.ChaveRPS is not None or
            self.TipoRPS is not None or
            self.DataEmissao is not None or
            self.StatusRPS is not None or
            self.TributacaoRPS is not None or
            self.ValorServicos is not None or
            self.ValorDeducoes is not None or
            self.ValorPIS is not None or
            self.ValorCOFINS is not None or
            self.ValorINSS is not None or
            self.ValorIR is not None or
            self.ValorCSLL is not None or
            self.CodigoServico is not None or
            self.AliquotaServicos is not None or
            self.ISSRetido is not None or
            self.CPFCNPJTomador is not None or
            self.InscricaoMunicipalTomador is not None or
            self.InscricaoEstadualTomador is not None or
            self.RazaoSocialTomador is not None or
            self.EnderecoTomador is not None or
            self.EmailTomador is not None or
            self.CPFCNPJIntermediario is not None or
            self.InscricaoMunicipalIntermediario is not None or
            self.ISSRetidoIntermediario is not None or
            self.EmailIntermediario is not None or
            self.Discriminacao is not None or
            self.ValorCargaTributaria is not None or
            self.PercentualCargaTributaria is not None or
            self.FonteCargaTributaria is not None or
            self.CodigoCEI is not None or
            self.MatriculaObra is not None or
            self.MunicipioPrestacao is not None or
            self.NumeroEncapsulamento is not None or
            self.ValorTotalRecebido is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpRPS', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpRPS')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpRPS':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpRPS')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpRPS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpRPS'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpRPS', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Assinatura is not None:
            namespaceprefix_ = self.Assinatura_nsprefix_ + ':' if (UseCapturedNS_ and self.Assinatura_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAssinatura>%s</%sAssinatura>%s' % (namespaceprefix_ , self.gds_format_base64(self.Assinatura, input_name='Assinatura'), namespaceprefix_ , eol_))
        if self.ChaveRPS is not None:
            namespaceprefix_ = self.ChaveRPS_nsprefix_ + ':' if (UseCapturedNS_ and self.ChaveRPS_nsprefix_) else ''
            self.ChaveRPS.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChaveRPS', pretty_print=pretty_print)
        if self.TipoRPS is not None:
            namespaceprefix_ = self.TipoRPS_nsprefix_ + ':' if (UseCapturedNS_ and self.TipoRPS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTipoRPS>%s</%sTipoRPS>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TipoRPS), input_name='TipoRPS')), namespaceprefix_ , eol_))
        if self.DataEmissao is not None:
            namespaceprefix_ = self.DataEmissao_nsprefix_ + ':' if (UseCapturedNS_ and self.DataEmissao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataEmissao>%s</%sDataEmissao>%s' % (namespaceprefix_ , self.gds_format_date(self.DataEmissao, input_name='DataEmissao'), namespaceprefix_ , eol_))
        if self.StatusRPS is not None:
            namespaceprefix_ = self.StatusRPS_nsprefix_ + ':' if (UseCapturedNS_ and self.StatusRPS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStatusRPS>%s</%sStatusRPS>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.StatusRPS), input_name='StatusRPS')), namespaceprefix_ , eol_))
        if self.TributacaoRPS is not None:
            namespaceprefix_ = self.TributacaoRPS_nsprefix_ + ':' if (UseCapturedNS_ and self.TributacaoRPS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTributacaoRPS>%s</%sTributacaoRPS>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.TributacaoRPS), input_name='TributacaoRPS')), namespaceprefix_ , eol_))
        if self.ValorServicos is not None:
            namespaceprefix_ = self.ValorServicos_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorServicos_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorServicos>%s</%sValorServicos>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorServicos, input_name='ValorServicos'), namespaceprefix_ , eol_))
        if self.ValorDeducoes is not None:
            namespaceprefix_ = self.ValorDeducoes_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorDeducoes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorDeducoes>%s</%sValorDeducoes>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorDeducoes, input_name='ValorDeducoes'), namespaceprefix_ , eol_))
        if self.ValorPIS is not None:
            namespaceprefix_ = self.ValorPIS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPIS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPIS>%s</%sValorPIS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorPIS, input_name='ValorPIS'), namespaceprefix_ , eol_))
        if self.ValorCOFINS is not None:
            namespaceprefix_ = self.ValorCOFINS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCOFINS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCOFINS>%s</%sValorCOFINS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCOFINS, input_name='ValorCOFINS'), namespaceprefix_ , eol_))
        if self.ValorINSS is not None:
            namespaceprefix_ = self.ValorINSS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorINSS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorINSS>%s</%sValorINSS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorINSS, input_name='ValorINSS'), namespaceprefix_ , eol_))
        if self.ValorIR is not None:
            namespaceprefix_ = self.ValorIR_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorIR_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorIR>%s</%sValorIR>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorIR, input_name='ValorIR'), namespaceprefix_ , eol_))
        if self.ValorCSLL is not None:
            namespaceprefix_ = self.ValorCSLL_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCSLL_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCSLL>%s</%sValorCSLL>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCSLL, input_name='ValorCSLL'), namespaceprefix_ , eol_))
        if self.CodigoServico is not None:
            namespaceprefix_ = self.CodigoServico_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoServico_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoServico>%s</%sCodigoServico>%s' % (namespaceprefix_ , self.gds_format_integer(self.CodigoServico, input_name='CodigoServico'), namespaceprefix_ , eol_))
        if self.AliquotaServicos is not None:
            namespaceprefix_ = self.AliquotaServicos_nsprefix_ + ':' if (UseCapturedNS_ and self.AliquotaServicos_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAliquotaServicos>%s</%sAliquotaServicos>%s' % (namespaceprefix_ , self.gds_format_decimal(self.AliquotaServicos, input_name='AliquotaServicos'), namespaceprefix_ , eol_))
        if self.ISSRetido is not None:
            namespaceprefix_ = self.ISSRetido_nsprefix_ + ':' if (UseCapturedNS_ and self.ISSRetido_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sISSRetido>%s</%sISSRetido>%s' % (namespaceprefix_ , self.gds_format_boolean(self.ISSRetido, input_name='ISSRetido'), namespaceprefix_ , eol_))
        if self.CPFCNPJTomador is not None:
            namespaceprefix_ = self.CPFCNPJTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.CPFCNPJTomador_nsprefix_) else ''
            self.CPFCNPJTomador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CPFCNPJTomador', pretty_print=pretty_print)
        if self.InscricaoMunicipalTomador is not None:
            namespaceprefix_ = self.InscricaoMunicipalTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipalTomador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipalTomador>%s</%sInscricaoMunicipalTomador>%s' % (namespaceprefix_ , self.gds_format_integer(self.InscricaoMunicipalTomador, input_name='InscricaoMunicipalTomador'), namespaceprefix_ , eol_))
        if self.InscricaoEstadualTomador is not None:
            namespaceprefix_ = self.InscricaoEstadualTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoEstadualTomador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoEstadualTomador>%s</%sInscricaoEstadualTomador>%s' % (namespaceprefix_ , self.gds_format_integer(self.InscricaoEstadualTomador, input_name='InscricaoEstadualTomador'), namespaceprefix_ , eol_))
        if self.RazaoSocialTomador is not None:
            namespaceprefix_ = self.RazaoSocialTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.RazaoSocialTomador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sRazaoSocialTomador>%s</%sRazaoSocialTomador>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.RazaoSocialTomador), input_name='RazaoSocialTomador')), namespaceprefix_ , eol_))
        if self.EnderecoTomador is not None:
            namespaceprefix_ = self.EnderecoTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.EnderecoTomador_nsprefix_) else ''
            self.EnderecoTomador.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EnderecoTomador', pretty_print=pretty_print)
        if self.EmailTomador is not None:
            namespaceprefix_ = self.EmailTomador_nsprefix_ + ':' if (UseCapturedNS_ and self.EmailTomador_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEmailTomador>%s</%sEmailTomador>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EmailTomador), input_name='EmailTomador')), namespaceprefix_ , eol_))
        if self.CPFCNPJIntermediario is not None:
            namespaceprefix_ = self.CPFCNPJIntermediario_nsprefix_ + ':' if (UseCapturedNS_ and self.CPFCNPJIntermediario_nsprefix_) else ''
            self.CPFCNPJIntermediario.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CPFCNPJIntermediario', pretty_print=pretty_print)
        if self.InscricaoMunicipalIntermediario is not None:
            namespaceprefix_ = self.InscricaoMunicipalIntermediario_nsprefix_ + ':' if (UseCapturedNS_ and self.InscricaoMunicipalIntermediario_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sInscricaoMunicipalIntermediario>%s</%sInscricaoMunicipalIntermediario>%s' % (namespaceprefix_ , self.gds_format_integer(self.InscricaoMunicipalIntermediario, input_name='InscricaoMunicipalIntermediario'), namespaceprefix_ , eol_))
        if self.ISSRetidoIntermediario is not None:
            namespaceprefix_ = self.ISSRetidoIntermediario_nsprefix_ + ':' if (UseCapturedNS_ and self.ISSRetidoIntermediario_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sISSRetidoIntermediario>%s</%sISSRetidoIntermediario>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ISSRetidoIntermediario), input_name='ISSRetidoIntermediario')), namespaceprefix_ , eol_))
        if self.EmailIntermediario is not None:
            namespaceprefix_ = self.EmailIntermediario_nsprefix_ + ':' if (UseCapturedNS_ and self.EmailIntermediario_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEmailIntermediario>%s</%sEmailIntermediario>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.EmailIntermediario), input_name='EmailIntermediario')), namespaceprefix_ , eol_))
        if self.Discriminacao is not None:
            namespaceprefix_ = self.Discriminacao_nsprefix_ + ':' if (UseCapturedNS_ and self.Discriminacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDiscriminacao>%s</%sDiscriminacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Discriminacao), input_name='Discriminacao')), namespaceprefix_ , eol_))
        if self.ValorCargaTributaria is not None:
            namespaceprefix_ = self.ValorCargaTributaria_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCargaTributaria_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCargaTributaria>%s</%sValorCargaTributaria>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCargaTributaria, input_name='ValorCargaTributaria'), namespaceprefix_ , eol_))
        if self.PercentualCargaTributaria is not None:
            namespaceprefix_ = self.PercentualCargaTributaria_nsprefix_ + ':' if (UseCapturedNS_ and self.PercentualCargaTributaria_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPercentualCargaTributaria>%s</%sPercentualCargaTributaria>%s' % (namespaceprefix_ , self.gds_format_decimal(self.PercentualCargaTributaria, input_name='PercentualCargaTributaria'), namespaceprefix_ , eol_))
        if self.FonteCargaTributaria is not None:
            namespaceprefix_ = self.FonteCargaTributaria_nsprefix_ + ':' if (UseCapturedNS_ and self.FonteCargaTributaria_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sFonteCargaTributaria>%s</%sFonteCargaTributaria>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.FonteCargaTributaria), input_name='FonteCargaTributaria')), namespaceprefix_ , eol_))
        if self.CodigoCEI is not None:
            namespaceprefix_ = self.CodigoCEI_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoCEI_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoCEI>%s</%sCodigoCEI>%s' % (namespaceprefix_ , self.gds_format_integer(self.CodigoCEI, input_name='CodigoCEI'), namespaceprefix_ , eol_))
        if self.MatriculaObra is not None:
            namespaceprefix_ = self.MatriculaObra_nsprefix_ + ':' if (UseCapturedNS_ and self.MatriculaObra_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMatriculaObra>%s</%sMatriculaObra>%s' % (namespaceprefix_ , self.gds_format_integer(self.MatriculaObra, input_name='MatriculaObra'), namespaceprefix_ , eol_))
        if self.MunicipioPrestacao is not None:
            namespaceprefix_ = self.MunicipioPrestacao_nsprefix_ + ':' if (UseCapturedNS_ and self.MunicipioPrestacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sMunicipioPrestacao>%s</%sMunicipioPrestacao>%s' % (namespaceprefix_ , self.gds_format_integer(self.MunicipioPrestacao, input_name='MunicipioPrestacao'), namespaceprefix_ , eol_))
        if self.NumeroEncapsulamento is not None:
            namespaceprefix_ = self.NumeroEncapsulamento_nsprefix_ + ':' if (UseCapturedNS_ and self.NumeroEncapsulamento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNumeroEncapsulamento>%s</%sNumeroEncapsulamento>%s' % (namespaceprefix_ , self.gds_format_integer(self.NumeroEncapsulamento, input_name='NumeroEncapsulamento'), namespaceprefix_ , eol_))
        if self.ValorTotalRecebido is not None:
            namespaceprefix_ = self.ValorTotalRecebido_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorTotalRecebido_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorTotalRecebido>%s</%sValorTotalRecebido>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorTotalRecebido, input_name='ValorTotalRecebido'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Assinatura':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Assinatura')
            else:
                bval_ = None
            self.Assinatura = bval_
            self.Assinatura_nsprefix_ = child_.prefix
            # validate type tpAssinatura
            self.validate_tpAssinatura(self.Assinatura)
        elif nodeName_ == 'ChaveRPS':
            obj_ = tpChaveRPS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChaveRPS = obj_
            obj_.original_tagname_ = 'ChaveRPS'
        elif nodeName_ == 'TipoRPS':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TipoRPS')
            value_ = self.gds_validate_string(value_, node, 'TipoRPS')
            self.TipoRPS = value_
            self.TipoRPS_nsprefix_ = child_.prefix
            # validate type tpTipoRPS
            self.validate_tpTipoRPS(self.TipoRPS)
        elif nodeName_ == 'DataEmissao':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.DataEmissao = dval_
            self.DataEmissao_nsprefix_ = child_.prefix
        elif nodeName_ == 'StatusRPS':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'StatusRPS')
            value_ = self.gds_validate_string(value_, node, 'StatusRPS')
            self.StatusRPS = value_
            self.StatusRPS_nsprefix_ = child_.prefix
            # validate type tpStatusNFe
            self.validate_tpStatusNFe(self.StatusRPS)
        elif nodeName_ == 'TributacaoRPS':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'TributacaoRPS')
            value_ = self.gds_validate_string(value_, node, 'TributacaoRPS')
            self.TributacaoRPS = value_
            self.TributacaoRPS_nsprefix_ = child_.prefix
            # validate type tpTributacaoNFe
            self.validate_tpTributacaoNFe(self.TributacaoRPS)
        elif nodeName_ == 'ValorServicos' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorServicos')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorServicos')
            self.ValorServicos = fval_
            self.ValorServicos_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorServicos)
        elif nodeName_ == 'ValorDeducoes' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorDeducoes')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorDeducoes')
            self.ValorDeducoes = fval_
            self.ValorDeducoes_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorDeducoes)
        elif nodeName_ == 'ValorPIS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorPIS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorPIS')
            self.ValorPIS = fval_
            self.ValorPIS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorPIS)
        elif nodeName_ == 'ValorCOFINS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCOFINS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCOFINS')
            self.ValorCOFINS = fval_
            self.ValorCOFINS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorCOFINS)
        elif nodeName_ == 'ValorINSS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorINSS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorINSS')
            self.ValorINSS = fval_
            self.ValorINSS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorINSS)
        elif nodeName_ == 'ValorIR' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorIR')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorIR')
            self.ValorIR = fval_
            self.ValorIR_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorIR)
        elif nodeName_ == 'ValorCSLL' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCSLL')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCSLL')
            self.ValorCSLL = fval_
            self.ValorCSLL_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorCSLL)
        elif nodeName_ == 'CodigoServico' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CodigoServico')
            ival_ = self.gds_validate_integer(ival_, node, 'CodigoServico')
            self.CodigoServico = ival_
            self.CodigoServico_nsprefix_ = child_.prefix
            # validate type tpCodigoServico
            self.validate_tpCodigoServico(self.CodigoServico)
        elif nodeName_ == 'AliquotaServicos' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'AliquotaServicos')
            fval_ = self.gds_validate_decimal(fval_, node, 'AliquotaServicos')
            self.AliquotaServicos = fval_
            self.AliquotaServicos_nsprefix_ = child_.prefix
            # validate type tpAliquota
            self.validate_tpAliquota(self.AliquotaServicos)
        elif nodeName_ == 'ISSRetido':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'ISSRetido')
            ival_ = self.gds_validate_boolean(ival_, node, 'ISSRetido')
            self.ISSRetido = ival_
            self.ISSRetido_nsprefix_ = child_.prefix
        elif nodeName_ == 'CPFCNPJTomador':
            obj_ = tpCPFCNPJ.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CPFCNPJTomador = obj_
            obj_.original_tagname_ = 'CPFCNPJTomador'
        elif nodeName_ == 'InscricaoMunicipalTomador' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'InscricaoMunicipalTomador')
            ival_ = self.gds_validate_integer(ival_, node, 'InscricaoMunicipalTomador')
            self.InscricaoMunicipalTomador = ival_
            self.InscricaoMunicipalTomador_nsprefix_ = child_.prefix
            # validate type tpInscricaoMunicipal
            self.validate_tpInscricaoMunicipal(self.InscricaoMunicipalTomador)
        elif nodeName_ == 'InscricaoEstadualTomador' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'InscricaoEstadualTomador')
            ival_ = self.gds_validate_integer(ival_, node, 'InscricaoEstadualTomador')
            self.InscricaoEstadualTomador = ival_
            self.InscricaoEstadualTomador_nsprefix_ = child_.prefix
            # validate type tpInscricaoEstadual
            self.validate_tpInscricaoEstadual(self.InscricaoEstadualTomador)
        elif nodeName_ == 'RazaoSocialTomador':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'RazaoSocialTomador')
            value_ = self.gds_validate_string(value_, node, 'RazaoSocialTomador')
            self.RazaoSocialTomador = value_
            self.RazaoSocialTomador_nsprefix_ = child_.prefix
            # validate type tpRazaoSocial
            self.validate_tpRazaoSocial(self.RazaoSocialTomador)
        elif nodeName_ == 'EnderecoTomador':
            obj_ = tpEndereco.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EnderecoTomador = obj_
            obj_.original_tagname_ = 'EnderecoTomador'
        elif nodeName_ == 'EmailTomador':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EmailTomador')
            value_ = self.gds_validate_string(value_, node, 'EmailTomador')
            self.EmailTomador = value_
            self.EmailTomador_nsprefix_ = child_.prefix
            # validate type tpEmail
            self.validate_tpEmail(self.EmailTomador)
        elif nodeName_ == 'CPFCNPJIntermediario':
            obj_ = tpCPFCNPJ.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CPFCNPJIntermediario = obj_
            obj_.original_tagname_ = 'CPFCNPJIntermediario'
        elif nodeName_ == 'InscricaoMunicipalIntermediario' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'InscricaoMunicipalIntermediario')
            ival_ = self.gds_validate_integer(ival_, node, 'InscricaoMunicipalIntermediario')
            self.InscricaoMunicipalIntermediario = ival_
            self.InscricaoMunicipalIntermediario_nsprefix_ = child_.prefix
            # validate type tpInscricaoMunicipal
            self.validate_tpInscricaoMunicipal(self.InscricaoMunicipalIntermediario)
        elif nodeName_ == 'ISSRetidoIntermediario':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ISSRetidoIntermediario')
            value_ = self.gds_validate_string(value_, node, 'ISSRetidoIntermediario')
            self.ISSRetidoIntermediario = value_
            self.ISSRetidoIntermediario_nsprefix_ = child_.prefix
        elif nodeName_ == 'EmailIntermediario':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'EmailIntermediario')
            value_ = self.gds_validate_string(value_, node, 'EmailIntermediario')
            self.EmailIntermediario = value_
            self.EmailIntermediario_nsprefix_ = child_.prefix
            # validate type tpEmail
            self.validate_tpEmail(self.EmailIntermediario)
        elif nodeName_ == 'Discriminacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Discriminacao')
            value_ = self.gds_validate_string(value_, node, 'Discriminacao')
            self.Discriminacao = value_
            self.Discriminacao_nsprefix_ = child_.prefix
            # validate type tpDiscriminacao
            self.validate_tpDiscriminacao(self.Discriminacao)
        elif nodeName_ == 'ValorCargaTributaria' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCargaTributaria')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCargaTributaria')
            self.ValorCargaTributaria = fval_
            self.ValorCargaTributaria_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorCargaTributaria)
        elif nodeName_ == 'PercentualCargaTributaria' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'PercentualCargaTributaria')
            fval_ = self.gds_validate_decimal(fval_, node, 'PercentualCargaTributaria')
            self.PercentualCargaTributaria = fval_
            self.PercentualCargaTributaria_nsprefix_ = child_.prefix
            # validate type tpPercentualCargaTributaria
            self.validate_tpPercentualCargaTributaria(self.PercentualCargaTributaria)
        elif nodeName_ == 'FonteCargaTributaria':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'FonteCargaTributaria')
            value_ = self.gds_validate_string(value_, node, 'FonteCargaTributaria')
            self.FonteCargaTributaria = value_
            self.FonteCargaTributaria_nsprefix_ = child_.prefix
            # validate type tpFonteCargaTributaria
            self.validate_tpFonteCargaTributaria(self.FonteCargaTributaria)
        elif nodeName_ == 'CodigoCEI' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CodigoCEI')
            ival_ = self.gds_validate_integer(ival_, node, 'CodigoCEI')
            self.CodigoCEI = ival_
            self.CodigoCEI_nsprefix_ = child_.prefix
            # validate type tpNumero
            self.validate_tpNumero(self.CodigoCEI)
        elif nodeName_ == 'MatriculaObra' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'MatriculaObra')
            ival_ = self.gds_validate_integer(ival_, node, 'MatriculaObra')
            self.MatriculaObra = ival_
            self.MatriculaObra_nsprefix_ = child_.prefix
            # validate type tpNumero
            self.validate_tpNumero(self.MatriculaObra)
        elif nodeName_ == 'MunicipioPrestacao' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'MunicipioPrestacao')
            ival_ = self.gds_validate_integer(ival_, node, 'MunicipioPrestacao')
            self.MunicipioPrestacao = ival_
            self.MunicipioPrestacao_nsprefix_ = child_.prefix
            # validate type tpCidade
            self.validate_tpCidade(self.MunicipioPrestacao)
        elif nodeName_ == 'NumeroEncapsulamento' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NumeroEncapsulamento')
            ival_ = self.gds_validate_integer(ival_, node, 'NumeroEncapsulamento')
            self.NumeroEncapsulamento = ival_
            self.NumeroEncapsulamento_nsprefix_ = child_.prefix
            # validate type tpNumero
            self.validate_tpNumero(self.NumeroEncapsulamento)
        elif nodeName_ == 'ValorTotalRecebido' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorTotalRecebido')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorTotalRecebido')
            self.ValorTotalRecebido = fval_
            self.ValorTotalRecebido_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorTotalRecebido)
# end class tpRPS


class SignatureType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional'}),
        MemberSpec_('SignedInfo', 'SignedInfoType', 0, 0, {'name': 'SignedInfo', 'type': 'SignedInfoType'}, None),
        MemberSpec_('SignatureValue', 'SignatureValueType', 0, 0, {'name': 'SignatureValue', 'type': 'SignatureValueType'}, None),
        MemberSpec_('KeyInfo', 'KeyInfoType', 0, 0, {'name': 'KeyInfo', 'type': 'KeyInfoType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, SignedInfo=None, SignatureValue=None, KeyInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.SignedInfo = SignedInfo
        self.SignedInfo_nsprefix_ = None
        self.SignatureValue = SignatureValue
        self.SignatureValue_nsprefix_ = None
        self.KeyInfo = KeyInfo
        self.KeyInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureType.subclass:
            return SignatureType.subclass(*args_, **kwargs_)
        else:
            return SignatureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.SignedInfo is not None or
            self.SignatureValue is not None or
            self.KeyInfo is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SignedInfo is not None:
            namespaceprefix_ = self.SignedInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.SignedInfo_nsprefix_) else ''
            self.SignedInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SignedInfo', pretty_print=pretty_print)
        if self.SignatureValue is not None:
            namespaceprefix_ = self.SignatureValue_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureValue_nsprefix_) else ''
            self.SignatureValue.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SignatureValue', pretty_print=pretty_print)
        if self.KeyInfo is not None:
            namespaceprefix_ = self.KeyInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyInfo_nsprefix_) else ''
            self.KeyInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='KeyInfo', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SignedInfo':
            obj_ = SignedInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignedInfo = obj_
            obj_.original_tagname_ = 'SignedInfo'
        elif nodeName_ == 'SignatureValue':
            obj_ = SignatureValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureValue = obj_
            obj_.original_tagname_ = 'SignatureValue'
        elif nodeName_ == 'KeyInfo':
            obj_ = KeyInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KeyInfo = obj_
            obj_.original_tagname_ = 'KeyInfo'
# end class SignatureType


class SignatureValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional'}),
        MemberSpec_('valueOf_', 'xs:base64Binary', 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureValueType.subclass:
            return SignatureValueType.subclass(*args_, **kwargs_)
        else:
            return SignatureValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureValueType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureValueType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureValueType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValueType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SignatureValueType


class SignedInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional'}),
        MemberSpec_('CanonicalizationMethod', 'CanonicalizationMethodType', 0, 0, {'name': 'CanonicalizationMethod', 'type': 'CanonicalizationMethodType'}, None),
        MemberSpec_('SignatureMethod', 'SignatureMethodType', 0, 0, {'name': 'SignatureMethod', 'type': 'SignatureMethodType'}, None),
        MemberSpec_('Reference', 'ReferenceType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'Reference', 'type': 'ReferenceType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, CanonicalizationMethod=None, SignatureMethod=None, Reference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.CanonicalizationMethod = CanonicalizationMethod
        self.CanonicalizationMethod_nsprefix_ = None
        self.SignatureMethod = SignatureMethod
        self.SignatureMethod_nsprefix_ = None
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
        self.Reference_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignedInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignedInfoType.subclass:
            return SignedInfoType.subclass(*args_, **kwargs_)
        else:
            return SignedInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.CanonicalizationMethod is not None or
            self.SignatureMethod is not None or
            self.Reference
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignedInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignedInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignedInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignedInfoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignedInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignedInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignedInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CanonicalizationMethod is not None:
            namespaceprefix_ = self.CanonicalizationMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.CanonicalizationMethod_nsprefix_) else ''
            self.CanonicalizationMethod.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CanonicalizationMethod', pretty_print=pretty_print)
        if self.SignatureMethod is not None:
            namespaceprefix_ = self.SignatureMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureMethod_nsprefix_) else ''
            self.SignatureMethod.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SignatureMethod', pretty_print=pretty_print)
        for Reference_ in self.Reference:
            namespaceprefix_ = self.Reference_nsprefix_ + ':' if (UseCapturedNS_ and self.Reference_nsprefix_) else ''
            Reference_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Reference', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CanonicalizationMethod':
            obj_ = CanonicalizationMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CanonicalizationMethod = obj_
            obj_.original_tagname_ = 'CanonicalizationMethod'
        elif nodeName_ == 'SignatureMethod':
            obj_ = SignatureMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureMethod = obj_
            obj_.original_tagname_ = 'SignatureMethod'
        elif nodeName_ == 'Reference':
            obj_ = ReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Reference.append(obj_)
            obj_.original_tagname_ = 'Reference'
# end class SignedInfoType


class ReferenceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional'}),
        MemberSpec_('URI', 'xs:anyURI', 0, 1, {'use': 'optional'}),
        MemberSpec_('Type', 'xs:anyURI', 0, 1, {'use': 'optional'}),
        MemberSpec_('Transforms', 'TransformsType', 0, 0, {'name': 'Transforms', 'type': 'TransformsType'}, None),
        MemberSpec_('DigestMethod', 'DigestMethodType', 0, 0, {'name': 'DigestMethod', 'type': 'DigestMethodType'}, None),
        MemberSpec_('DigestValue', ['DigestValueType', 'xs:base64Binary'], 0, 0, {'name': 'DigestValue', 'type': 'xs:base64Binary'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, URI=None, Type=None, Transforms=None, DigestMethod=None, DigestValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.URI = _cast(None, URI)
        self.URI_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Transforms = Transforms
        self.Transforms_nsprefix_ = None
        self.DigestMethod = DigestMethod
        self.DigestMethod_nsprefix_ = None
        self.DigestValue = DigestValue
        self.validate_DigestValueType(self.DigestValue)
        self.DigestValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReferenceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReferenceType.subclass:
            return ReferenceType.subclass(*args_, **kwargs_)
        else:
            return ReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_DigestValueType(self, value):
        result = True
        # Validate type DigestValueType, a restriction on xs:base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def hasContent_(self):
        if (
            self.Transforms is not None or
            self.DigestMethod is not None or
            self.DigestValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='ReferenceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReferenceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReferenceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReferenceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReferenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='ReferenceType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            outfile.write(' URI=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.URI), input_name='URI')), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Type), input_name='Type')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='ReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transforms is not None:
            namespaceprefix_ = self.Transforms_nsprefix_ + ':' if (UseCapturedNS_ and self.Transforms_nsprefix_) else ''
            self.Transforms.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Transforms', pretty_print=pretty_print)
        if self.DigestMethod is not None:
            namespaceprefix_ = self.DigestMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.DigestMethod_nsprefix_) else ''
            self.DigestMethod.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DigestMethod', pretty_print=pretty_print)
        if self.DigestValue is not None:
            namespaceprefix_ = self.DigestValue_nsprefix_ + ':' if (UseCapturedNS_ and self.DigestValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDigestValue>%s</%sDigestValue>%s' % (namespaceprefix_ , self.gds_format_base64(self.DigestValue, input_name='DigestValue'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        value = find_attr_value_('URI', node)
        if value is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            self.URI = value
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transforms':
            obj_ = TransformsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transforms = obj_
            obj_.original_tagname_ = 'Transforms'
        elif nodeName_ == 'DigestMethod':
            obj_ = DigestMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DigestMethod = obj_
            obj_.original_tagname_ = 'DigestMethod'
        elif nodeName_ == 'DigestValue':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'DigestValue')
            else:
                bval_ = None
            self.DigestValue = bval_
            self.DigestValue_nsprefix_ = child_.prefix
            # validate type DigestValueType
            self.validate_DigestValueType(self.DigestValue)
# end class ReferenceType


class TransformsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Transform', 'TransformType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'Transform', 'type': 'TransformType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Transform=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Transform is None:
            self.Transform = []
        else:
            self.Transform = Transform
        self.Transform_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransformsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransformsType.subclass:
            return TransformsType.subclass(*args_, **kwargs_)
        else:
            return TransformsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Transform
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransformsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransformsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransformsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Transform_ in self.Transform:
            namespaceprefix_ = self.Transform_nsprefix_ + ':' if (UseCapturedNS_ and self.Transform_nsprefix_) else ''
            Transform_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Transform', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transform':
            obj_ = TransformType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transform.append(obj_)
            obj_.original_tagname_ = 'Transform'
# end class TransformsType


class TransformType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'xs:anyURI', 0, 0, {'use': 'required'}),
        MemberSpec_('XPath', 'xs:string', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'XPath', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, XPath=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        if XPath is None:
            self.XPath = []
        else:
            self.XPath = XPath
        self.XPath_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransformType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransformType.subclass:
            return TransformType.subclass(*args_, **kwargs_)
        else:
            return TransformType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.XPath
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransformType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransformType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransformType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Algorithm), input_name='Algorithm')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for XPath_ in self.XPath:
            namespaceprefix_ = self.XPath_nsprefix_ + ':' if (UseCapturedNS_ and self.XPath_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sXPath>%s</%sXPath>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(XPath_), input_name='XPath')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'XPath':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'XPath')
            value_ = self.gds_validate_string(value_, node, 'XPath')
            self.XPath.append(value_)
            self.XPath_nsprefix_ = child_.prefix
# end class TransformType


class KeyInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional'}),
        MemberSpec_('X509Data', 'X509DataType', 0, 0, {'name': 'X509Data', 'type': 'X509DataType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, X509Data=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.X509Data = X509Data
        self.X509Data_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyInfoType.subclass:
            return KeyInfoType.subclass(*args_, **kwargs_)
        else:
            return KeyInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.X509Data is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyInfoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='KeyInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='KeyInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.X509Data is not None:
            namespaceprefix_ = self.X509Data_nsprefix_ + ':' if (UseCapturedNS_ and self.X509Data_nsprefix_) else ''
            self.X509Data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='X509Data', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'X509Data':
            obj_ = X509DataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.X509Data = obj_
            obj_.original_tagname_ = 'X509Data'
# end class KeyInfoType


class KeyValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('RSAKeyValue', 'RSAKeyValueType', 0, 0, {'name': 'RSAKeyValue', 'type': 'RSAKeyValueType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, RSAKeyValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.RSAKeyValue = RSAKeyValue
        self.RSAKeyValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyValueType.subclass:
            return KeyValueType.subclass(*args_, **kwargs_)
        else:
            return KeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.RSAKeyValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyValueType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='KeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='KeyValueType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.RSAKeyValue is not None:
            namespaceprefix_ = self.RSAKeyValue_nsprefix_ + ':' if (UseCapturedNS_ and self.RSAKeyValue_nsprefix_) else ''
            self.RSAKeyValue.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RSAKeyValue', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'RSAKeyValue':
            obj_ = RSAKeyValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RSAKeyValue = obj_
            obj_.original_tagname_ = 'RSAKeyValue'
# end class KeyValueType


class X509DataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('X509Certificate', 'xs:base64Binary', 0, 0, {'name': 'X509Certificate', 'type': 'xs:base64Binary'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, X509Certificate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.X509Certificate = X509Certificate
        self.X509Certificate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, X509DataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if X509DataType.subclass:
            return X509DataType.subclass(*args_, **kwargs_)
        else:
            return X509DataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.X509Certificate is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509DataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('X509DataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'X509DataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='X509DataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='X509DataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='X509DataType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509DataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.X509Certificate is not None:
            namespaceprefix_ = self.X509Certificate_nsprefix_ + ':' if (UseCapturedNS_ and self.X509Certificate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509Certificate>%s</%sX509Certificate>%s' % (namespaceprefix_ , self.gds_format_base64(self.X509Certificate, input_name='X509Certificate'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'X509Certificate':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'X509Certificate')
            else:
                bval_ = None
            self.X509Certificate = bval_
            self.X509Certificate_nsprefix_ = child_.prefix
# end class X509DataType


class CabecalhoType(GeneratedsSuper):
    """Cabeçalho do pedido.Informe a Versão do Schema XML utilizado."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Versao', 'tipos:tpVersao', 0, 0, {'use': 'required'}),
        MemberSpec_('CPFCNPJRemetente', 'tpCPFCNPJ', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CPFCNPJRemetente', 'type': 'tpCPFCNPJ'}, None),
        MemberSpec_('transacao', 'xs:boolean', 0, 0, {'default': 'true', 'maxOccurs': '1', 'minOccurs': '1', 'name': 'transacao', 'type': 'xs:boolean'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Versao='1', CPFCNPJRemetente=None, transacao=True, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Versao = _cast(None, Versao)
        self.Versao_nsprefix_ = None
        self.CPFCNPJRemetente = CPFCNPJRemetente
        self.CPFCNPJRemetente_nsprefix_ = None
        self.transacao = transacao
        self.transacao_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CabecalhoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CabecalhoType.subclass:
            return CabecalhoType.subclass(*args_, **kwargs_)
        else:
            return CabecalhoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpVersao(self, value):
        # Validate type tipos:tpVersao, a restriction on xs:long.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpVersao_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpVersao_patterns_, ))
    validate_tpVersao_patterns_ = [['^([0-9]{1,3})$']]
    def hasContent_(self):
        if (
            self.CPFCNPJRemetente is not None or
            not self.transacao
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CabecalhoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CabecalhoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CabecalhoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CabecalhoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CabecalhoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CabecalhoType'):
        if self.Versao is not None and 'Versao' not in already_processed:
            already_processed.add('Versao')
            outfile.write(' Versao="%s"' % self.gds_format_integer(self.Versao, input_name='Versao'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CabecalhoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CPFCNPJRemetente is not None:
            namespaceprefix_ = self.CPFCNPJRemetente_nsprefix_ + ':' if (UseCapturedNS_ and self.CPFCNPJRemetente_nsprefix_) else ''
            self.CPFCNPJRemetente.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CPFCNPJRemetente', pretty_print=pretty_print)
        if self.transacao is not None:
            namespaceprefix_ = self.transacao_nsprefix_ + ':' if (UseCapturedNS_ and self.transacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stransacao>%s</%stransacao>%s' % (namespaceprefix_ , self.gds_format_boolean(self.transacao, input_name='transacao'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Versao', node)
        if value is not None and 'Versao' not in already_processed:
            already_processed.add('Versao')
            self.Versao = self.gds_parse_integer(value, node, 'Versao')
            self.validate_tpVersao(self.Versao)    # validate type tpVersao
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CPFCNPJRemetente':
            obj_ = tpCPFCNPJ.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CPFCNPJRemetente = obj_
            obj_.original_tagname_ = 'CPFCNPJRemetente'
        elif nodeName_ == 'transacao':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'transacao')
            ival_ = self.gds_validate_boolean(ival_, node, 'transacao')
            self.transacao = ival_
            self.transacao_nsprefix_ = child_.prefix
# end class CabecalhoType


class DetalheType(GeneratedsSuper):
    """Detalhe do pedido de cancelamento de NFS-e. Cada detalhe deverá conter a
    Chave de uma NFS-e e sua respectiva assinatura de cancelamento."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('ChaveNFe', 'tpChaveNFe', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ChaveNFe', 'type': 'tpChaveNFe'}, None),
        MemberSpec_('AssinaturaCancelamento', ['tpAssinaturaCancelamento', 'xs:base64Binary'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'AssinaturaCancelamento', 'type': 'xs:base64Binary'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, ChaveNFe=None, AssinaturaCancelamento=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ChaveNFe = ChaveNFe
        self.ChaveNFe_nsprefix_ = None
        self.AssinaturaCancelamento = AssinaturaCancelamento
        self.validate_tpAssinaturaCancelamento(self.AssinaturaCancelamento)
        self.AssinaturaCancelamento_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DetalheType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DetalheType.subclass:
            return DetalheType.subclass(*args_, **kwargs_)
        else:
            return DetalheType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpAssinaturaCancelamento(self, value):
        result = True
        # Validate type tpAssinaturaCancelamento, a restriction on xs:base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def hasContent_(self):
        if (
            self.ChaveNFe is not None or
            self.AssinaturaCancelamento is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DetalheType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DetalheType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DetalheType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DetalheType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DetalheType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DetalheType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DetalheType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ChaveNFe is not None:
            namespaceprefix_ = self.ChaveNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.ChaveNFe_nsprefix_) else ''
            self.ChaveNFe.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChaveNFe', pretty_print=pretty_print)
        if self.AssinaturaCancelamento is not None:
            namespaceprefix_ = self.AssinaturaCancelamento_nsprefix_ + ':' if (UseCapturedNS_ and self.AssinaturaCancelamento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAssinaturaCancelamento>%s</%sAssinaturaCancelamento>%s' % (namespaceprefix_ , self.gds_format_string(self.AssinaturaCancelamento, input_name='AssinaturaCancelamento'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ChaveNFe':
            obj_ = tpChaveNFe.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChaveNFe = obj_
            obj_.original_tagname_ = 'ChaveNFe'
        elif nodeName_ == 'AssinaturaCancelamento':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'AssinaturaCancelamento')
            else:
                bval_ = None
            self.AssinaturaCancelamento = bval_
            self.AssinaturaCancelamento_nsprefix_ = child_.prefix
            # validate type tpAssinaturaCancelamento
            self.validate_tpAssinaturaCancelamento(self.AssinaturaCancelamento)
# end class DetalheType


class CanonicalizationMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'xs:anyURI', 0, 0, {'use': 'required'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CanonicalizationMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CanonicalizationMethodType.subclass:
            return CanonicalizationMethodType.subclass(*args_, **kwargs_)
        else:
            return CanonicalizationMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CanonicalizationMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CanonicalizationMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CanonicalizationMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CanonicalizationMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CanonicalizationMethodType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CanonicalizationMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Algorithm), input_name='Algorithm')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CanonicalizationMethodType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CanonicalizationMethodType


class SignatureMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'xs:anyURI', 0, 0, {'use': 'required'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureMethodType.subclass:
            return SignatureMethodType.subclass(*args_, **kwargs_)
        else:
            return SignatureMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SignatureMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureMethodType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SignatureMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Algorithm), input_name='Algorithm')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SignatureMethodType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SignatureMethodType


class DigestMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'xs:anyURI', 0, 0, {'use': 'required'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DigestMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DigestMethodType.subclass:
            return DigestMethodType.subclass(*args_, **kwargs_)
        else:
            return DigestMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DigestMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DigestMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DigestMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DigestMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DigestMethodType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DigestMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Algorithm), input_name='Algorithm')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DigestMethodType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DigestMethodType


class RSAKeyValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Modulus', ['CryptoBinary', 'xs:base64Binary'], 0, 0, {'name': 'Modulus', 'type': 'xs:base64Binary'}, None),
        MemberSpec_('Exponent', ['CryptoBinary', 'xs:base64Binary'], 0, 0, {'name': 'Exponent', 'type': 'xs:base64Binary'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Modulus=None, Exponent=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Modulus = Modulus
        self.validate_CryptoBinary(self.Modulus)
        self.Modulus_nsprefix_ = None
        self.Exponent = Exponent
        self.validate_CryptoBinary(self.Exponent)
        self.Exponent_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RSAKeyValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RSAKeyValueType.subclass:
            return RSAKeyValueType.subclass(*args_, **kwargs_)
        else:
            return RSAKeyValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_CryptoBinary(self, value):
        result = True
        # Validate type CryptoBinary, a restriction on xs:base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def hasContent_(self):
        if (
            self.Modulus is not None or
            self.Exponent is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RSAKeyValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RSAKeyValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RSAKeyValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RSAKeyValueType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RSAKeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RSAKeyValueType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RSAKeyValueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Modulus is not None:
            namespaceprefix_ = self.Modulus_nsprefix_ + ':' if (UseCapturedNS_ and self.Modulus_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sModulus>%s</%sModulus>%s' % (namespaceprefix_ , self.gds_format_base64(self.Modulus, input_name='Modulus'), namespaceprefix_ , eol_))
        if self.Exponent is not None:
            namespaceprefix_ = self.Exponent_nsprefix_ + ':' if (UseCapturedNS_ and self.Exponent_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sExponent>%s</%sExponent>%s' % (namespaceprefix_ , self.gds_format_base64(self.Exponent, input_name='Exponent'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Modulus':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Modulus')
            else:
                bval_ = None
            self.Modulus = bval_
            self.Modulus_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Modulus)
        elif nodeName_ == 'Exponent':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'Exponent')
            else:
                bval_ = None
            self.Exponent = bval_
            self.Exponent_nsprefix_ = child_.prefix
            # validate type CryptoBinary
            self.validate_CryptoBinary(self.Exponent)
# end class RSAKeyValueType


GDSClassesMapping = {
    'Signature': SignatureType,
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PedidoCancelamentoNFe'
        rootClass = PedidoCancelamentoNFe
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PedidoCancelamentoNFe'
        rootClass = PedidoCancelamentoNFe
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PedidoCancelamentoNFe'
        rootClass = PedidoCancelamentoNFe
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PedidoCancelamentoNFe'
        rootClass = PedidoCancelamentoNFe
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from PedidoCancelamentoNFe import *\n\n')
        sys.stdout.write('import PedidoCancelamentoNFe as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.prefeitura.sp.gov.br/nfe': [],
 'http://www.prefeitura.sp.gov.br/nfe/tipos': [('tpAliquota',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpAssinatura',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpAssinaturaCancelamento',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpBairro',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpCEP',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpCidade',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpCNPJ',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpCodigoServico',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpCodigoEvento',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpCodigoVerificacao',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpComplementoEndereco',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpCPF',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpDescricaoEvento',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpDiscriminacao',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpEmail',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpInscricaoEstadual',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpInscricaoMunicipal',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpLogradouro',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpNumero',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpNumeroEndereco',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpOpcaoSimples',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpQuantidade',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpRazaoSocial',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpSerieRPS',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpStatusNFe',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpSucesso',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpTempoProcessamento',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpTipoLogradouro',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpTipoRPS',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpTributacaoNFe',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpUF',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpValor',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpVersao',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpPercentualCargaTributaria',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpFonteCargaTributaria',
                                                'TiposNFe_v01.xsd',
                                                'ST'),
                                               ('tpEvento',
                                                'TiposNFe_v01.xsd',
                                                'CT'),
                                               ('tpCPFCNPJ',
                                                'TiposNFe_v01.xsd',
                                                'CT'),
                                               ('tpChaveNFeRPS',
                                                'TiposNFe_v01.xsd',
                                                'CT'),
                                               ('tpChaveNFe',
                                                'TiposNFe_v01.xsd',
                                                'CT'),
                                               ('tpChaveRPS',
                                                'TiposNFe_v01.xsd',
                                                'CT'),
                                               ('tpEndereco',
                                                'TiposNFe_v01.xsd',
                                                'CT'),
                                               ('tpInformacoesLote',
                                                'TiposNFe_v01.xsd',
                                                'CT'),
                                               ('tpNFe',
                                                'TiposNFe_v01.xsd',
                                                'CT'),
                                               ('tpRPS',
                                                'TiposNFe_v01.xsd',
                                                'CT')],
 'http://www.w3.org/2000/09/xmldsig#': [('CryptoBinary',
                                         'xmldsig-core-schema_v01.xsd',
                                         'ST'),
                                        ('DigestValueType',
                                         'xmldsig-core-schema_v01.xsd',
                                         'ST'),
                                        ('SignatureType',
                                         'xmldsig-core-schema_v01.xsd',
                                         'CT'),
                                        ('SignatureValueType',
                                         'xmldsig-core-schema_v01.xsd',
                                         'CT'),
                                        ('SignedInfoType',
                                         'xmldsig-core-schema_v01.xsd',
                                         'CT'),
                                        ('ReferenceType',
                                         'xmldsig-core-schema_v01.xsd',
                                         'CT'),
                                        ('TransformsType',
                                         'xmldsig-core-schema_v01.xsd',
                                         'CT'),
                                        ('TransformType',
                                         'xmldsig-core-schema_v01.xsd',
                                         'CT'),
                                        ('KeyInfoType',
                                         'xmldsig-core-schema_v01.xsd',
                                         'CT'),
                                        ('KeyValueType',
                                         'xmldsig-core-schema_v01.xsd',
                                         'CT'),
                                        ('X509DataType',
                                         'xmldsig-core-schema_v01.xsd',
                                         'CT')]}

__all__ = [
    "CabecalhoType",
    "CanonicalizationMethodType",
    "DetalheType",
    "DigestMethodType",
    "KeyInfoType",
    "KeyValueType",
    "PedidoCancelamentoNFe",
    "RSAKeyValueType",
    "ReferenceType",
    "SignatureMethodType",
    "SignatureType",
    "SignatureValueType",
    "SignedInfoType",
    "TransformType",
    "TransformsType",
    "X509DataType",
    "tpCPFCNPJ",
    "tpChaveNFe",
    "tpChaveNFeRPS",
    "tpChaveRPS",
    "tpEndereco",
    "tpEvento",
    "tpInformacoesLote",
    "tpNFe",
    "tpRPS"
]
