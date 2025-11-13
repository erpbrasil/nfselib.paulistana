#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated  by generateDS.py version 2.44.3.
# Python 3.10.12 (main, Nov  4 2025, 08:48:33) [GCC 11.4.0]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('--no-dates', '')
#   ('--member-specs', 'list')
#   ('--use-getter-setter', 'none')
#   ('-f', '')
#   ('-o', 'nfselib/paulistana/v03/RetornoConsulta.py')
#
# Command line arguments:
#   schemas/nfse/RetornoConsulta_v02.xsd
#
# Command line:
#   /home/cristiano/nfse_paulistana/venv/bin/generateDS --no-namespace-defs --no-dates --member-specs="list" --use-getter-setter="none" -f -o "nfselib/paulistana/v03/RetornoConsulta.py" schemas/nfse/RetornoConsulta_v02.xsd
#
# Current working directory (os.getcwd()):
#   nfse_paulistana
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
from lxml import etree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
TagNamePrefix = ""
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
# "xsi:type" attribute value.  See the _exportAttributes method of
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
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

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
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass

    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile('(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00)$')
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
        def __str__(self):
            settings = {
                'str_pretty_print': True,
                'str_indent_level': 0,
                'str_namespaceprefix': '',
                'str_name': self.__class__.__name__,
                'str_namespacedefs': '',
            }
            for n in settings:
                if hasattr(self, n):
                    settings[n] = getattr(self, n)
            if sys.version_info.major == 2:
                from StringIO import StringIO
            else:
                from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings['str_indent_level'],
                pretty_print=settings['str_pretty_print'],
                namespaceprefix_=settings['str_namespaceprefix'],
                name_=settings['str_name'],
                namespacedef_=settings['str_namespacedefs']
            )
            strval = output.getvalue()
            output.close()
            return strval
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
            return base64.b64encode(input_data).decode('ascii')
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % int(input_data)
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
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            value = ('%.15f' % float(input_data)).rstrip('0')
            if value.endswith('.'):
                value += '0'
            return value

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
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
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
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
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
            return '%s' % input_data
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
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
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
            input_data = input_data.strip()
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
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
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
            target = str(target)
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
        Tag_strip_pattern_ = re_.compile(r'{.*}')
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
    s1 = s1.replace('\n', '&#10;')
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
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
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
    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
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
    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
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
# Start enum classes
#
class tpEnteGov(str, Enum):
    """tpEnteGov -- Tipo do ente da compra governamental.

    """
    _1='1' # União.
    _2='2' # Estados.
    _3='3' # Distrito Federal.
    _4='4' # Municípios.


class tpFinNFSe(str, Enum):
    """tpFinNFSe -- Indicador da finalidade da emiss
    ã
    o de NFS-e.

    """
    _0='0' # 0 = NFS-e regular.


class tpIndDest(str, Enum):
    """tpIndDest -- Indica o Destinat
    á
    rio dos servi
    ç
    os.

    """
    _0='0' # O destinatário é o próprio tomador/adquirente identificado na NFS-e (tomador = adquirente = destinatário).
    _1='1' # O destinatário não é o próprio adquirente, podendo ser outra pessoa, física ou jurídica (ou equiparada), ou um estabelecimento diferente do indicado como tomador (tomador = adquirente ≠ destinatário).


class tpNaoNIF(str, Enum):
    """tpNaoNIF -- Tipo do motivo para n
    ã
    o informa
    ç
    ã
    o do NIF.

    """
    _0='0' # 0 - Não informado na nota de origem;
    _1='1' # 1 - Dispensado do NIF;
    _2='2' # 2 - Não exigência do NIF;


class tpNaoSim(str, Enum):
    """tpNaoSim -- Tipo de N
    ã
    o ou Sim.

    """
    _0='0' # Não.
    _1='1' # Sim.


class tpOpcaoSimples(str, Enum):
    """tpOpcaoSimples -- Tipo referente
    à
    s poss
    í
    veis op
    ç
    õ
    es de escolha pelo Simples.

    """
    _0='0' # Não-optante pelo Simples Federal nem Municipal.
    _1='1' # Optante pelo Simples Federal (Alíquota de 1,0%).
    _2='2' # Optante pelo Simples Federal (Alíquota de 0,5%).
    _3='3' # Optante pelo Simples Municipal.
    _4='4' # Optante pelo Simples Nacional - DAS.
    _6='6' # Optante pelo Simples Nacional - DAMSP.


class tpOper(str, Enum):
    """tpOper -- Tipo de Opera
    ç
    ã
    o com Entes Governamentais ou outros servi
    ç
    os sobre bens im
    ó
    veis.

    """
    _1='1' # Fornecimento com pagamento posterior.
    _2='2' # Recebimento do pagamento com fornecimento já realizado.
    _3='3' # Fornecimento com pagamento já realizado.
    _4='4' # Recebimento do pagamento com fornecimento posterior.
    _5='5' # Fornecimento e recebimento do pagamento concomitantes.


class tpReeRepRes(str, Enum):
    """tpReeRepRes -- Tipo de valor inclu
    í
    do neste documento, recebido por motivo de estarem relacionadas a opera
    ç
    õ
    es de terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, j
    á
    tributados e aqui referenciados.
    01 = Repasse de remunera
    ç
    ã
    o por intermedia
    ç
    ã
    o de im
    ó
    veis a demais corretores envolvidos na opera
    ç
    ã
    o.
    02 = Repasse de valores a fornecedor relativo a fornecimento intermediado por ag
    ê
    ncia de turismo.
    03 = Reembolso ou ressarcimento recebido por ag
    ê
    ncia de propaganda e publicidade por valores pagos relativos a servi
    ç
    os de produ
    ç
    ã
    o externa por conta e ordem de terceiro.
    04 = Reembolso ou ressarcimento recebido por ag
    ê
    ncia de propaganda e publicidade por valores pagos relativos a servi
    ç
    os de m
    í
    dia por conta e ordem de terceiro.
    99 = Outros reembolsos ou ressarcimentos recebidos por valores pagos relativos a opera
    ç
    õ
    es por conta e ordem de terceiro.

    """
    _0_1='01' # 01 = Repasse de remuneração por intermediação de imóveis a demais corretores envolvidos na operação
    _0_2='02' # 02 = Repasse de valores a fornecedor relativo a fornecimento intermediado por agência de turismo.
    _0_3='03' # 03 = Reembolso ou ressarcimento recebido por agência de propaganda e publicidade por valores pagos relativos a serviços de produção externa por conta e ordem de terceiro.
    _0_4='04' # 04 = Reembolso ou ressarcimento recebido por agência de propaganda e publicidade por valores pagos relativos a serviços de mídia por conta e ordem de terceiro.
    _9_9='99' # 99 = Outros reembolsos ou ressarcimentos recebidos por valores pagos relativos a operações por conta e ordem de terceiro


class tpReferencia(str, Enum):
    """tpReferencia -- Tipo de refer
    ê
    ncia da nota.

    """
    _0='0' # Nota fiscal referenciada para emissão de nota de multa e juros.
    _1='1' # Nota fiscal de pagamento parcelado antecipado.


class tpStatusNFe(str, Enum):
    """tpStatusNFe -- Tipo referente aos poss
    í
    veis status de NFS-e.

    """
    N='N' # Normal.
    C='C' # Cancelada.
    E='E' # Extraviada.


class tpTipoChaveDFE(str, Enum):
    """tpTipoChaveDFE -- Documento fiscal a que se refere a chaveDfe que seja um dos documentos do Reposit
    ó
    rio Nacional:
    1 - NFS-e.
    2 - NF-e.
    3 - CT-e.
    9 - Outro.

    """
    _1='1' # NFS-e.
    _2='2' # NF-e.
    _3='3' # CT-e.
    _9='9' # Outro.


class tpTipoNotaReferenciada(str, Enum):
    """tpTipoNotaReferenciada -- Tipo de nota fiscal referenciada.

    """
    _0='0' # NFS-e.
    _1='1' # NFTS.


class tpTipoRPS(str, Enum):
    """tpTipoRPS -- Tipo referente aos poss
    í
    veis tipos de RPS.

    """
    RPS='RPS' # Recibo Provisório de Serviços.
    RPSM='RPS-M' # Recibo Provisório de Serviços proveniente de Nota Fiscal Conjugada (Mista).
    RPSC='RPS-C' # Cupom.


#
# Start data representation classes
#
class RetornoConsulta(GeneratedsSuper):
    """RetornoConsulta -- Schema utilizado para RETORNO de pedidos de consulta de NFS-e/RPS, consultade NFS-e recebidas e consulta de lote.
    Este Schema XML
    é
    utilizado pelo Web Service para informar aos tomadores e/ou prestadores de servi
    ç
    os o resultado de pedidos de consulta de NFS-e/RPS, consultade NFS-e recebidas e consulta de lote.
    Cabecalho -- Cabe
    ç
    alho do retorno.
    Alerta -- Elemento que representa a ocorr
    ê
    ncia de eventos de alerta durante o processamento da mensagem XML.
    Erro -- Elemento que representa a ocorr
    ê
    ncia de eventos de erro durante o processamento da mensagem XML.
    NFe -- Elemento NFe - Cada item ser
    á
    um NFS-e.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Cabecalho', 'CabecalhoType', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'Cabecalho', 'type': 'CabecalhoType'}, None),
        MemberSpec_('Alerta', 'tpEvento', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Alerta', 'type': 'tpEvento'}, None),
        MemberSpec_('Erro', 'tpEvento', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Erro', 'type': 'tpEvento'}, None),
        MemberSpec_('NFe', 'tpNFe', 1, 1, {'maxOccurs': '50', 'minOccurs': '0', 'name': 'NFe', 'type': 'tpNFe'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Cabecalho=None, Alerta=None, Erro=None, NFe=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Cabecalho = Cabecalho
        self.Cabecalho_nsprefix_ = None
        if Alerta is None:
            self.Alerta = []
        else:
            self.Alerta = Alerta
        self.Alerta_nsprefix_ = None
        if Erro is None:
            self.Erro = []
        else:
            self.Erro = Erro
        self.Erro_nsprefix_ = None
        if NFe is None:
            self.NFe = []
        else:
            self.NFe = NFe
        self.NFe_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RetornoConsulta)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RetornoConsulta.subclass:
            return RetornoConsulta.subclass(*args_, **kwargs_)
        else:
            return RetornoConsulta(*args_, **kwargs_)
    factory = staticmethod(factory)
    def has__content(self):
        if (
            self.Cabecalho is not None or
            self.Alerta or
            self.Erro or
            self.NFe
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RetornoConsulta', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RetornoConsulta')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RetornoConsulta':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RetornoConsulta')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RetornoConsulta', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RetornoConsulta'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RetornoConsulta', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Cabecalho is not None:
            namespaceprefix_ = self.Cabecalho_nsprefix_ + ':' if (UseCapturedNS_ and self.Cabecalho_nsprefix_) else ''
            self.Cabecalho.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Cabecalho', pretty_print=pretty_print)
        for Alerta_ in self.Alerta:
            namespaceprefix_ = self.Alerta_nsprefix_ + ':' if (UseCapturedNS_ and self.Alerta_nsprefix_) else ''
            Alerta_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Alerta', pretty_print=pretty_print)
        for Erro_ in self.Erro:
            namespaceprefix_ = self.Erro_nsprefix_ + ':' if (UseCapturedNS_ and self.Erro_nsprefix_) else ''
            Erro_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Erro', pretty_print=pretty_print)
        for NFe_ in self.NFe:
            namespaceprefix_ = self.NFe_nsprefix_ + ':' if (UseCapturedNS_ and self.NFe_nsprefix_) else ''
            NFe_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NFe', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Cabecalho':
            obj_ = CabecalhoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Cabecalho = obj_
            obj_.original_tagname_ = 'Cabecalho'
        elif nodeName_ == 'Alerta':
            obj_ = tpEvento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Alerta.append(obj_)
            obj_.original_tagname_ = 'Alerta'
        elif nodeName_ == 'Erro':
            obj_ = tpEvento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Erro.append(obj_)
            obj_.original_tagname_ = 'Erro'
        elif nodeName_ == 'NFe':
            obj_ = tpNFe.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NFe.append(obj_)
            obj_.original_tagname_ = 'NFe'
# end class RetornoConsulta


class tpEvento(GeneratedsSuper):
    """tpEvento -- Chave para identifica
    ç
    ã
    o da origem do evento.
    C
    Codigo -- C
    ó
    digo do evento.
    Descricao -- Descri
    ç
    ã
    o do evento.
    ChaveRPS -- Chave do RPS.
    ChaveNFe -- Chave da NFe.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Codigo', ['tpCodigoEvento', 'xs:short'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'Codigo', 'type': 'xs:short'}, None),
        MemberSpec_('Descricao', ['tpDescricaoEvento', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Descricao', 'type': 'xs:string'}, None),
        MemberSpec_('ChaveRPS', 'tpChaveRPS', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ChaveRPS', 'type': 'tpChaveRPS'}, 3),
        MemberSpec_('ChaveNFe', 'tpChaveNFe', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ChaveNFe', 'type': 'tpChaveNFe'}, 3),
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpEvento')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpEvento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpEvento'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEvento', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
    """tpCPFCNPJ -- Tipo que representa um CPF/CNPJ.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('CPF', ['tpCPF', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CPF', 'type': 'xs:string'}, 4),
        MemberSpec_('CNPJ', ['tpCNPJ', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CNPJ', 'type': 'xs:string'}, 4),
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
    validate_tpCNPJ_patterns_ = [['^([0-9A-Z]{12}[0-9]{2})$']]
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpCPFCNPJ')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpCPFCNPJ', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpCPFCNPJ'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpCPFCNPJ', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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


class tpCPFCNPJNIF(GeneratedsSuper):
    """tpCPFCNPJNIF -- Tipo que representa um CPF/CNPJ/NIF.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('CPF', ['tpCPF', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CPF', 'type': 'xs:string'}, None),
        MemberSpec_('CNPJ', ['tpCNPJ', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CNPJ', 'type': 'xs:string'}, None),
        MemberSpec_('NIF', ['tpNIF', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'NIF', 'type': 'xs:string'}, None),
        MemberSpec_('NaoNIF', ['tpNaoNIF', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'NaoNIF', 'type': 'xs:int'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, CPF=None, CNPJ=None, NIF=None, NaoNIF=None, gds_collector_=None, **kwargs_):
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
        self.NIF = NIF
        self.validate_tpNIF(self.NIF)
        self.NIF_nsprefix_ = None
        self.NaoNIF = NaoNIF
        self.validate_tpNaoNIF(self.NaoNIF)
        self.NaoNIF_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpCPFCNPJNIF)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpCPFCNPJNIF.subclass:
            return tpCPFCNPJNIF.subclass(*args_, **kwargs_)
        else:
            return tpCPFCNPJNIF(*args_, **kwargs_)
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
    validate_tpCNPJ_patterns_ = [['^([0-9A-Z]{12}[0-9]{2})$']]
    def validate_tpNIF(self, value):
        result = True
        # Validate type tpNIF, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpNIF' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpNIF' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpNaoNIF(self, value):
        result = True
        # Validate type tpNaoNIF, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [0, 1, 2]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpNaoNIF' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            self.CPF is not None or
            self.CNPJ is not None or
            self.NIF is not None or
            self.NaoNIF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpCPFCNPJNIF', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpCPFCNPJNIF')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpCPFCNPJNIF':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpCPFCNPJNIF')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpCPFCNPJNIF', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpCPFCNPJNIF'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpCPFCNPJNIF', fromsubclass_=False, pretty_print=True):
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
        if self.NIF is not None:
            namespaceprefix_ = self.NIF_nsprefix_ + ':' if (UseCapturedNS_ and self.NIF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNIF>%s</%sNIF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NIF), input_name='NIF')), namespaceprefix_ , eol_))
        if self.NaoNIF is not None:
            namespaceprefix_ = self.NaoNIF_nsprefix_ + ':' if (UseCapturedNS_ and self.NaoNIF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNaoNIF>%s</%sNaoNIF>%s' % (namespaceprefix_ , self.gds_format_integer(self.NaoNIF, input_name='NaoNIF'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
        elif nodeName_ == 'NIF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NIF')
            value_ = self.gds_validate_string(value_, node, 'NIF')
            self.NIF = value_
            self.NIF_nsprefix_ = child_.prefix
            # validate type tpNIF
            self.validate_tpNIF(self.NIF)
        elif nodeName_ == 'NaoNIF' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NaoNIF')
            ival_ = self.gds_validate_integer(ival_, node, 'NaoNIF')
            self.NaoNIF = ival_
            self.NaoNIF_nsprefix_ = child_.prefix
            # validate type tpNaoNIF
            self.validate_tpNaoNIF(self.NaoNIF)
# end class tpCPFCNPJNIF


class tpChaveNFeRPS(GeneratedsSuper):
    """tpChaveNFeRPS -- Tipo que representa a chave de uma NFS-e e a Chave do RPS que a mesma substitui.
    ChaveNFe -- Chave da NFS-e gerada.
    ChaveRPS -- Chave do RPS substitu
    í
    do.

    """
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpChaveNFeRPS')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpChaveNFeRPS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpChaveNFeRPS'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpChaveNFeRPS', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
    """tpChaveNFe -- Chave de identifica
    ç
    ã
    o da NFS-e.
    InscricaoPrestador -- Inscri
    ç
    ã
    o municipal do prestador de servi
    ç
    os.
    NumeroNFe -- N
    ú
    mero da NFS-e.
    CodigoVerificacao -- C
    ó
    digo de verifica
    ç
    ã
    o da NFS-e.
    ChaveNotaNacional -- Chave da Nota Nacional.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('InscricaoPrestador', ['tpInscricaoMunicipal', 'xs:long'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'InscricaoPrestador', 'type': 'xs:long'}, None),
        MemberSpec_('NumeroNFe', ['tpNumero', 'xs:long'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'NumeroNFe', 'type': 'xs:long'}, None),
        MemberSpec_('CodigoVerificacao', ['tpCodigoVerificacao', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CodigoVerificacao', 'type': 'xs:string'}, None),
        MemberSpec_('ChaveNotaNacional', ['tpChaveNotaNacional', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ChaveNotaNacional', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, InscricaoPrestador=None, NumeroNFe=None, CodigoVerificacao=None, ChaveNotaNacional=None, gds_collector_=None, **kwargs_):
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
        self.ChaveNotaNacional = ChaveNotaNacional
        self.validate_tpChaveNotaNacional(self.ChaveNotaNacional)
        self.ChaveNotaNacional_nsprefix_ = None
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
    validate_tpInscricaoMunicipal_patterns_ = [['^([0-9]{1,12})$']]
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
    def validate_tpChaveNotaNacional(self, value):
        result = True
        # Validate type tpChaveNotaNacional, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpChaveNotaNacional_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpChaveNotaNacional_patterns_, ))
                result = False
        return result
    validate_tpChaveNotaNacional_patterns_ = [['^([0-9A-Z]{50})$']]
    def has__content(self):
        if (
            self.InscricaoPrestador is not None or
            self.NumeroNFe is not None or
            self.CodigoVerificacao is not None or
            self.ChaveNotaNacional is not None
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpChaveNFe')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpChaveNFe', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpChaveNFe'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpChaveNFe', fromsubclass_=False, pretty_print=True):
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
        if self.ChaveNotaNacional is not None:
            namespaceprefix_ = self.ChaveNotaNacional_nsprefix_ + ':' if (UseCapturedNS_ and self.ChaveNotaNacional_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sChaveNotaNacional>%s</%sChaveNotaNacional>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.ChaveNotaNacional), input_name='ChaveNotaNacional')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
        elif nodeName_ == 'ChaveNotaNacional':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ChaveNotaNacional')
            value_ = self.gds_validate_string(value_, node, 'ChaveNotaNacional')
            self.ChaveNotaNacional = value_
            self.ChaveNotaNacional_nsprefix_ = child_.prefix
            # validate type tpChaveNotaNacional
            self.validate_tpChaveNotaNacional(self.ChaveNotaNacional)
# end class tpChaveNFe


class tpChaveRPS(GeneratedsSuper):
    """tpChaveRPS -- Tipo que define a chave identificadora de um RPS.
    InscricaoPrestador -- Inscri
    ç
    ã
    o municipal do prestador de servi
    ç
    os.
    SerieRPS -- S
    é
    rie do RPS.
    NumeroRPS -- N
    ú
    mero do RPS.

    """
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
    validate_tpInscricaoMunicipal_patterns_ = [['^([0-9]{1,12})$']]
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpChaveRPS')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpChaveRPS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpChaveRPS'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpChaveRPS', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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


class tpEnderecoExterior(GeneratedsSuper):
    """tpEnderecoExterior -- Tipo endere
    ç
    o no exterior.
    cPais -- C
    ó
    digo do pa
    í
    s (Tabela de Pa
    í
    ses ISO).
    cEndPost -- C
    ó
    digo alfanum
    é
    rico do Endere
    ç
    amento Postal no exterior do prestador do servi
    ç
    o.
    xCidade -- Nome da cidade no exterior do prestador do servi
    ç
    o.
    xEstProvReg -- Estado, prov
    í
    ncia ou regi
    ã
    o da cidade no exterior do prestador do servi
    ç
    o.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('cPais', ['tpCodigoPaisISO', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'cPais', 'type': 'xs:string'}, None),
        MemberSpec_('cEndPost', ['tpCodigoEndPostal', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'cEndPost', 'type': 'xs:string'}, None),
        MemberSpec_('xCidade', ['tpNomeCidade', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'xCidade', 'type': 'xs:string'}, None),
        MemberSpec_('xEstProvReg', ['tpEstadoProvinciaRegiao', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'xEstProvReg', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, cPais=None, cEndPost=None, xCidade=None, xEstProvReg=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.cPais = cPais
        self.validate_tpCodigoPaisISO(self.cPais)
        self.cPais_nsprefix_ = None
        self.cEndPost = cEndPost
        self.validate_tpCodigoEndPostal(self.cEndPost)
        self.cEndPost_nsprefix_ = None
        self.xCidade = xCidade
        self.validate_tpNomeCidade(self.xCidade)
        self.xCidade_nsprefix_ = None
        self.xEstProvReg = xEstProvReg
        self.validate_tpEstadoProvinciaRegiao(self.xEstProvReg)
        self.xEstProvReg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpEnderecoExterior)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpEnderecoExterior.subclass:
            return tpEnderecoExterior.subclass(*args_, **kwargs_)
        else:
            return tpEnderecoExterior(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpCodigoPaisISO(self, value):
        result = True
        # Validate type tpCodigoPaisISO, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCodigoPaisISO_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCodigoPaisISO_patterns_, ))
                result = False
        return result
    validate_tpCodigoPaisISO_patterns_ = [['^([A-Z]{2})$']]
    def validate_tpCodigoEndPostal(self, value):
        result = True
        # Validate type tpCodigoEndPostal, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpCodigoEndPostal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpCodigoEndPostal' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpNomeCidade(self, value):
        result = True
        # Validate type tpNomeCidade, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpNomeCidade' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpNomeCidade' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpEstadoProvinciaRegiao(self, value):
        result = True
        # Validate type tpEstadoProvinciaRegiao, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpEstadoProvinciaRegiao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpEstadoProvinciaRegiao' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            self.cPais is not None or
            self.cEndPost is not None or
            self.xCidade is not None or
            self.xEstProvReg is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEnderecoExterior', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpEnderecoExterior')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpEnderecoExterior':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpEnderecoExterior')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpEnderecoExterior', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpEnderecoExterior'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEnderecoExterior', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cPais is not None:
            namespaceprefix_ = self.cPais_nsprefix_ + ':' if (UseCapturedNS_ and self.cPais_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scPais>%s</%scPais>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cPais), input_name='cPais')), namespaceprefix_ , eol_))
        if self.cEndPost is not None:
            namespaceprefix_ = self.cEndPost_nsprefix_ + ':' if (UseCapturedNS_ and self.cEndPost_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scEndPost>%s</%scEndPost>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cEndPost), input_name='cEndPost')), namespaceprefix_ , eol_))
        if self.xCidade is not None:
            namespaceprefix_ = self.xCidade_nsprefix_ + ':' if (UseCapturedNS_ and self.xCidade_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxCidade>%s</%sxCidade>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xCidade), input_name='xCidade')), namespaceprefix_ , eol_))
        if self.xEstProvReg is not None:
            namespaceprefix_ = self.xEstProvReg_nsprefix_ + ':' if (UseCapturedNS_ and self.xEstProvReg_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxEstProvReg>%s</%sxEstProvReg>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xEstProvReg), input_name='xEstProvReg')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'cPais':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cPais')
            value_ = self.gds_validate_string(value_, node, 'cPais')
            self.cPais = value_
            self.cPais_nsprefix_ = child_.prefix
            # validate type tpCodigoPaisISO
            self.validate_tpCodigoPaisISO(self.cPais)
        elif nodeName_ == 'cEndPost':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cEndPost')
            value_ = self.gds_validate_string(value_, node, 'cEndPost')
            self.cEndPost = value_
            self.cEndPost_nsprefix_ = child_.prefix
            # validate type tpCodigoEndPostal
            self.validate_tpCodigoEndPostal(self.cEndPost)
        elif nodeName_ == 'xCidade':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xCidade')
            value_ = self.gds_validate_string(value_, node, 'xCidade')
            self.xCidade = value_
            self.xCidade_nsprefix_ = child_.prefix
            # validate type tpNomeCidade
            self.validate_tpNomeCidade(self.xCidade)
        elif nodeName_ == 'xEstProvReg':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xEstProvReg')
            value_ = self.gds_validate_string(value_, node, 'xEstProvReg')
            self.xEstProvReg = value_
            self.xEstProvReg_nsprefix_ = child_.prefix
            # validate type tpEstadoProvinciaRegiao
            self.validate_tpEstadoProvinciaRegiao(self.xEstProvReg)
# end class tpEnderecoExterior


class tpEnderecoNacional(GeneratedsSuper):
    """tpEnderecoNacional -- Tipo endere
    ç
    o no nacional.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('cMun', ['tpCidade', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'cMun', 'type': 'xs:int'}, None),
        MemberSpec_('CEP', ['tpCEP', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CEP', 'type': 'xs:int'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, cMun=None, CEP=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.cMun = cMun
        self.validate_tpCidade(self.cMun)
        self.cMun_nsprefix_ = None
        self.CEP = CEP
        self.validate_tpCEP(self.CEP)
        self.CEP_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpEnderecoNacional)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpEnderecoNacional.subclass:
            return tpEnderecoNacional.subclass(*args_, **kwargs_)
        else:
            return tpEnderecoNacional(*args_, **kwargs_)
    factory = staticmethod(factory)
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
    def has__content(self):
        if (
            self.cMun is not None or
            self.CEP is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEnderecoNacional', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpEnderecoNacional')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpEnderecoNacional':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpEnderecoNacional')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpEnderecoNacional', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpEnderecoNacional'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEnderecoNacional', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cMun is not None:
            namespaceprefix_ = self.cMun_nsprefix_ + ':' if (UseCapturedNS_ and self.cMun_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scMun>%s</%scMun>%s' % (namespaceprefix_ , self.gds_format_integer(self.cMun, input_name='cMun'), namespaceprefix_ , eol_))
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'cMun' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'cMun')
            ival_ = self.gds_validate_integer(ival_, node, 'cMun')
            self.cMun = ival_
            self.cMun_nsprefix_ = child_.prefix
            # validate type tpCidade
            self.validate_tpCidade(self.cMun)
        elif nodeName_ == 'CEP' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CEP')
            ival_ = self.gds_validate_integer(ival_, node, 'CEP')
            self.CEP = ival_
            self.CEP_nsprefix_ = child_.prefix
            # validate type tpCEP
            self.validate_tpCEP(self.CEP)
# end class tpEnderecoNacional


class tpEndereco(GeneratedsSuper):
    """tpEndereco -- Tipo Endere
    ç
    o.

    """
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
        MemberSpec_('EnderecoExterior', 'tpEnderecoExterior', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'EnderecoExterior', 'type': 'tpEnderecoExterior'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, TipoLogradouro=None, Logradouro=None, NumeroEndereco=None, ComplementoEndereco=None, Bairro=None, Cidade=None, UF=None, CEP=None, EnderecoExterior=None, gds_collector_=None, **kwargs_):
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
        self.EnderecoExterior = EnderecoExterior
        self.EnderecoExterior_nsprefix_ = None
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
    def has__content(self):
        if (
            self.TipoLogradouro is not None or
            self.Logradouro is not None or
            self.NumeroEndereco is not None or
            self.ComplementoEndereco is not None or
            self.Bairro is not None or
            self.Cidade is not None or
            self.UF is not None or
            self.CEP is not None or
            self.EnderecoExterior is not None
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpEndereco')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpEndereco', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpEndereco'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEndereco', fromsubclass_=False, pretty_print=True):
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
        if self.EnderecoExterior is not None:
            namespaceprefix_ = self.EnderecoExterior_nsprefix_ + ':' if (UseCapturedNS_ and self.EnderecoExterior_nsprefix_) else ''
            self.EnderecoExterior.export(outfile, level, namespaceprefix_, namespacedef_='', name_='EnderecoExterior', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
        elif nodeName_ == 'EnderecoExterior':
            obj_ = tpEnderecoExterior.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.EnderecoExterior = obj_
            obj_.original_tagname_ = 'EnderecoExterior'
# end class tpEndereco


class tpEnderecoIBSCBS(GeneratedsSuper):
    """tpEnderecoIBSCBS -- Tipo Endere
    ç
    o para o IBSCBS.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('endNac', 'tpEnderecoNacional', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'endNac', 'type': 'tpEnderecoNacional'}, 5),
        MemberSpec_('endExt', 'tpEnderecoExterior', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'endExt', 'type': 'tpEnderecoExterior'}, 5),
        MemberSpec_('xLgr', ['tpLogradouro', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'xLgr', 'type': 'xs:string'}, None),
        MemberSpec_('nro', ['tpNumeroEndereco', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'nro', 'type': 'xs:string'}, None),
        MemberSpec_('xCpl', ['tpComplementoEndereco', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'xCpl', 'type': 'xs:string'}, None),
        MemberSpec_('xBairro', ['tpBairro', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'xBairro', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, endNac=None, endExt=None, xLgr=None, nro=None, xCpl=None, xBairro=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.endNac = endNac
        self.endNac_nsprefix_ = None
        self.endExt = endExt
        self.endExt_nsprefix_ = None
        self.xLgr = xLgr
        self.validate_tpLogradouro(self.xLgr)
        self.xLgr_nsprefix_ = None
        self.nro = nro
        self.validate_tpNumeroEndereco(self.nro)
        self.nro_nsprefix_ = None
        self.xCpl = xCpl
        self.validate_tpComplementoEndereco(self.xCpl)
        self.xCpl_nsprefix_ = None
        self.xBairro = xBairro
        self.validate_tpBairro(self.xBairro)
        self.xBairro_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpEnderecoIBSCBS)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpEnderecoIBSCBS.subclass:
            return tpEnderecoIBSCBS.subclass(*args_, **kwargs_)
        else:
            return tpEnderecoIBSCBS(*args_, **kwargs_)
    factory = staticmethod(factory)
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
    def has__content(self):
        if (
            self.endNac is not None or
            self.endExt is not None or
            self.xLgr is not None or
            self.nro is not None or
            self.xCpl is not None or
            self.xBairro is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEnderecoIBSCBS', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpEnderecoIBSCBS')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpEnderecoIBSCBS':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpEnderecoIBSCBS')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpEnderecoIBSCBS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpEnderecoIBSCBS'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEnderecoIBSCBS', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.endNac is not None:
            namespaceprefix_ = self.endNac_nsprefix_ + ':' if (UseCapturedNS_ and self.endNac_nsprefix_) else ''
            self.endNac.export(outfile, level, namespaceprefix_, namespacedef_='', name_='endNac', pretty_print=pretty_print)
        if self.endExt is not None:
            namespaceprefix_ = self.endExt_nsprefix_ + ':' if (UseCapturedNS_ and self.endExt_nsprefix_) else ''
            self.endExt.export(outfile, level, namespaceprefix_, namespacedef_='', name_='endExt', pretty_print=pretty_print)
        if self.xLgr is not None:
            namespaceprefix_ = self.xLgr_nsprefix_ + ':' if (UseCapturedNS_ and self.xLgr_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxLgr>%s</%sxLgr>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xLgr), input_name='xLgr')), namespaceprefix_ , eol_))
        if self.nro is not None:
            namespaceprefix_ = self.nro_nsprefix_ + ':' if (UseCapturedNS_ and self.nro_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snro>%s</%snro>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.nro), input_name='nro')), namespaceprefix_ , eol_))
        if self.xCpl is not None:
            namespaceprefix_ = self.xCpl_nsprefix_ + ':' if (UseCapturedNS_ and self.xCpl_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxCpl>%s</%sxCpl>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xCpl), input_name='xCpl')), namespaceprefix_ , eol_))
        if self.xBairro is not None:
            namespaceprefix_ = self.xBairro_nsprefix_ + ':' if (UseCapturedNS_ and self.xBairro_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxBairro>%s</%sxBairro>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xBairro), input_name='xBairro')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'endNac':
            obj_ = tpEnderecoNacional.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.endNac = obj_
            obj_.original_tagname_ = 'endNac'
        elif nodeName_ == 'endExt':
            obj_ = tpEnderecoExterior.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.endExt = obj_
            obj_.original_tagname_ = 'endExt'
        elif nodeName_ == 'xLgr':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xLgr')
            value_ = self.gds_validate_string(value_, node, 'xLgr')
            self.xLgr = value_
            self.xLgr_nsprefix_ = child_.prefix
            # validate type tpLogradouro
            self.validate_tpLogradouro(self.xLgr)
        elif nodeName_ == 'nro':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nro')
            value_ = self.gds_validate_string(value_, node, 'nro')
            self.nro = value_
            self.nro_nsprefix_ = child_.prefix
            # validate type tpNumeroEndereco
            self.validate_tpNumeroEndereco(self.nro)
        elif nodeName_ == 'xCpl':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xCpl')
            value_ = self.gds_validate_string(value_, node, 'xCpl')
            self.xCpl = value_
            self.xCpl_nsprefix_ = child_.prefix
            # validate type tpComplementoEndereco
            self.validate_tpComplementoEndereco(self.xCpl)
        elif nodeName_ == 'xBairro':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xBairro')
            value_ = self.gds_validate_string(value_, node, 'xBairro')
            self.xBairro = value_
            self.xBairro_nsprefix_ = child_.prefix
            # validate type tpBairro
            self.validate_tpBairro(self.xBairro)
# end class tpEnderecoIBSCBS


class tpEnderecoSimplesIBSCBS(GeneratedsSuper):
    """tpEnderecoSimplesIBSCBS -- Tipo Endere
    ç
    o simplificado para o IBSCBS.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('CEP', ['tpCEP', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CEP', 'type': 'xs:int'}, 6),
        MemberSpec_('endExt', 'tpEnderecoExterior', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'endExt', 'type': 'tpEnderecoExterior'}, 6),
        MemberSpec_('xLgr', ['tpLogradouro', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'xLgr', 'type': 'xs:string'}, None),
        MemberSpec_('nro', ['tpNumeroEndereco', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'nro', 'type': 'xs:string'}, None),
        MemberSpec_('xCpl', ['tpComplementoEndereco', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'xCpl', 'type': 'xs:string'}, None),
        MemberSpec_('xBairro', ['tpBairro', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'xBairro', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, CEP=None, endExt=None, xLgr=None, nro=None, xCpl=None, xBairro=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.CEP = CEP
        self.validate_tpCEP(self.CEP)
        self.CEP_nsprefix_ = None
        self.endExt = endExt
        self.endExt_nsprefix_ = None
        self.xLgr = xLgr
        self.validate_tpLogradouro(self.xLgr)
        self.xLgr_nsprefix_ = None
        self.nro = nro
        self.validate_tpNumeroEndereco(self.nro)
        self.nro_nsprefix_ = None
        self.xCpl = xCpl
        self.validate_tpComplementoEndereco(self.xCpl)
        self.xCpl_nsprefix_ = None
        self.xBairro = xBairro
        self.validate_tpBairro(self.xBairro)
        self.xBairro_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpEnderecoSimplesIBSCBS)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpEnderecoSimplesIBSCBS.subclass:
            return tpEnderecoSimplesIBSCBS.subclass(*args_, **kwargs_)
        else:
            return tpEnderecoSimplesIBSCBS(*args_, **kwargs_)
    factory = staticmethod(factory)
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
    def has__content(self):
        if (
            self.CEP is not None or
            self.endExt is not None or
            self.xLgr is not None or
            self.nro is not None or
            self.xCpl is not None or
            self.xBairro is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEnderecoSimplesIBSCBS', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpEnderecoSimplesIBSCBS')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpEnderecoSimplesIBSCBS':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpEnderecoSimplesIBSCBS')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpEnderecoSimplesIBSCBS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpEnderecoSimplesIBSCBS'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpEnderecoSimplesIBSCBS', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CEP is not None:
            namespaceprefix_ = self.CEP_nsprefix_ + ':' if (UseCapturedNS_ and self.CEP_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCEP>%s</%sCEP>%s' % (namespaceprefix_ , self.gds_format_integer(self.CEP, input_name='CEP'), namespaceprefix_ , eol_))
        if self.endExt is not None:
            namespaceprefix_ = self.endExt_nsprefix_ + ':' if (UseCapturedNS_ and self.endExt_nsprefix_) else ''
            self.endExt.export(outfile, level, namespaceprefix_, namespacedef_='', name_='endExt', pretty_print=pretty_print)
        if self.xLgr is not None:
            namespaceprefix_ = self.xLgr_nsprefix_ + ':' if (UseCapturedNS_ and self.xLgr_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxLgr>%s</%sxLgr>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xLgr), input_name='xLgr')), namespaceprefix_ , eol_))
        if self.nro is not None:
            namespaceprefix_ = self.nro_nsprefix_ + ':' if (UseCapturedNS_ and self.nro_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snro>%s</%snro>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.nro), input_name='nro')), namespaceprefix_ , eol_))
        if self.xCpl is not None:
            namespaceprefix_ = self.xCpl_nsprefix_ + ':' if (UseCapturedNS_ and self.xCpl_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxCpl>%s</%sxCpl>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xCpl), input_name='xCpl')), namespaceprefix_ , eol_))
        if self.xBairro is not None:
            namespaceprefix_ = self.xBairro_nsprefix_ + ':' if (UseCapturedNS_ and self.xBairro_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxBairro>%s</%sxBairro>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xBairro), input_name='xBairro')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CEP' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'CEP')
            ival_ = self.gds_validate_integer(ival_, node, 'CEP')
            self.CEP = ival_
            self.CEP_nsprefix_ = child_.prefix
            # validate type tpCEP
            self.validate_tpCEP(self.CEP)
        elif nodeName_ == 'endExt':
            obj_ = tpEnderecoExterior.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.endExt = obj_
            obj_.original_tagname_ = 'endExt'
        elif nodeName_ == 'xLgr':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xLgr')
            value_ = self.gds_validate_string(value_, node, 'xLgr')
            self.xLgr = value_
            self.xLgr_nsprefix_ = child_.prefix
            # validate type tpLogradouro
            self.validate_tpLogradouro(self.xLgr)
        elif nodeName_ == 'nro':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nro')
            value_ = self.gds_validate_string(value_, node, 'nro')
            self.nro = value_
            self.nro_nsprefix_ = child_.prefix
            # validate type tpNumeroEndereco
            self.validate_tpNumeroEndereco(self.nro)
        elif nodeName_ == 'xCpl':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xCpl')
            value_ = self.gds_validate_string(value_, node, 'xCpl')
            self.xCpl = value_
            self.xCpl_nsprefix_ = child_.prefix
            # validate type tpComplementoEndereco
            self.validate_tpComplementoEndereco(self.xCpl)
        elif nodeName_ == 'xBairro':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xBairro')
            value_ = self.gds_validate_string(value_, node, 'xBairro')
            self.xBairro = value_
            self.xBairro_nsprefix_ = child_.prefix
            # validate type tpBairro
            self.validate_tpBairro(self.xBairro)
# end class tpEnderecoSimplesIBSCBS


class tpInformacoesLote(GeneratedsSuper):
    """tpInformacoesLote -- Informa
    ç
    õ
    es do lote processado.
    NumeroLote -- N
    ú
    mero de lote.
    InscricaoPrestador -- Inscri
    ç
    ã
    o municipal do prestador dos RPS contidos no lote.
    CPFCNPJRemetente -- CNPJ do remetente autorizado a transmitir a mensagem XML.
    DataEnvioLote -- Data/hora de envio do lote.
    QtdNotasProcessadas -- Quantidade de RPS do lote.
    TempoProcessamento -- Tempo de processamento do lote.
    ValorTotalServicos -- Valor total dos servi
    ç
    os dos RPS contidos na mensagem XML.
    ValorTotalDeducoes -- Valor total das dedu
    ç
    õ
    es dos RPS contidos na mensagem XML.

    """
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
    validate_tpInscricaoMunicipal_patterns_ = [['^([0-9]{1,12})$']]
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpInformacoesLote')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpInformacoesLote', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpInformacoesLote'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpInformacoesLote', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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


class tpInformacoesPessoa(GeneratedsSuper):
    """tpInformacoesPessoa -- Tipo de informa
    ç
    õ
    es de pessoa.
    xNome -- Nome.
    end -- Endere
    ç
    o.
    email -- Endere
    ç
    o eletr
    ô
    nico.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('CPF', ['tpCPF', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CPF', 'type': 'xs:string'}, None),
        MemberSpec_('CNPJ', ['tpCNPJ', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CNPJ', 'type': 'xs:string'}, None),
        MemberSpec_('NIF', ['tpNIF', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'NIF', 'type': 'xs:string'}, None),
        MemberSpec_('NaoNIF', ['tpNaoNIF', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'NaoNIF', 'type': 'xs:int'}, None),
        MemberSpec_('xNome', ['tpRazaoSocialObrigatorio', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'xNome', 'type': 'xs:string'}, None),
        MemberSpec_('end', 'tpEnderecoIBSCBS', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'end', 'type': 'tpEnderecoIBSCBS'}, None),
        MemberSpec_('email', ['tpEmail', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'email', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, CPF=None, CNPJ=None, NIF=None, NaoNIF=None, xNome=None, end=None, email=None, gds_collector_=None, **kwargs_):
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
        self.NIF = NIF
        self.validate_tpNIF(self.NIF)
        self.NIF_nsprefix_ = None
        self.NaoNIF = NaoNIF
        self.validate_tpNaoNIF(self.NaoNIF)
        self.NaoNIF_nsprefix_ = None
        self.xNome = xNome
        self.validate_tpRazaoSocialObrigatorio(self.xNome)
        self.xNome_nsprefix_ = None
        self.end = end
        self.end_nsprefix_ = None
        self.email = email
        self.validate_tpEmail(self.email)
        self.email_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpInformacoesPessoa)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpInformacoesPessoa.subclass:
            return tpInformacoesPessoa.subclass(*args_, **kwargs_)
        else:
            return tpInformacoesPessoa(*args_, **kwargs_)
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
    validate_tpCNPJ_patterns_ = [['^([0-9A-Z]{12}[0-9]{2})$']]
    def validate_tpNIF(self, value):
        result = True
        # Validate type tpNIF, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpNIF' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpNIF' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpNaoNIF(self, value):
        result = True
        # Validate type tpNaoNIF, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [0, 1, 2]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpNaoNIF' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpRazaoSocialObrigatorio(self, value):
        result = True
        # Validate type tpRazaoSocialObrigatorio, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 75:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpRazaoSocialObrigatorio' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpRazaoSocialObrigatorio' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
    def has__content(self):
        if (
            self.CPF is not None or
            self.CNPJ is not None or
            self.NIF is not None or
            self.NaoNIF is not None or
            self.xNome is not None or
            self.end is not None or
            self.email is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpInformacoesPessoa', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpInformacoesPessoa')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpInformacoesPessoa':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpInformacoesPessoa')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpInformacoesPessoa', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpInformacoesPessoa'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpInformacoesPessoa', fromsubclass_=False, pretty_print=True):
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
        if self.NIF is not None:
            namespaceprefix_ = self.NIF_nsprefix_ + ':' if (UseCapturedNS_ and self.NIF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNIF>%s</%sNIF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NIF), input_name='NIF')), namespaceprefix_ , eol_))
        if self.NaoNIF is not None:
            namespaceprefix_ = self.NaoNIF_nsprefix_ + ':' if (UseCapturedNS_ and self.NaoNIF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNaoNIF>%s</%sNaoNIF>%s' % (namespaceprefix_ , self.gds_format_integer(self.NaoNIF, input_name='NaoNIF'), namespaceprefix_ , eol_))
        if self.xNome is not None:
            namespaceprefix_ = self.xNome_nsprefix_ + ':' if (UseCapturedNS_ and self.xNome_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxNome>%s</%sxNome>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xNome), input_name='xNome')), namespaceprefix_ , eol_))
        if self.end is not None:
            namespaceprefix_ = self.end_nsprefix_ + ':' if (UseCapturedNS_ and self.end_nsprefix_) else ''
            self.end.export(outfile, level, namespaceprefix_, namespacedef_='', name_='end', pretty_print=pretty_print)
        if self.email is not None:
            namespaceprefix_ = self.email_nsprefix_ + ':' if (UseCapturedNS_ and self.email_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%semail>%s</%semail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.email), input_name='email')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
        elif nodeName_ == 'NIF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NIF')
            value_ = self.gds_validate_string(value_, node, 'NIF')
            self.NIF = value_
            self.NIF_nsprefix_ = child_.prefix
            # validate type tpNIF
            self.validate_tpNIF(self.NIF)
        elif nodeName_ == 'NaoNIF' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NaoNIF')
            ival_ = self.gds_validate_integer(ival_, node, 'NaoNIF')
            self.NaoNIF = ival_
            self.NaoNIF_nsprefix_ = child_.prefix
            # validate type tpNaoNIF
            self.validate_tpNaoNIF(self.NaoNIF)
        elif nodeName_ == 'xNome':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xNome')
            value_ = self.gds_validate_string(value_, node, 'xNome')
            self.xNome = value_
            self.xNome_nsprefix_ = child_.prefix
            # validate type tpRazaoSocialObrigatorio
            self.validate_tpRazaoSocialObrigatorio(self.xNome)
        elif nodeName_ == 'end':
            obj_ = tpEnderecoIBSCBS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.end = obj_
            obj_.original_tagname_ = 'end'
        elif nodeName_ == 'email':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'email')
            value_ = self.gds_validate_string(value_, node, 'email')
            self.email = value_
            self.email_nsprefix_ = child_.prefix
            # validate type tpEmail
            self.validate_tpEmail(self.email)
# end class tpInformacoesPessoa


class tpGRefNFSe(GeneratedsSuper):
    """tpGRefNFSe -- Grupo com Ids da nota nacional referenciadas, associadas a NFSE.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('refNFSe', ['tpChaveNotaNacional', 'xs:string'], 1, 0, {'maxOccurs': '99', 'minOccurs': '1', 'name': 'refNFSe', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, refNFSe=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if refNFSe is None:
            self.refNFSe = []
        else:
            self.refNFSe = refNFSe
        self.refNFSe_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpGRefNFSe)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpGRefNFSe.subclass:
            return tpGRefNFSe.subclass(*args_, **kwargs_)
        else:
            return tpGRefNFSe(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpChaveNotaNacional(self, value):
        result = True
        # Validate type tpChaveNotaNacional, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpChaveNotaNacional_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpChaveNotaNacional_patterns_, ))
                result = False
        return result
    validate_tpChaveNotaNacional_patterns_ = [['^([0-9A-Z]{50})$']]
    def has__content(self):
        if (
            self.refNFSe
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpGRefNFSe', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpGRefNFSe')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpGRefNFSe':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpGRefNFSe')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpGRefNFSe', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpGRefNFSe'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpGRefNFSe', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for refNFSe_ in self.refNFSe:
            namespaceprefix_ = self.refNFSe_nsprefix_ + ':' if (UseCapturedNS_ and self.refNFSe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srefNFSe>%s</%srefNFSe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(refNFSe_), input_name='refNFSe')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'refNFSe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'refNFSe')
            value_ = self.gds_validate_string(value_, node, 'refNFSe')
            self.refNFSe.append(value_)
            self.refNFSe_nsprefix_ = child_.prefix
            # validate type tpChaveNotaNacional
            self.validate_tpChaveNotaNacional(self.refNFSe[-1])
# end class tpGRefNFSe


class tpGrupoReeRepRes(GeneratedsSuper):
    """tpGrupoReeRepRes -- Grupo de informa
    ç
    õ
    es relativas a valores inclu
    í
    dos neste documento e recebidos por
    motivo de estarem relacionadas a opera
    ç
    õ
    es de terceiros, objeto de reembolso, repasse ou
    ressarcimento pelo recebedor, j
    á
    tributados e aqui referenciados.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('documentos', 'tpDocumento', 1, 0, {'maxOccurs': '100', 'minOccurs': '1', 'name': 'documentos', 'type': 'tpDocumento'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, documentos=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if documentos is None:
            self.documentos = []
        else:
            self.documentos = documentos
        self.documentos_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpGrupoReeRepRes)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpGrupoReeRepRes.subclass:
            return tpGrupoReeRepRes.subclass(*args_, **kwargs_)
        else:
            return tpGrupoReeRepRes(*args_, **kwargs_)
    factory = staticmethod(factory)
    def has__content(self):
        if (
            self.documentos
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpGrupoReeRepRes', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpGrupoReeRepRes')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpGrupoReeRepRes':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpGrupoReeRepRes')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpGrupoReeRepRes', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpGrupoReeRepRes'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpGrupoReeRepRes', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for documentos_ in self.documentos:
            namespaceprefix_ = self.documentos_nsprefix_ + ':' if (UseCapturedNS_ and self.documentos_nsprefix_) else ''
            documentos_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='documentos', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'documentos':
            obj_ = tpDocumento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.documentos.append(obj_)
            obj_.original_tagname_ = 'documentos'
# end class tpGrupoReeRepRes


class tpImovelObra(GeneratedsSuper):
    """tpImovelObra -- Tipo de imovel/obra.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('inscImobFisc', ['tpInscImobFisc', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'inscImobFisc', 'type': 'xs:string'}, None),
        MemberSpec_('cCIB', ['tpCCIB', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'cCIB', 'type': 'xs:string'}, 7),
        MemberSpec_('cObra', ['tpCObra', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'cObra', 'type': 'xs:string'}, 7),
        MemberSpec_('end', 'tpEnderecoSimplesIBSCBS', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'end', 'type': 'tpEnderecoSimplesIBSCBS'}, 7),
    ]
    subclass = None
    superclass = None
    def __init__(self, inscImobFisc=None, cCIB=None, cObra=None, end=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.inscImobFisc = inscImobFisc
        self.validate_tpInscImobFisc(self.inscImobFisc)
        self.inscImobFisc_nsprefix_ = None
        self.cCIB = cCIB
        self.validate_tpCCIB(self.cCIB)
        self.cCIB_nsprefix_ = None
        self.cObra = cObra
        self.validate_tpCObra(self.cObra)
        self.cObra_nsprefix_ = None
        self.end = end
        self.end_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpImovelObra)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpImovelObra.subclass:
            return tpImovelObra.subclass(*args_, **kwargs_)
        else:
            return tpImovelObra(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpInscImobFisc(self, value):
        result = True
        # Validate type tpInscImobFisc, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpInscImobFisc' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpInscImobFisc' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpCCIB(self, value):
        result = True
        # Validate type tpCCIB, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCCIB_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCCIB_patterns_, ))
                result = False
        return result
    validate_tpCCIB_patterns_ = [['^([0-9A-Z]{8})$']]
    def validate_tpCObra(self, value):
        result = True
        # Validate type tpCObra, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpCObra' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpCObra' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            self.inscImobFisc is not None or
            self.cCIB is not None or
            self.cObra is not None or
            self.end is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpImovelObra', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpImovelObra')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpImovelObra':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpImovelObra')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpImovelObra', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpImovelObra'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpImovelObra', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.inscImobFisc is not None:
            namespaceprefix_ = self.inscImobFisc_nsprefix_ + ':' if (UseCapturedNS_ and self.inscImobFisc_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sinscImobFisc>%s</%sinscImobFisc>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.inscImobFisc), input_name='inscImobFisc')), namespaceprefix_ , eol_))
        if self.cCIB is not None:
            namespaceprefix_ = self.cCIB_nsprefix_ + ':' if (UseCapturedNS_ and self.cCIB_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scCIB>%s</%scCIB>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cCIB), input_name='cCIB')), namespaceprefix_ , eol_))
        if self.cObra is not None:
            namespaceprefix_ = self.cObra_nsprefix_ + ':' if (UseCapturedNS_ and self.cObra_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scObra>%s</%scObra>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cObra), input_name='cObra')), namespaceprefix_ , eol_))
        if self.end is not None:
            namespaceprefix_ = self.end_nsprefix_ + ':' if (UseCapturedNS_ and self.end_nsprefix_) else ''
            self.end.export(outfile, level, namespaceprefix_, namespacedef_='', name_='end', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'inscImobFisc':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'inscImobFisc')
            value_ = self.gds_validate_string(value_, node, 'inscImobFisc')
            self.inscImobFisc = value_
            self.inscImobFisc_nsprefix_ = child_.prefix
            # validate type tpInscImobFisc
            self.validate_tpInscImobFisc(self.inscImobFisc)
        elif nodeName_ == 'cCIB':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cCIB')
            value_ = self.gds_validate_string(value_, node, 'cCIB')
            self.cCIB = value_
            self.cCIB_nsprefix_ = child_.prefix
            # validate type tpCCIB
            self.validate_tpCCIB(self.cCIB)
        elif nodeName_ == 'cObra':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cObra')
            value_ = self.gds_validate_string(value_, node, 'cObra')
            self.cObra = value_
            self.cObra_nsprefix_ = child_.prefix
            # validate type tpCObra
            self.validate_tpCObra(self.cObra)
        elif nodeName_ == 'end':
            obj_ = tpEnderecoSimplesIBSCBS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.end = obj_
            obj_.original_tagname_ = 'end'
# end class tpImovelObra


class tpDocumento(GeneratedsSuper):
    """tpDocumento -- Tipo de documento referenciado nos casos de reembolso, repasse e ressarcimento que ser
    ã
    o considerados na base de c
    á
    lculo do ISSQN, do IBS e da CBS.
    dtEmiDoc -- Data da emiss
    ã
    o do documento dedut
    í
    vel. Ano, m
    ê
    s e dia (AAAA-MM-DD).
    dtCompDoc -- Data da compet
    ê
    ncia do documento dedut
    í
    vel. Ano, m
    ê
    s e dia (AAAA-MM-DD).
    tpReeRepRes -- Tipo de valor inclu
    í
    do neste documento, recebido por motivo de estarem relacionadas a opera
    ç
    õ
    es de
    terceiros, objeto de reembolso, repasse ou ressarcimento pelo recebedor, j
    á
    tributados e aqui referenciado.
    xTpReeRepRes -- Descri
    ç
    ã
    o do reembolso ou ressarcimento quando a op
    ç
    ã
    o
    é
    "99 - Outros reembolsos ou ressarcimentos recebidos por valores pagos relativos a opera
    ç
    õ
    es por conta e ordem de terceiro"
    vlrReeRepRes -- Valor monet
    á
    rio (total ou parcial, conforme documento informado) utilizado para n
    ã
    o inclus
    ã
    o na base de c
    á
    lculo do ISS e do IBS e da CBS da NFS-e que est
    á
    sendo emitida (R$).

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('dFeNacional', 'tpDFeNacional', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'dFeNacional', 'type': 'tpDFeNacional'}, 8),
        MemberSpec_('docFiscalOutro', 'tpDocFiscalOutro', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'docFiscalOutro', 'type': 'tpDocFiscalOutro'}, 8),
        MemberSpec_('docOutro', 'tpDocOutro', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'docOutro', 'type': 'tpDocOutro'}, 8),
        MemberSpec_('fornec', 'tpFornecedor', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'fornec', 'type': 'tpFornecedor'}, None),
        MemberSpec_('dtEmiDoc', 'xs:date', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'dtEmiDoc', 'type': 'xs:date'}, None),
        MemberSpec_('dtCompDoc', 'xs:date', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'dtCompDoc', 'type': 'xs:date'}, None),
        MemberSpec_('tpReeRepRes', ['tpReeRepRes', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'tpReeRepRes', 'type': 'xs:int'}, None),
        MemberSpec_('xTpReeRepRes', ['tpXTpReeRepRes', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'xTpReeRepRes', 'type': 'xs:string'}, None),
        MemberSpec_('vlrReeRepRes', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'vlrReeRepRes', 'type': 'xs:decimal'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, dFeNacional=None, docFiscalOutro=None, docOutro=None, fornec=None, dtEmiDoc=None, dtCompDoc=None, tpReeRepRes=None, xTpReeRepRes=None, vlrReeRepRes=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.dFeNacional = dFeNacional
        self.dFeNacional_nsprefix_ = None
        self.docFiscalOutro = docFiscalOutro
        self.docFiscalOutro_nsprefix_ = None
        self.docOutro = docOutro
        self.docOutro_nsprefix_ = None
        self.fornec = fornec
        self.fornec_nsprefix_ = None
        if isinstance(dtEmiDoc, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dtEmiDoc, '%Y-%m-%d').date()
        else:
            initvalue_ = dtEmiDoc
        self.dtEmiDoc = initvalue_
        self.dtEmiDoc_nsprefix_ = None
        if isinstance(dtCompDoc, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dtCompDoc, '%Y-%m-%d').date()
        else:
            initvalue_ = dtCompDoc
        self.dtCompDoc = initvalue_
        self.dtCompDoc_nsprefix_ = None
        self.tpReeRepRes = tpReeRepRes
        self.validate_tpReeRepRes(self.tpReeRepRes)
        self.tpReeRepRes_nsprefix_ = None
        self.xTpReeRepRes = xTpReeRepRes
        self.validate_tpXTpReeRepRes(self.xTpReeRepRes)
        self.xTpReeRepRes_nsprefix_ = None
        self.vlrReeRepRes = vlrReeRepRes
        self.validate_tpValor(self.vlrReeRepRes)
        self.vlrReeRepRes_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpDocumento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpDocumento.subclass:
            return tpDocumento.subclass(*args_, **kwargs_)
        else:
            return tpDocumento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpReeRepRes(self, value):
        result = True
        # Validate type tpReeRepRes, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [1, 2, 3, 4, 99]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpReeRepRes' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpXTpReeRepRes(self, value):
        result = True
        # Validate type tpXTpReeRepRes, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 150:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpXTpReeRepRes' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpXTpReeRepRes' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
    def has__content(self):
        if (
            self.dFeNacional is not None or
            self.docFiscalOutro is not None or
            self.docOutro is not None or
            self.fornec is not None or
            self.dtEmiDoc is not None or
            self.dtCompDoc is not None or
            self.tpReeRepRes is not None or
            self.xTpReeRepRes is not None or
            self.vlrReeRepRes is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpDocumento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpDocumento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpDocumento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpDocumento')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpDocumento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpDocumento'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpDocumento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.dFeNacional is not None:
            namespaceprefix_ = self.dFeNacional_nsprefix_ + ':' if (UseCapturedNS_ and self.dFeNacional_nsprefix_) else ''
            self.dFeNacional.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dFeNacional', pretty_print=pretty_print)
        if self.docFiscalOutro is not None:
            namespaceprefix_ = self.docFiscalOutro_nsprefix_ + ':' if (UseCapturedNS_ and self.docFiscalOutro_nsprefix_) else ''
            self.docFiscalOutro.export(outfile, level, namespaceprefix_, namespacedef_='', name_='docFiscalOutro', pretty_print=pretty_print)
        if self.docOutro is not None:
            namespaceprefix_ = self.docOutro_nsprefix_ + ':' if (UseCapturedNS_ and self.docOutro_nsprefix_) else ''
            self.docOutro.export(outfile, level, namespaceprefix_, namespacedef_='', name_='docOutro', pretty_print=pretty_print)
        if self.fornec is not None:
            namespaceprefix_ = self.fornec_nsprefix_ + ':' if (UseCapturedNS_ and self.fornec_nsprefix_) else ''
            self.fornec.export(outfile, level, namespaceprefix_, namespacedef_='', name_='fornec', pretty_print=pretty_print)
        if self.dtEmiDoc is not None:
            namespaceprefix_ = self.dtEmiDoc_nsprefix_ + ':' if (UseCapturedNS_ and self.dtEmiDoc_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdtEmiDoc>%s</%sdtEmiDoc>%s' % (namespaceprefix_ , self.gds_format_date(self.dtEmiDoc, input_name='dtEmiDoc'), namespaceprefix_ , eol_))
        if self.dtCompDoc is not None:
            namespaceprefix_ = self.dtCompDoc_nsprefix_ + ':' if (UseCapturedNS_ and self.dtCompDoc_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdtCompDoc>%s</%sdtCompDoc>%s' % (namespaceprefix_ , self.gds_format_date(self.dtCompDoc, input_name='dtCompDoc'), namespaceprefix_ , eol_))
        if self.tpReeRepRes is not None:
            namespaceprefix_ = self.tpReeRepRes_nsprefix_ + ':' if (UseCapturedNS_ and self.tpReeRepRes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpReeRepRes>%s</%stpReeRepRes>%s' % (namespaceprefix_ , self.gds_format_integer(self.tpReeRepRes, input_name='tpReeRepRes'), namespaceprefix_ , eol_))
        if self.xTpReeRepRes is not None:
            namespaceprefix_ = self.xTpReeRepRes_nsprefix_ + ':' if (UseCapturedNS_ and self.xTpReeRepRes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxTpReeRepRes>%s</%sxTpReeRepRes>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xTpReeRepRes), input_name='xTpReeRepRes')), namespaceprefix_ , eol_))
        if self.vlrReeRepRes is not None:
            namespaceprefix_ = self.vlrReeRepRes_nsprefix_ + ':' if (UseCapturedNS_ and self.vlrReeRepRes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svlrReeRepRes>%s</%svlrReeRepRes>%s' % (namespaceprefix_ , self.gds_format_decimal(self.vlrReeRepRes, input_name='vlrReeRepRes'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'dFeNacional':
            obj_ = tpDFeNacional.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dFeNacional = obj_
            obj_.original_tagname_ = 'dFeNacional'
        elif nodeName_ == 'docFiscalOutro':
            obj_ = tpDocFiscalOutro.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.docFiscalOutro = obj_
            obj_.original_tagname_ = 'docFiscalOutro'
        elif nodeName_ == 'docOutro':
            obj_ = tpDocOutro.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.docOutro = obj_
            obj_.original_tagname_ = 'docOutro'
        elif nodeName_ == 'fornec':
            obj_ = tpFornecedor.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.fornec = obj_
            obj_.original_tagname_ = 'fornec'
        elif nodeName_ == 'dtEmiDoc':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.dtEmiDoc = dval_
            self.dtEmiDoc_nsprefix_ = child_.prefix
        elif nodeName_ == 'dtCompDoc':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.dtCompDoc = dval_
            self.dtCompDoc_nsprefix_ = child_.prefix
        elif nodeName_ == 'tpReeRepRes' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'tpReeRepRes')
            ival_ = self.gds_validate_integer(ival_, node, 'tpReeRepRes')
            self.tpReeRepRes = ival_
            self.tpReeRepRes_nsprefix_ = child_.prefix
            # validate type tpReeRepRes
            self.validate_tpReeRepRes(self.tpReeRepRes)
        elif nodeName_ == 'xTpReeRepRes':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xTpReeRepRes')
            value_ = self.gds_validate_string(value_, node, 'xTpReeRepRes')
            self.xTpReeRepRes = value_
            self.xTpReeRepRes_nsprefix_ = child_.prefix
            # validate type tpXTpReeRepRes
            self.validate_tpXTpReeRepRes(self.xTpReeRepRes)
        elif nodeName_ == 'vlrReeRepRes' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'vlrReeRepRes')
            fval_ = self.gds_validate_decimal(fval_, node, 'vlrReeRepRes')
            self.vlrReeRepRes = fval_
            self.vlrReeRepRes_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.vlrReeRepRes)
# end class tpDocumento


class tpDFeNacional(GeneratedsSuper):
    """tpDFeNacional -- Tipo de documento do reposit
    ó
    rio nacional.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('tipoChaveDFe', ['tpTipoChaveDFE', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'tipoChaveDFe', 'type': 'xs:int'}, None),
        MemberSpec_('xTipoChaveDFe', ['tpXTipoChaveDFe', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'xTipoChaveDFe', 'type': 'xs:string'}, None),
        MemberSpec_('chaveDFe', ['tpChaveDFe', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'chaveDFe', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, tipoChaveDFe=None, xTipoChaveDFe=None, chaveDFe=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.tipoChaveDFe = tipoChaveDFe
        self.validate_tpTipoChaveDFE(self.tipoChaveDFe)
        self.tipoChaveDFe_nsprefix_ = None
        self.xTipoChaveDFe = xTipoChaveDFe
        self.validate_tpXTipoChaveDFe(self.xTipoChaveDFe)
        self.xTipoChaveDFe_nsprefix_ = None
        self.chaveDFe = chaveDFe
        self.validate_tpChaveDFe(self.chaveDFe)
        self.chaveDFe_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpDFeNacional)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpDFeNacional.subclass:
            return tpDFeNacional.subclass(*args_, **kwargs_)
        else:
            return tpDFeNacional(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpTipoChaveDFE(self, value):
        result = True
        # Validate type tpTipoChaveDFE, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [1, 2, 3, 9]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpTipoChaveDFE' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpXTipoChaveDFe(self, value):
        result = True
        # Validate type tpXTipoChaveDFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpXTipoChaveDFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpXTipoChaveDFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpChaveDFe(self, value):
        result = True
        # Validate type tpChaveDFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpChaveDFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpChaveDFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            self.tipoChaveDFe is not None or
            self.xTipoChaveDFe is not None or
            self.chaveDFe is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpDFeNacional', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpDFeNacional')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpDFeNacional':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpDFeNacional')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpDFeNacional', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpDFeNacional'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpDFeNacional', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.tipoChaveDFe is not None:
            namespaceprefix_ = self.tipoChaveDFe_nsprefix_ + ':' if (UseCapturedNS_ and self.tipoChaveDFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stipoChaveDFe>%s</%stipoChaveDFe>%s' % (namespaceprefix_ , self.gds_format_integer(self.tipoChaveDFe, input_name='tipoChaveDFe'), namespaceprefix_ , eol_))
        if self.xTipoChaveDFe is not None:
            namespaceprefix_ = self.xTipoChaveDFe_nsprefix_ + ':' if (UseCapturedNS_ and self.xTipoChaveDFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxTipoChaveDFe>%s</%sxTipoChaveDFe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xTipoChaveDFe), input_name='xTipoChaveDFe')), namespaceprefix_ , eol_))
        if self.chaveDFe is not None:
            namespaceprefix_ = self.chaveDFe_nsprefix_ + ':' if (UseCapturedNS_ and self.chaveDFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%schaveDFe>%s</%schaveDFe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.chaveDFe), input_name='chaveDFe')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'tipoChaveDFe' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'tipoChaveDFe')
            ival_ = self.gds_validate_integer(ival_, node, 'tipoChaveDFe')
            self.tipoChaveDFe = ival_
            self.tipoChaveDFe_nsprefix_ = child_.prefix
            # validate type tpTipoChaveDFE
            self.validate_tpTipoChaveDFE(self.tipoChaveDFe)
        elif nodeName_ == 'xTipoChaveDFe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xTipoChaveDFe')
            value_ = self.gds_validate_string(value_, node, 'xTipoChaveDFe')
            self.xTipoChaveDFe = value_
            self.xTipoChaveDFe_nsprefix_ = child_.prefix
            # validate type tpXTipoChaveDFe
            self.validate_tpXTipoChaveDFe(self.xTipoChaveDFe)
        elif nodeName_ == 'chaveDFe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'chaveDFe')
            value_ = self.gds_validate_string(value_, node, 'chaveDFe')
            self.chaveDFe = value_
            self.chaveDFe_nsprefix_ = child_.prefix
            # validate type tpChaveDFe
            self.validate_tpChaveDFe(self.chaveDFe)
# end class tpDFeNacional


class tpDocFiscalOutro(GeneratedsSuper):
    """tpDocFiscalOutro -- Grupo de informa
    ç
    õ
    es de documento fiscais, eletr
    ô
    nicos ou n
    ã
    o, que n
    ã
    o se encontram no reposit
    ó
    rio nacional.
    cMunDocFiscal -- C
    ó
    digo do munic
    í
    pio emissor do documento fiscal que n
    ã
    o se encontra no reposit
    ó
    rio nacional.
    nDocFiscal -- N
    ú
    mero do documento fiscal que n
    ã
    o se encontra no reposit
    ó
    rio nacional.
    xDocFiscal -- Descri
    ç
    ã
    o do documento fiscal.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('cMunDocFiscal', ['tpCidade', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'cMunDocFiscal', 'type': 'xs:int'}, None),
        MemberSpec_('nDocFiscal', ['tpNumeroDescricaoDocumento', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'nDocFiscal', 'type': 'xs:string'}, None),
        MemberSpec_('xDocFiscal', ['tpNumeroDescricaoDocumento', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'xDocFiscal', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, cMunDocFiscal=None, nDocFiscal=None, xDocFiscal=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.cMunDocFiscal = cMunDocFiscal
        self.validate_tpCidade(self.cMunDocFiscal)
        self.cMunDocFiscal_nsprefix_ = None
        self.nDocFiscal = nDocFiscal
        self.validate_tpNumeroDescricaoDocumento(self.nDocFiscal)
        self.nDocFiscal_nsprefix_ = None
        self.xDocFiscal = xDocFiscal
        self.validate_tpNumeroDescricaoDocumento(self.xDocFiscal)
        self.xDocFiscal_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpDocFiscalOutro)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpDocFiscalOutro.subclass:
            return tpDocFiscalOutro.subclass(*args_, **kwargs_)
        else:
            return tpDocFiscalOutro(*args_, **kwargs_)
    factory = staticmethod(factory)
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
    def validate_tpNumeroDescricaoDocumento(self, value):
        result = True
        # Validate type tpNumeroDescricaoDocumento, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpNumeroDescricaoDocumento' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpNumeroDescricaoDocumento' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            self.cMunDocFiscal is not None or
            self.nDocFiscal is not None or
            self.xDocFiscal is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpDocFiscalOutro', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpDocFiscalOutro')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpDocFiscalOutro':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpDocFiscalOutro')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpDocFiscalOutro', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpDocFiscalOutro'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpDocFiscalOutro', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cMunDocFiscal is not None:
            namespaceprefix_ = self.cMunDocFiscal_nsprefix_ + ':' if (UseCapturedNS_ and self.cMunDocFiscal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scMunDocFiscal>%s</%scMunDocFiscal>%s' % (namespaceprefix_ , self.gds_format_integer(self.cMunDocFiscal, input_name='cMunDocFiscal'), namespaceprefix_ , eol_))
        if self.nDocFiscal is not None:
            namespaceprefix_ = self.nDocFiscal_nsprefix_ + ':' if (UseCapturedNS_ and self.nDocFiscal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snDocFiscal>%s</%snDocFiscal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.nDocFiscal), input_name='nDocFiscal')), namespaceprefix_ , eol_))
        if self.xDocFiscal is not None:
            namespaceprefix_ = self.xDocFiscal_nsprefix_ + ':' if (UseCapturedNS_ and self.xDocFiscal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxDocFiscal>%s</%sxDocFiscal>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xDocFiscal), input_name='xDocFiscal')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'cMunDocFiscal' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'cMunDocFiscal')
            ival_ = self.gds_validate_integer(ival_, node, 'cMunDocFiscal')
            self.cMunDocFiscal = ival_
            self.cMunDocFiscal_nsprefix_ = child_.prefix
            # validate type tpCidade
            self.validate_tpCidade(self.cMunDocFiscal)
        elif nodeName_ == 'nDocFiscal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nDocFiscal')
            value_ = self.gds_validate_string(value_, node, 'nDocFiscal')
            self.nDocFiscal = value_
            self.nDocFiscal_nsprefix_ = child_.prefix
            # validate type tpNumeroDescricaoDocumento
            self.validate_tpNumeroDescricaoDocumento(self.nDocFiscal)
        elif nodeName_ == 'xDocFiscal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xDocFiscal')
            value_ = self.gds_validate_string(value_, node, 'xDocFiscal')
            self.xDocFiscal = value_
            self.xDocFiscal_nsprefix_ = child_.prefix
            # validate type tpNumeroDescricaoDocumento
            self.validate_tpNumeroDescricaoDocumento(self.xDocFiscal)
# end class tpDocFiscalOutro


class tpDocOutro(GeneratedsSuper):
    """tpDocOutro -- Grupo de informa
    ç
    õ
    es de documento n
    ã
    o fiscal.
    nDoc -- N
    ú
    mero do documento n
    ã
    o fiscal.
    xDoc -- Descri
    ç
    ã
    o do documento n
    ã
    o fiscal.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('nDoc', ['tpNumeroDescricaoDocumento', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'nDoc', 'type': 'xs:string'}, None),
        MemberSpec_('xDoc', ['tpNumeroDescricaoDocumento', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'xDoc', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, nDoc=None, xDoc=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.nDoc = nDoc
        self.validate_tpNumeroDescricaoDocumento(self.nDoc)
        self.nDoc_nsprefix_ = None
        self.xDoc = xDoc
        self.validate_tpNumeroDescricaoDocumento(self.xDoc)
        self.xDoc_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpDocOutro)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpDocOutro.subclass:
            return tpDocOutro.subclass(*args_, **kwargs_)
        else:
            return tpDocOutro(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpNumeroDescricaoDocumento(self, value):
        result = True
        # Validate type tpNumeroDescricaoDocumento, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpNumeroDescricaoDocumento' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpNumeroDescricaoDocumento' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            self.nDoc is not None or
            self.xDoc is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpDocOutro', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpDocOutro')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpDocOutro':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpDocOutro')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpDocOutro', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpDocOutro'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpDocOutro', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.nDoc is not None:
            namespaceprefix_ = self.nDoc_nsprefix_ + ':' if (UseCapturedNS_ and self.nDoc_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snDoc>%s</%snDoc>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.nDoc), input_name='nDoc')), namespaceprefix_ , eol_))
        if self.xDoc is not None:
            namespaceprefix_ = self.xDoc_nsprefix_ + ':' if (UseCapturedNS_ and self.xDoc_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxDoc>%s</%sxDoc>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xDoc), input_name='xDoc')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'nDoc':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nDoc')
            value_ = self.gds_validate_string(value_, node, 'nDoc')
            self.nDoc = value_
            self.nDoc_nsprefix_ = child_.prefix
            # validate type tpNumeroDescricaoDocumento
            self.validate_tpNumeroDescricaoDocumento(self.nDoc)
        elif nodeName_ == 'xDoc':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xDoc')
            value_ = self.gds_validate_string(value_, node, 'xDoc')
            self.xDoc = value_
            self.xDoc_nsprefix_ = child_.prefix
            # validate type tpNumeroDescricaoDocumento
            self.validate_tpNumeroDescricaoDocumento(self.xDoc)
# end class tpDocOutro


class tpFornecedor(GeneratedsSuper):
    """tpFornecedor -- Grupo de informa
    ç
    õ
    es do fornecedor do documento referenciado.
    xNome -- Nome do fornecedor.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('CPF', ['tpCPF', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CPF', 'type': 'xs:string'}, None),
        MemberSpec_('CNPJ', ['tpCNPJ', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CNPJ', 'type': 'xs:string'}, None),
        MemberSpec_('NIF', ['tpNIF', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'NIF', 'type': 'xs:string'}, None),
        MemberSpec_('NaoNIF', ['tpNaoNIF', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'NaoNIF', 'type': 'xs:int'}, None),
        MemberSpec_('xNome', ['tpRazaoSocialObrigatorio', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'xNome', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, CPF=None, CNPJ=None, NIF=None, NaoNIF=None, xNome=None, gds_collector_=None, **kwargs_):
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
        self.NIF = NIF
        self.validate_tpNIF(self.NIF)
        self.NIF_nsprefix_ = None
        self.NaoNIF = NaoNIF
        self.validate_tpNaoNIF(self.NaoNIF)
        self.NaoNIF_nsprefix_ = None
        self.xNome = xNome
        self.validate_tpRazaoSocialObrigatorio(self.xNome)
        self.xNome_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpFornecedor)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpFornecedor.subclass:
            return tpFornecedor.subclass(*args_, **kwargs_)
        else:
            return tpFornecedor(*args_, **kwargs_)
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
    validate_tpCNPJ_patterns_ = [['^([0-9A-Z]{12}[0-9]{2})$']]
    def validate_tpNIF(self, value):
        result = True
        # Validate type tpNIF, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpNIF' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpNIF' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpNaoNIF(self, value):
        result = True
        # Validate type tpNaoNIF, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [0, 1, 2]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpNaoNIF' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpRazaoSocialObrigatorio(self, value):
        result = True
        # Validate type tpRazaoSocialObrigatorio, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 75:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpRazaoSocialObrigatorio' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpRazaoSocialObrigatorio' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            self.CPF is not None or
            self.CNPJ is not None or
            self.NIF is not None or
            self.NaoNIF is not None or
            self.xNome is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpFornecedor', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpFornecedor')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpFornecedor':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpFornecedor')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpFornecedor', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpFornecedor'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpFornecedor', fromsubclass_=False, pretty_print=True):
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
        if self.NIF is not None:
            namespaceprefix_ = self.NIF_nsprefix_ + ':' if (UseCapturedNS_ and self.NIF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNIF>%s</%sNIF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NIF), input_name='NIF')), namespaceprefix_ , eol_))
        if self.NaoNIF is not None:
            namespaceprefix_ = self.NaoNIF_nsprefix_ + ':' if (UseCapturedNS_ and self.NaoNIF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNaoNIF>%s</%sNaoNIF>%s' % (namespaceprefix_ , self.gds_format_integer(self.NaoNIF, input_name='NaoNIF'), namespaceprefix_ , eol_))
        if self.xNome is not None:
            namespaceprefix_ = self.xNome_nsprefix_ + ':' if (UseCapturedNS_ and self.xNome_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxNome>%s</%sxNome>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xNome), input_name='xNome')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
        elif nodeName_ == 'NIF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NIF')
            value_ = self.gds_validate_string(value_, node, 'NIF')
            self.NIF = value_
            self.NIF_nsprefix_ = child_.prefix
            # validate type tpNIF
            self.validate_tpNIF(self.NIF)
        elif nodeName_ == 'NaoNIF' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'NaoNIF')
            ival_ = self.gds_validate_integer(ival_, node, 'NaoNIF')
            self.NaoNIF = ival_
            self.NaoNIF_nsprefix_ = child_.prefix
            # validate type tpNaoNIF
            self.validate_tpNaoNIF(self.NaoNIF)
        elif nodeName_ == 'xNome':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xNome')
            value_ = self.gds_validate_string(value_, node, 'xNome')
            self.xNome = value_
            self.xNome_nsprefix_ = child_.prefix
            # validate type tpRazaoSocialObrigatorio
            self.validate_tpRazaoSocialObrigatorio(self.xNome)
# end class tpFornecedor


class tpAtividadeEvento(GeneratedsSuper):
    """tpAtividadeEvento -- Tipo de informa
    ç
    õ
    es relativas
    à
    atividades de eventos.
    xNomeEvt -- Nome do evento cultural, art
    í
    stico, esportivo.
    dtIniEvt -- Data de in
    í
    cio da atividade de evento. Ano, M
    ê
    s e Dia (AAAA-MM-DD).
    dtFimEvt -- Data de fim da atividade de evento. Ano, M
    ê
    s e Dia (AAAA-MM-DD).
    end -- Endere
    ç
    o do Evento.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('xNomeEvt', ['tpXNomeEvt', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'xNomeEvt', 'type': 'xs:string'}, None),
        MemberSpec_('dtIniEvt', 'xs:date', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'dtIniEvt', 'type': 'xs:date'}, None),
        MemberSpec_('dtFimEvt', 'xs:date', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'dtFimEvt', 'type': 'xs:date'}, None),
        MemberSpec_('end', 'tpEnderecoSimplesIBSCBS', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'end', 'type': 'tpEnderecoSimplesIBSCBS'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, xNomeEvt=None, dtIniEvt=None, dtFimEvt=None, end=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.xNomeEvt = xNomeEvt
        self.validate_tpXNomeEvt(self.xNomeEvt)
        self.xNomeEvt_nsprefix_ = None
        if isinstance(dtIniEvt, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dtIniEvt, '%Y-%m-%d').date()
        else:
            initvalue_ = dtIniEvt
        self.dtIniEvt = initvalue_
        self.dtIniEvt_nsprefix_ = None
        if isinstance(dtFimEvt, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dtFimEvt, '%Y-%m-%d').date()
        else:
            initvalue_ = dtFimEvt
        self.dtFimEvt = initvalue_
        self.dtFimEvt_nsprefix_ = None
        self.end = end
        self.end_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpAtividadeEvento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpAtividadeEvento.subclass:
            return tpAtividadeEvento.subclass(*args_, **kwargs_)
        else:
            return tpAtividadeEvento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpXNomeEvt(self, value):
        result = True
        # Validate type tpXNomeEvt, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on tpXNomeEvt' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on tpXNomeEvt' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            self.xNomeEvt is not None or
            self.dtIniEvt is not None or
            self.dtFimEvt is not None or
            self.end is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpAtividadeEvento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpAtividadeEvento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpAtividadeEvento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpAtividadeEvento')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpAtividadeEvento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpAtividadeEvento'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpAtividadeEvento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.xNomeEvt is not None:
            namespaceprefix_ = self.xNomeEvt_nsprefix_ + ':' if (UseCapturedNS_ and self.xNomeEvt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxNomeEvt>%s</%sxNomeEvt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xNomeEvt), input_name='xNomeEvt')), namespaceprefix_ , eol_))
        if self.dtIniEvt is not None:
            namespaceprefix_ = self.dtIniEvt_nsprefix_ + ':' if (UseCapturedNS_ and self.dtIniEvt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdtIniEvt>%s</%sdtIniEvt>%s' % (namespaceprefix_ , self.gds_format_date(self.dtIniEvt, input_name='dtIniEvt'), namespaceprefix_ , eol_))
        if self.dtFimEvt is not None:
            namespaceprefix_ = self.dtFimEvt_nsprefix_ + ':' if (UseCapturedNS_ and self.dtFimEvt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdtFimEvt>%s</%sdtFimEvt>%s' % (namespaceprefix_ , self.gds_format_date(self.dtFimEvt, input_name='dtFimEvt'), namespaceprefix_ , eol_))
        if self.end is not None:
            namespaceprefix_ = self.end_nsprefix_ + ':' if (UseCapturedNS_ and self.end_nsprefix_) else ''
            self.end.export(outfile, level, namespaceprefix_, namespacedef_='', name_='end', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'xNomeEvt':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xNomeEvt')
            value_ = self.gds_validate_string(value_, node, 'xNomeEvt')
            self.xNomeEvt = value_
            self.xNomeEvt_nsprefix_ = child_.prefix
            # validate type tpXNomeEvt
            self.validate_tpXNomeEvt(self.xNomeEvt)
        elif nodeName_ == 'dtIniEvt':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.dtIniEvt = dval_
            self.dtIniEvt_nsprefix_ = child_.prefix
        elif nodeName_ == 'dtFimEvt':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.dtFimEvt = dval_
            self.dtFimEvt_nsprefix_ = child_.prefix
        elif nodeName_ == 'end':
            obj_ = tpEnderecoSimplesIBSCBS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.end = obj_
            obj_.original_tagname_ = 'end'
# end class tpAtividadeEvento


class tpIBSCBS(GeneratedsSuper):
    """tpIBSCBS -- Tipo das informa
    ç
    õ
    es do IBS/CBS.
    finNFSe -- Indicador da finalidade da emiss
    ã
    o de NFS-e.
    0 = NFS-e regular.
    indFinal -- Indica opera
    ç
    ã
    o de uso ou consumo pessoal. (0-N
    ã
    o ou 1-Sim).
    0 - N
    ã
    o.
    1 - Sim.
    cIndOp -- C
    ó
    digo indicador da opera
    ç
    ã
    o de fornecimento, conforme tabela "c
    ó
    digo indicador de opera
    ç
    ã
    o".
    Referente
    à
    tabela de indicador da opera
    ç
    ã
    o publicada no ANEXO AnexoVII-IndOp_IBSCBS_V1.00.00-.xlsx.
    tpOper -- Tipo de Opera
    ç
    ã
    o com Entes Governamentais ou outros servi
    ç
    os sobre bens im
    ó
    veis.
    gRefNFSe -- Grupo de NFS-e referenciadas.
    tpEnteGov -- Tipo do ente da compra governamental.
    indDest -- Indica o Destinat
    á
    rio dos servi
    ç
    os.
    dest -- Destinat
    á
    rio.
    valores -- Informa
    ç
    õ
    es relacionadas aos valores do servi
    ç
    o prestado para IBS e
    à
    CBS.
    imovelobra -- Informa
    ç
    õ
    es sobre o Tipo de Im
    ó
    vel/Obra.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('finNFSe', ['tpFinNFSe', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'finNFSe', 'type': 'xs:int'}, None),
        MemberSpec_('indFinal', ['tpNaoSim', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'indFinal', 'type': 'xs:int'}, None),
        MemberSpec_('cIndOp', ['tpCIndOp', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'cIndOp', 'type': 'xs:string'}, None),
        MemberSpec_('tpOper', ['tpOper', 'xs:int'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'tpOper', 'type': 'xs:int'}, None),
        MemberSpec_('gRefNFSe', 'tpGRefNFSe', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'gRefNFSe', 'type': 'tpGRefNFSe'}, None),
        MemberSpec_('tpEnteGov', ['tpEnteGov', 'xs:int'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'tpEnteGov', 'type': 'xs:int'}, None),
        MemberSpec_('indDest', ['tpIndDest', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'indDest', 'type': 'xs:int'}, None),
        MemberSpec_('dest', 'tpInformacoesPessoa', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'dest', 'type': 'tpInformacoesPessoa'}, None),
        MemberSpec_('valores', 'tpValores', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'valores', 'type': 'tpValores'}, None),
        MemberSpec_('imovelobra', 'tpImovelObra', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'imovelobra', 'type': 'tpImovelObra'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, finNFSe=None, indFinal=None, cIndOp=None, tpOper=None, gRefNFSe=None, tpEnteGov=None, indDest=None, dest=None, valores=None, imovelobra=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.finNFSe = finNFSe
        self.validate_tpFinNFSe(self.finNFSe)
        self.finNFSe_nsprefix_ = None
        self.indFinal = indFinal
        self.validate_tpNaoSim(self.indFinal)
        self.indFinal_nsprefix_ = None
        self.cIndOp = cIndOp
        self.validate_tpCIndOp(self.cIndOp)
        self.cIndOp_nsprefix_ = None
        self.tpOper = tpOper
        self.validate_tpOper(self.tpOper)
        self.tpOper_nsprefix_ = None
        self.gRefNFSe = gRefNFSe
        self.gRefNFSe_nsprefix_ = None
        self.tpEnteGov = tpEnteGov
        self.validate_tpEnteGov(self.tpEnteGov)
        self.tpEnteGov_nsprefix_ = None
        self.indDest = indDest
        self.validate_tpIndDest(self.indDest)
        self.indDest_nsprefix_ = None
        self.dest = dest
        self.dest_nsprefix_ = None
        self.valores = valores
        self.valores_nsprefix_ = None
        self.imovelobra = imovelobra
        self.imovelobra_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpIBSCBS)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpIBSCBS.subclass:
            return tpIBSCBS.subclass(*args_, **kwargs_)
        else:
            return tpIBSCBS(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpFinNFSe(self, value):
        result = True
        # Validate type tpFinNFSe, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [0]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpFinNFSe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpNaoSim(self, value):
        result = True
        # Validate type tpNaoSim, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [0, 1]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpNaoSim' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpNaoSim_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpNaoSim_patterns_, ))
                result = False
        return result
    validate_tpNaoSim_patterns_ = [['^([01]{1})$']]
    def validate_tpCIndOp(self, value):
        result = True
        # Validate type tpCIndOp, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCIndOp_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCIndOp_patterns_, ))
                result = False
        return result
    validate_tpCIndOp_patterns_ = [['^([0-9]{6})$']]
    def validate_tpOper(self, value):
        result = True
        # Validate type tpOper, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [1, 2, 3, 4, 5]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpOper' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpEnteGov(self, value):
        result = True
        # Validate type tpEnteGov, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [1, 2, 3, 4]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpEnteGov' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tpIndDest(self, value):
        result = True
        # Validate type tpIndDest, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [0, 1]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpIndDest' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def has__content(self):
        if (
            self.finNFSe is not None or
            self.indFinal is not None or
            self.cIndOp is not None or
            self.tpOper is not None or
            self.gRefNFSe is not None or
            self.tpEnteGov is not None or
            self.indDest is not None or
            self.dest is not None or
            self.valores is not None or
            self.imovelobra is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpIBSCBS', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpIBSCBS')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpIBSCBS':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpIBSCBS')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpIBSCBS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpIBSCBS'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpIBSCBS', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.finNFSe is not None:
            namespaceprefix_ = self.finNFSe_nsprefix_ + ':' if (UseCapturedNS_ and self.finNFSe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfinNFSe>%s</%sfinNFSe>%s' % (namespaceprefix_ , self.gds_format_integer(self.finNFSe, input_name='finNFSe'), namespaceprefix_ , eol_))
        if self.indFinal is not None:
            namespaceprefix_ = self.indFinal_nsprefix_ + ':' if (UseCapturedNS_ and self.indFinal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindFinal>%s</%sindFinal>%s' % (namespaceprefix_ , self.gds_format_integer(self.indFinal, input_name='indFinal'), namespaceprefix_ , eol_))
        if self.cIndOp is not None:
            namespaceprefix_ = self.cIndOp_nsprefix_ + ':' if (UseCapturedNS_ and self.cIndOp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scIndOp>%s</%scIndOp>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cIndOp), input_name='cIndOp')), namespaceprefix_ , eol_))
        if self.tpOper is not None:
            namespaceprefix_ = self.tpOper_nsprefix_ + ':' if (UseCapturedNS_ and self.tpOper_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpOper>%s</%stpOper>%s' % (namespaceprefix_ , self.gds_format_integer(self.tpOper, input_name='tpOper'), namespaceprefix_ , eol_))
        if self.gRefNFSe is not None:
            namespaceprefix_ = self.gRefNFSe_nsprefix_ + ':' if (UseCapturedNS_ and self.gRefNFSe_nsprefix_) else ''
            self.gRefNFSe.export(outfile, level, namespaceprefix_, namespacedef_='', name_='gRefNFSe', pretty_print=pretty_print)
        if self.tpEnteGov is not None:
            namespaceprefix_ = self.tpEnteGov_nsprefix_ + ':' if (UseCapturedNS_ and self.tpEnteGov_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpEnteGov>%s</%stpEnteGov>%s' % (namespaceprefix_ , self.gds_format_integer(self.tpEnteGov, input_name='tpEnteGov'), namespaceprefix_ , eol_))
        if self.indDest is not None:
            namespaceprefix_ = self.indDest_nsprefix_ + ':' if (UseCapturedNS_ and self.indDest_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindDest>%s</%sindDest>%s' % (namespaceprefix_ , self.gds_format_integer(self.indDest, input_name='indDest'), namespaceprefix_ , eol_))
        if self.dest is not None:
            namespaceprefix_ = self.dest_nsprefix_ + ':' if (UseCapturedNS_ and self.dest_nsprefix_) else ''
            self.dest.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dest', pretty_print=pretty_print)
        if self.valores is not None:
            namespaceprefix_ = self.valores_nsprefix_ + ':' if (UseCapturedNS_ and self.valores_nsprefix_) else ''
            self.valores.export(outfile, level, namespaceprefix_, namespacedef_='', name_='valores', pretty_print=pretty_print)
        if self.imovelobra is not None:
            namespaceprefix_ = self.imovelobra_nsprefix_ + ':' if (UseCapturedNS_ and self.imovelobra_nsprefix_) else ''
            self.imovelobra.export(outfile, level, namespaceprefix_, namespacedef_='', name_='imovelobra', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'finNFSe' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'finNFSe')
            ival_ = self.gds_validate_integer(ival_, node, 'finNFSe')
            self.finNFSe = ival_
            self.finNFSe_nsprefix_ = child_.prefix
            # validate type tpFinNFSe
            self.validate_tpFinNFSe(self.finNFSe)
        elif nodeName_ == 'indFinal' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'indFinal')
            ival_ = self.gds_validate_integer(ival_, node, 'indFinal')
            self.indFinal = ival_
            self.indFinal_nsprefix_ = child_.prefix
            # validate type tpNaoSim
            self.validate_tpNaoSim(self.indFinal)
        elif nodeName_ == 'cIndOp':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cIndOp')
            value_ = self.gds_validate_string(value_, node, 'cIndOp')
            self.cIndOp = value_
            self.cIndOp_nsprefix_ = child_.prefix
            # validate type tpCIndOp
            self.validate_tpCIndOp(self.cIndOp)
        elif nodeName_ == 'tpOper' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'tpOper')
            ival_ = self.gds_validate_integer(ival_, node, 'tpOper')
            self.tpOper = ival_
            self.tpOper_nsprefix_ = child_.prefix
            # validate type tpOper
            self.validate_tpOper(self.tpOper)
        elif nodeName_ == 'gRefNFSe':
            obj_ = tpGRefNFSe.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.gRefNFSe = obj_
            obj_.original_tagname_ = 'gRefNFSe'
        elif nodeName_ == 'tpEnteGov' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'tpEnteGov')
            ival_ = self.gds_validate_integer(ival_, node, 'tpEnteGov')
            self.tpEnteGov = ival_
            self.tpEnteGov_nsprefix_ = child_.prefix
            # validate type tpEnteGov
            self.validate_tpEnteGov(self.tpEnteGov)
        elif nodeName_ == 'indDest' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'indDest')
            ival_ = self.gds_validate_integer(ival_, node, 'indDest')
            self.indDest = ival_
            self.indDest_nsprefix_ = child_.prefix
            # validate type tpIndDest
            self.validate_tpIndDest(self.indDest)
        elif nodeName_ == 'dest':
            obj_ = tpInformacoesPessoa.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dest = obj_
            obj_.original_tagname_ = 'dest'
        elif nodeName_ == 'valores':
            obj_ = tpValores.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.valores = obj_
            obj_.original_tagname_ = 'valores'
        elif nodeName_ == 'imovelobra':
            obj_ = tpImovelObra.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.imovelobra = obj_
            obj_.original_tagname_ = 'imovelobra'
# end class tpIBSCBS


class tpGIBSCBS(GeneratedsSuper):
    """tpGIBSCBS -- Informa
    ç
    õ
    es relacionadas ao IBS e
    à
    CBS.
    cClassTrib -- C
    ó
    digo de classifica
    ç
    ã
    o Tribut
    á
    ria do IBS e da CBS.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('cClassTrib', ['tpClassificacaoTributaria', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'cClassTrib', 'type': 'xs:string'}, None),
        MemberSpec_('gTribRegular', 'tpGTribRegular', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'gTribRegular', 'type': 'tpGTribRegular'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, cClassTrib=None, gTribRegular=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.cClassTrib = cClassTrib
        self.validate_tpClassificacaoTributaria(self.cClassTrib)
        self.cClassTrib_nsprefix_ = None
        self.gTribRegular = gTribRegular
        self.gTribRegular_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpGIBSCBS)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpGIBSCBS.subclass:
            return tpGIBSCBS.subclass(*args_, **kwargs_)
        else:
            return tpGIBSCBS(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpClassificacaoTributaria(self, value):
        result = True
        # Validate type tpClassificacaoTributaria, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpClassificacaoTributaria_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpClassificacaoTributaria_patterns_, ))
                result = False
        return result
    validate_tpClassificacaoTributaria_patterns_ = [['^([0-9]{6})$']]
    def has__content(self):
        if (
            self.cClassTrib is not None or
            self.gTribRegular is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpGIBSCBS', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpGIBSCBS')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpGIBSCBS':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpGIBSCBS')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpGIBSCBS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpGIBSCBS'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpGIBSCBS', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cClassTrib is not None:
            namespaceprefix_ = self.cClassTrib_nsprefix_ + ':' if (UseCapturedNS_ and self.cClassTrib_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scClassTrib>%s</%scClassTrib>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cClassTrib), input_name='cClassTrib')), namespaceprefix_ , eol_))
        if self.gTribRegular is not None:
            namespaceprefix_ = self.gTribRegular_nsprefix_ + ':' if (UseCapturedNS_ and self.gTribRegular_nsprefix_) else ''
            self.gTribRegular.export(outfile, level, namespaceprefix_, namespacedef_='', name_='gTribRegular', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'cClassTrib':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cClassTrib')
            value_ = self.gds_validate_string(value_, node, 'cClassTrib')
            self.cClassTrib = value_
            self.cClassTrib_nsprefix_ = child_.prefix
            # validate type tpClassificacaoTributaria
            self.validate_tpClassificacaoTributaria(self.cClassTrib)
        elif nodeName_ == 'gTribRegular':
            obj_ = tpGTribRegular.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.gTribRegular = obj_
            obj_.original_tagname_ = 'gTribRegular'
# end class tpGIBSCBS


class tpGTribRegular(GeneratedsSuper):
    """tpGTribRegular -- Informa
    ç
    õ
    es relacionadas
    à
    tributa
    ç
    ã
    o regular.
    cClassTribReg -- C
    ó
    digo de classifica
    ç
    ã
    o Tribut
    á
    ria do IBS e da CBS.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('cClassTribReg', ['tpClassificacaoTributaria', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'cClassTribReg', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, cClassTribReg=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.cClassTribReg = cClassTribReg
        self.validate_tpClassificacaoTributaria(self.cClassTribReg)
        self.cClassTribReg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpGTribRegular)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpGTribRegular.subclass:
            return tpGTribRegular.subclass(*args_, **kwargs_)
        else:
            return tpGTribRegular(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tpClassificacaoTributaria(self, value):
        result = True
        # Validate type tpClassificacaoTributaria, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpClassificacaoTributaria_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpClassificacaoTributaria_patterns_, ))
                result = False
        return result
    validate_tpClassificacaoTributaria_patterns_ = [['^([0-9]{6})$']]
    def has__content(self):
        if (
            self.cClassTribReg is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpGTribRegular', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpGTribRegular')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpGTribRegular':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpGTribRegular')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpGTribRegular', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpGTribRegular'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpGTribRegular', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cClassTribReg is not None:
            namespaceprefix_ = self.cClassTribReg_nsprefix_ + ':' if (UseCapturedNS_ and self.cClassTribReg_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scClassTribReg>%s</%scClassTribReg>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cClassTribReg), input_name='cClassTribReg')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'cClassTribReg':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cClassTribReg')
            value_ = self.gds_validate_string(value_, node, 'cClassTribReg')
            self.cClassTribReg = value_
            self.cClassTribReg_nsprefix_ = child_.prefix
            # validate type tpClassificacaoTributaria
            self.validate_tpClassificacaoTributaria(self.cClassTribReg)
# end class tpGTribRegular


class tpRetornoComplementarIBSCBS(GeneratedsSuper):
    """tpRetornoComplementarIBSCBS -- Informa
    ç
    õ
    es complementares referente ao IBS e
    à
    CBS.
    Adquirente -- Adquirente.
    ValorBCIBSCBS -- Valor da base de c
    á
    lculo (BC) do IBS/CBS antes das reduc
    õ
    es para c
    á
    lculo do tributo bruto.
    ValorAliqEstadualIBS -- Al
    í
    quota do IBS de compet
    ê
    ncia do Estado.
    ValorPercRedEstadualIBS -- Percentual de redu
    ç
    ã
    o de al
    í
    quota estadual do IBS.
    ValorAliqEfetivaEstadualIBS -- Al
    í
    quota efetiva estadual do IBS.
    ValorEstadualIBS -- Valor do Tributo do IBS da UF calculado.
    ValorAliqMunicipalIBS -- Al
    í
    quota do IBS de compet
    ê
    ncia do Munic
    í
    pio.
    ValorPercRedMunicipalIBS -- Percentual de redu
    ç
    ã
    o de aliquota municipal.
    ValorAliqEfetivaMunicipalIBS -- Al
    í
    quota efetiva municipal do IBS.
    ValorMunicipalIBS -- Valor do Tributo do IBS do Munic
    í
    pio calculado.
    ValorIBS -- Valor do IBS Total.
    ValorAliqCBS -- Al
    í
    quota da CBS.
    ValorPercRedCBS -- Percentual da redu
    ç
    ã
    o de al
    í
    quota para a CBS.
    ValorAliqEfetivaCBS -- Al
    í
    quota efetiva CBS.
    ValorCBS -- Valor do Tributo da CBS calculado. Total Valor da CBS da Uni
    ã
    o.
    ValorPercDiferimentoEstadual -- Percentual de diferimento estadual.
    ValorDiferimentoEstadual -- Total do Diferimento do IBS estadual.
    ValorPercDiferimentoMunicipal -- Percentual de diferimento municipal.
    ValorDiferimentoMunicipal -- Total do Diferimento do IBS municipal.
    ValorPercDiferimentoCBS -- Percentual de diferimento da CBS.
    ValorDiferimentoCBS -- Total do Diferimento CBS.
    CodigoClassCredPresumidoIBS -- C
    ó
    digo e classifica
    ç
    ã
    o do cr
    é
    dito presumido IBS.
    ValorPercCredPresumidoIBS -- Al
    í
    quota do Cr
    é
    dito Presumido para o IBS.
    ValorCredPresumidoIBS -- Valor do Cr
    é
    dito Presumido para o IBS.
    CodigoClassCredPresumidoCBS -- C
    ó
    digo de Classifica
    ç
    ã
    o do Cr
    é
    dito Presumido CBS.
    ValorPercCredPresumidoCBS -- Al
    í
    quota de cr
    é
    dito presumido para a CBS.
    ValorCredPresumidoCBS -- Valor do Cr
    é
    dito Presumido CBS.
    ValorAliqEstadualRegularIBS -- Al
    í
    quota efetiva de tributa
    ç
    ã
    o regular do IBS estadual.
    ValorAliqMunicipalRegularIBS -- Al
    í
    quota efetiva de tributa
    ç
    ã
    o regular do IBS municipal.
    ValorAliqRegularCBS -- Al
    í
    quota efetiva de tributa
    ç
    ã
    o regular da CBS.
    ValorEstadualRegularIBS -- Valor da tributa
    ç
    ã
    o regular do IBS estadual.
    ValorMunicipalRegularIBS -- Valor da tributa
    ç
    ã
    o regular do IBS municipal.
    ValorRegularCBS -- Valor da tributa
    ç
    ã
    o regular da CBS.
    ValorTotalReeRepRes -- Valor total dos valores n
    ã
    o inclusos na base de c
    á
    lculo, somat
    ó
    ria dos valores informados pelo contribuinte no campo vlrReeRepRes.
    ValorAliqEstadualIBSCompraGov -- Valor da al
    í
    quota estadual para o IBS, referente a compra governamental.
    ValorEstadualBSCompraGov -- Valor do IBS estadual referente a compra governamental
    ValorAliqMunicipalIBSCompraGov -- Valor da al
    í
    quota municipal para o IBS, referente a compra governamental.
    ValorMunicipalIBSCompraGov -- Valor do IBS municipal referente a compra governamental
    ValorAliqCBSCompraGov -- Valor da al
    í
    quota da CBS, referente a compra governamental.
    ValorCBSCompraGov -- Valor da CBS referente a compra governamental

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Adquirente', 'tpInformacoesPessoa', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Adquirente', 'type': 'tpInformacoesPessoa'}, None),
        MemberSpec_('ValorBCIBSCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorBCIBSCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqEstadualIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqEstadualIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorPercRedEstadualIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorPercRedEstadualIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqEfetivaEstadualIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqEfetivaEstadualIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorEstadualIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorEstadualIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqMunicipalIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqMunicipalIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorPercRedMunicipalIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorPercRedMunicipalIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqEfetivaMunicipalIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqEfetivaMunicipalIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorMunicipalIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorMunicipalIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorPercRedCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorPercRedCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqEfetivaCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqEfetivaCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorPercDiferimentoEstadual', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorPercDiferimentoEstadual', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorDiferimentoEstadual', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorDiferimentoEstadual', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorPercDiferimentoMunicipal', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorPercDiferimentoMunicipal', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorDiferimentoMunicipal', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorDiferimentoMunicipal', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorPercDiferimentoCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorPercDiferimentoCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorDiferimentoCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorDiferimentoCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('CodigoClassCredPresumidoIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CodigoClassCredPresumidoIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorPercCredPresumidoIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorPercCredPresumidoIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorCredPresumidoIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorCredPresumidoIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('CodigoClassCredPresumidoCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CodigoClassCredPresumidoCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorPercCredPresumidoCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorPercCredPresumidoCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorCredPresumidoCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorCredPresumidoCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqEstadualRegularIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqEstadualRegularIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqMunicipalRegularIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqMunicipalRegularIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqRegularCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqRegularCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorEstadualRegularIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorEstadualRegularIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorMunicipalRegularIBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorMunicipalRegularIBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorRegularCBS', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorRegularCBS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorTotalReeRepRes', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorTotalReeRepRes', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqEstadualIBSCompraGov', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqEstadualIBSCompraGov', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorEstadualBSCompraGov', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorEstadualBSCompraGov', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqMunicipalIBSCompraGov', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqMunicipalIBSCompraGov', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorMunicipalIBSCompraGov', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorMunicipalIBSCompraGov', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorAliqCBSCompraGov', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorAliqCBSCompraGov', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorCBSCompraGov', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorCBSCompraGov', 'type': 'xs:decimal'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Adquirente=None, ValorBCIBSCBS=None, ValorAliqEstadualIBS=None, ValorPercRedEstadualIBS=None, ValorAliqEfetivaEstadualIBS=None, ValorEstadualIBS=None, ValorAliqMunicipalIBS=None, ValorPercRedMunicipalIBS=None, ValorAliqEfetivaMunicipalIBS=None, ValorMunicipalIBS=None, ValorIBS=None, ValorAliqCBS=None, ValorPercRedCBS=None, ValorAliqEfetivaCBS=None, ValorCBS=None, ValorPercDiferimentoEstadual=None, ValorDiferimentoEstadual=None, ValorPercDiferimentoMunicipal=None, ValorDiferimentoMunicipal=None, ValorPercDiferimentoCBS=None, ValorDiferimentoCBS=None, CodigoClassCredPresumidoIBS=None, ValorPercCredPresumidoIBS=None, ValorCredPresumidoIBS=None, CodigoClassCredPresumidoCBS=None, ValorPercCredPresumidoCBS=None, ValorCredPresumidoCBS=None, ValorAliqEstadualRegularIBS=None, ValorAliqMunicipalRegularIBS=None, ValorAliqRegularCBS=None, ValorEstadualRegularIBS=None, ValorMunicipalRegularIBS=None, ValorRegularCBS=None, ValorTotalReeRepRes=None, ValorAliqEstadualIBSCompraGov=None, ValorEstadualBSCompraGov=None, ValorAliqMunicipalIBSCompraGov=None, ValorMunicipalIBSCompraGov=None, ValorAliqCBSCompraGov=None, ValorCBSCompraGov=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Adquirente = Adquirente
        self.Adquirente_nsprefix_ = None
        self.ValorBCIBSCBS = ValorBCIBSCBS
        self.validate_tpValor(self.ValorBCIBSCBS)
        self.ValorBCIBSCBS_nsprefix_ = None
        self.ValorAliqEstadualIBS = ValorAliqEstadualIBS
        self.validate_tpValor(self.ValorAliqEstadualIBS)
        self.ValorAliqEstadualIBS_nsprefix_ = None
        self.ValorPercRedEstadualIBS = ValorPercRedEstadualIBS
        self.validate_tpValor(self.ValorPercRedEstadualIBS)
        self.ValorPercRedEstadualIBS_nsprefix_ = None
        self.ValorAliqEfetivaEstadualIBS = ValorAliqEfetivaEstadualIBS
        self.validate_tpValor(self.ValorAliqEfetivaEstadualIBS)
        self.ValorAliqEfetivaEstadualIBS_nsprefix_ = None
        self.ValorEstadualIBS = ValorEstadualIBS
        self.validate_tpValor(self.ValorEstadualIBS)
        self.ValorEstadualIBS_nsprefix_ = None
        self.ValorAliqMunicipalIBS = ValorAliqMunicipalIBS
        self.validate_tpValor(self.ValorAliqMunicipalIBS)
        self.ValorAliqMunicipalIBS_nsprefix_ = None
        self.ValorPercRedMunicipalIBS = ValorPercRedMunicipalIBS
        self.validate_tpValor(self.ValorPercRedMunicipalIBS)
        self.ValorPercRedMunicipalIBS_nsprefix_ = None
        self.ValorAliqEfetivaMunicipalIBS = ValorAliqEfetivaMunicipalIBS
        self.validate_tpValor(self.ValorAliqEfetivaMunicipalIBS)
        self.ValorAliqEfetivaMunicipalIBS_nsprefix_ = None
        self.ValorMunicipalIBS = ValorMunicipalIBS
        self.validate_tpValor(self.ValorMunicipalIBS)
        self.ValorMunicipalIBS_nsprefix_ = None
        self.ValorIBS = ValorIBS
        self.validate_tpValor(self.ValorIBS)
        self.ValorIBS_nsprefix_ = None
        self.ValorAliqCBS = ValorAliqCBS
        self.validate_tpValor(self.ValorAliqCBS)
        self.ValorAliqCBS_nsprefix_ = None
        self.ValorPercRedCBS = ValorPercRedCBS
        self.validate_tpValor(self.ValorPercRedCBS)
        self.ValorPercRedCBS_nsprefix_ = None
        self.ValorAliqEfetivaCBS = ValorAliqEfetivaCBS
        self.validate_tpValor(self.ValorAliqEfetivaCBS)
        self.ValorAliqEfetivaCBS_nsprefix_ = None
        self.ValorCBS = ValorCBS
        self.validate_tpValor(self.ValorCBS)
        self.ValorCBS_nsprefix_ = None
        self.ValorPercDiferimentoEstadual = ValorPercDiferimentoEstadual
        self.validate_tpValor(self.ValorPercDiferimentoEstadual)
        self.ValorPercDiferimentoEstadual_nsprefix_ = None
        self.ValorDiferimentoEstadual = ValorDiferimentoEstadual
        self.validate_tpValor(self.ValorDiferimentoEstadual)
        self.ValorDiferimentoEstadual_nsprefix_ = None
        self.ValorPercDiferimentoMunicipal = ValorPercDiferimentoMunicipal
        self.validate_tpValor(self.ValorPercDiferimentoMunicipal)
        self.ValorPercDiferimentoMunicipal_nsprefix_ = None
        self.ValorDiferimentoMunicipal = ValorDiferimentoMunicipal
        self.validate_tpValor(self.ValorDiferimentoMunicipal)
        self.ValorDiferimentoMunicipal_nsprefix_ = None
        self.ValorPercDiferimentoCBS = ValorPercDiferimentoCBS
        self.validate_tpValor(self.ValorPercDiferimentoCBS)
        self.ValorPercDiferimentoCBS_nsprefix_ = None
        self.ValorDiferimentoCBS = ValorDiferimentoCBS
        self.validate_tpValor(self.ValorDiferimentoCBS)
        self.ValorDiferimentoCBS_nsprefix_ = None
        self.CodigoClassCredPresumidoIBS = CodigoClassCredPresumidoIBS
        self.validate_tpValor(self.CodigoClassCredPresumidoIBS)
        self.CodigoClassCredPresumidoIBS_nsprefix_ = None
        self.ValorPercCredPresumidoIBS = ValorPercCredPresumidoIBS
        self.validate_tpValor(self.ValorPercCredPresumidoIBS)
        self.ValorPercCredPresumidoIBS_nsprefix_ = None
        self.ValorCredPresumidoIBS = ValorCredPresumidoIBS
        self.validate_tpValor(self.ValorCredPresumidoIBS)
        self.ValorCredPresumidoIBS_nsprefix_ = None
        self.CodigoClassCredPresumidoCBS = CodigoClassCredPresumidoCBS
        self.validate_tpValor(self.CodigoClassCredPresumidoCBS)
        self.CodigoClassCredPresumidoCBS_nsprefix_ = None
        self.ValorPercCredPresumidoCBS = ValorPercCredPresumidoCBS
        self.validate_tpValor(self.ValorPercCredPresumidoCBS)
        self.ValorPercCredPresumidoCBS_nsprefix_ = None
        self.ValorCredPresumidoCBS = ValorCredPresumidoCBS
        self.validate_tpValor(self.ValorCredPresumidoCBS)
        self.ValorCredPresumidoCBS_nsprefix_ = None
        self.ValorAliqEstadualRegularIBS = ValorAliqEstadualRegularIBS
        self.validate_tpValor(self.ValorAliqEstadualRegularIBS)
        self.ValorAliqEstadualRegularIBS_nsprefix_ = None
        self.ValorAliqMunicipalRegularIBS = ValorAliqMunicipalRegularIBS
        self.validate_tpValor(self.ValorAliqMunicipalRegularIBS)
        self.ValorAliqMunicipalRegularIBS_nsprefix_ = None
        self.ValorAliqRegularCBS = ValorAliqRegularCBS
        self.validate_tpValor(self.ValorAliqRegularCBS)
        self.ValorAliqRegularCBS_nsprefix_ = None
        self.ValorEstadualRegularIBS = ValorEstadualRegularIBS
        self.validate_tpValor(self.ValorEstadualRegularIBS)
        self.ValorEstadualRegularIBS_nsprefix_ = None
        self.ValorMunicipalRegularIBS = ValorMunicipalRegularIBS
        self.validate_tpValor(self.ValorMunicipalRegularIBS)
        self.ValorMunicipalRegularIBS_nsprefix_ = None
        self.ValorRegularCBS = ValorRegularCBS
        self.validate_tpValor(self.ValorRegularCBS)
        self.ValorRegularCBS_nsprefix_ = None
        self.ValorTotalReeRepRes = ValorTotalReeRepRes
        self.validate_tpValor(self.ValorTotalReeRepRes)
        self.ValorTotalReeRepRes_nsprefix_ = None
        self.ValorAliqEstadualIBSCompraGov = ValorAliqEstadualIBSCompraGov
        self.validate_tpValor(self.ValorAliqEstadualIBSCompraGov)
        self.ValorAliqEstadualIBSCompraGov_nsprefix_ = None
        self.ValorEstadualBSCompraGov = ValorEstadualBSCompraGov
        self.validate_tpValor(self.ValorEstadualBSCompraGov)
        self.ValorEstadualBSCompraGov_nsprefix_ = None
        self.ValorAliqMunicipalIBSCompraGov = ValorAliqMunicipalIBSCompraGov
        self.validate_tpValor(self.ValorAliqMunicipalIBSCompraGov)
        self.ValorAliqMunicipalIBSCompraGov_nsprefix_ = None
        self.ValorMunicipalIBSCompraGov = ValorMunicipalIBSCompraGov
        self.validate_tpValor(self.ValorMunicipalIBSCompraGov)
        self.ValorMunicipalIBSCompraGov_nsprefix_ = None
        self.ValorAliqCBSCompraGov = ValorAliqCBSCompraGov
        self.validate_tpValor(self.ValorAliqCBSCompraGov)
        self.ValorAliqCBSCompraGov_nsprefix_ = None
        self.ValorCBSCompraGov = ValorCBSCompraGov
        self.validate_tpValor(self.ValorCBSCompraGov)
        self.ValorCBSCompraGov_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpRetornoComplementarIBSCBS)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpRetornoComplementarIBSCBS.subclass:
            return tpRetornoComplementarIBSCBS.subclass(*args_, **kwargs_)
        else:
            return tpRetornoComplementarIBSCBS(*args_, **kwargs_)
    factory = staticmethod(factory)
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
    def has__content(self):
        if (
            self.Adquirente is not None or
            self.ValorBCIBSCBS is not None or
            self.ValorAliqEstadualIBS is not None or
            self.ValorPercRedEstadualIBS is not None or
            self.ValorAliqEfetivaEstadualIBS is not None or
            self.ValorEstadualIBS is not None or
            self.ValorAliqMunicipalIBS is not None or
            self.ValorPercRedMunicipalIBS is not None or
            self.ValorAliqEfetivaMunicipalIBS is not None or
            self.ValorMunicipalIBS is not None or
            self.ValorIBS is not None or
            self.ValorAliqCBS is not None or
            self.ValorPercRedCBS is not None or
            self.ValorAliqEfetivaCBS is not None or
            self.ValorCBS is not None or
            self.ValorPercDiferimentoEstadual is not None or
            self.ValorDiferimentoEstadual is not None or
            self.ValorPercDiferimentoMunicipal is not None or
            self.ValorDiferimentoMunicipal is not None or
            self.ValorPercDiferimentoCBS is not None or
            self.ValorDiferimentoCBS is not None or
            self.CodigoClassCredPresumidoIBS is not None or
            self.ValorPercCredPresumidoIBS is not None or
            self.ValorCredPresumidoIBS is not None or
            self.CodigoClassCredPresumidoCBS is not None or
            self.ValorPercCredPresumidoCBS is not None or
            self.ValorCredPresumidoCBS is not None or
            self.ValorAliqEstadualRegularIBS is not None or
            self.ValorAliqMunicipalRegularIBS is not None or
            self.ValorAliqRegularCBS is not None or
            self.ValorEstadualRegularIBS is not None or
            self.ValorMunicipalRegularIBS is not None or
            self.ValorRegularCBS is not None or
            self.ValorTotalReeRepRes is not None or
            self.ValorAliqEstadualIBSCompraGov is not None or
            self.ValorEstadualBSCompraGov is not None or
            self.ValorAliqMunicipalIBSCompraGov is not None or
            self.ValorMunicipalIBSCompraGov is not None or
            self.ValorAliqCBSCompraGov is not None or
            self.ValorCBSCompraGov is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpRetornoComplementarIBSCBS', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpRetornoComplementarIBSCBS')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpRetornoComplementarIBSCBS':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpRetornoComplementarIBSCBS')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpRetornoComplementarIBSCBS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpRetornoComplementarIBSCBS'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpRetornoComplementarIBSCBS', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Adquirente is not None:
            namespaceprefix_ = self.Adquirente_nsprefix_ + ':' if (UseCapturedNS_ and self.Adquirente_nsprefix_) else ''
            self.Adquirente.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Adquirente', pretty_print=pretty_print)
        if self.ValorBCIBSCBS is not None:
            namespaceprefix_ = self.ValorBCIBSCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorBCIBSCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorBCIBSCBS>%s</%sValorBCIBSCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorBCIBSCBS, input_name='ValorBCIBSCBS'), namespaceprefix_ , eol_))
        if self.ValorAliqEstadualIBS is not None:
            namespaceprefix_ = self.ValorAliqEstadualIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqEstadualIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqEstadualIBS>%s</%sValorAliqEstadualIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqEstadualIBS, input_name='ValorAliqEstadualIBS'), namespaceprefix_ , eol_))
        if self.ValorPercRedEstadualIBS is not None:
            namespaceprefix_ = self.ValorPercRedEstadualIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPercRedEstadualIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPercRedEstadualIBS>%s</%sValorPercRedEstadualIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorPercRedEstadualIBS, input_name='ValorPercRedEstadualIBS'), namespaceprefix_ , eol_))
        if self.ValorAliqEfetivaEstadualIBS is not None:
            namespaceprefix_ = self.ValorAliqEfetivaEstadualIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqEfetivaEstadualIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqEfetivaEstadualIBS>%s</%sValorAliqEfetivaEstadualIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqEfetivaEstadualIBS, input_name='ValorAliqEfetivaEstadualIBS'), namespaceprefix_ , eol_))
        if self.ValorEstadualIBS is not None:
            namespaceprefix_ = self.ValorEstadualIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorEstadualIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorEstadualIBS>%s</%sValorEstadualIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorEstadualIBS, input_name='ValorEstadualIBS'), namespaceprefix_ , eol_))
        if self.ValorAliqMunicipalIBS is not None:
            namespaceprefix_ = self.ValorAliqMunicipalIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqMunicipalIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqMunicipalIBS>%s</%sValorAliqMunicipalIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqMunicipalIBS, input_name='ValorAliqMunicipalIBS'), namespaceprefix_ , eol_))
        if self.ValorPercRedMunicipalIBS is not None:
            namespaceprefix_ = self.ValorPercRedMunicipalIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPercRedMunicipalIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPercRedMunicipalIBS>%s</%sValorPercRedMunicipalIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorPercRedMunicipalIBS, input_name='ValorPercRedMunicipalIBS'), namespaceprefix_ , eol_))
        if self.ValorAliqEfetivaMunicipalIBS is not None:
            namespaceprefix_ = self.ValorAliqEfetivaMunicipalIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqEfetivaMunicipalIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqEfetivaMunicipalIBS>%s</%sValorAliqEfetivaMunicipalIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqEfetivaMunicipalIBS, input_name='ValorAliqEfetivaMunicipalIBS'), namespaceprefix_ , eol_))
        if self.ValorMunicipalIBS is not None:
            namespaceprefix_ = self.ValorMunicipalIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorMunicipalIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorMunicipalIBS>%s</%sValorMunicipalIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorMunicipalIBS, input_name='ValorMunicipalIBS'), namespaceprefix_ , eol_))
        if self.ValorIBS is not None:
            namespaceprefix_ = self.ValorIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorIBS>%s</%sValorIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorIBS, input_name='ValorIBS'), namespaceprefix_ , eol_))
        if self.ValorAliqCBS is not None:
            namespaceprefix_ = self.ValorAliqCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqCBS>%s</%sValorAliqCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqCBS, input_name='ValorAliqCBS'), namespaceprefix_ , eol_))
        if self.ValorPercRedCBS is not None:
            namespaceprefix_ = self.ValorPercRedCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPercRedCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPercRedCBS>%s</%sValorPercRedCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorPercRedCBS, input_name='ValorPercRedCBS'), namespaceprefix_ , eol_))
        if self.ValorAliqEfetivaCBS is not None:
            namespaceprefix_ = self.ValorAliqEfetivaCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqEfetivaCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqEfetivaCBS>%s</%sValorAliqEfetivaCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqEfetivaCBS, input_name='ValorAliqEfetivaCBS'), namespaceprefix_ , eol_))
        if self.ValorCBS is not None:
            namespaceprefix_ = self.ValorCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCBS>%s</%sValorCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCBS, input_name='ValorCBS'), namespaceprefix_ , eol_))
        if self.ValorPercDiferimentoEstadual is not None:
            namespaceprefix_ = self.ValorPercDiferimentoEstadual_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPercDiferimentoEstadual_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPercDiferimentoEstadual>%s</%sValorPercDiferimentoEstadual>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorPercDiferimentoEstadual, input_name='ValorPercDiferimentoEstadual'), namespaceprefix_ , eol_))
        if self.ValorDiferimentoEstadual is not None:
            namespaceprefix_ = self.ValorDiferimentoEstadual_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorDiferimentoEstadual_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorDiferimentoEstadual>%s</%sValorDiferimentoEstadual>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorDiferimentoEstadual, input_name='ValorDiferimentoEstadual'), namespaceprefix_ , eol_))
        if self.ValorPercDiferimentoMunicipal is not None:
            namespaceprefix_ = self.ValorPercDiferimentoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPercDiferimentoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPercDiferimentoMunicipal>%s</%sValorPercDiferimentoMunicipal>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorPercDiferimentoMunicipal, input_name='ValorPercDiferimentoMunicipal'), namespaceprefix_ , eol_))
        if self.ValorDiferimentoMunicipal is not None:
            namespaceprefix_ = self.ValorDiferimentoMunicipal_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorDiferimentoMunicipal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorDiferimentoMunicipal>%s</%sValorDiferimentoMunicipal>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorDiferimentoMunicipal, input_name='ValorDiferimentoMunicipal'), namespaceprefix_ , eol_))
        if self.ValorPercDiferimentoCBS is not None:
            namespaceprefix_ = self.ValorPercDiferimentoCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPercDiferimentoCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPercDiferimentoCBS>%s</%sValorPercDiferimentoCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorPercDiferimentoCBS, input_name='ValorPercDiferimentoCBS'), namespaceprefix_ , eol_))
        if self.ValorDiferimentoCBS is not None:
            namespaceprefix_ = self.ValorDiferimentoCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorDiferimentoCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorDiferimentoCBS>%s</%sValorDiferimentoCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorDiferimentoCBS, input_name='ValorDiferimentoCBS'), namespaceprefix_ , eol_))
        if self.CodigoClassCredPresumidoIBS is not None:
            namespaceprefix_ = self.CodigoClassCredPresumidoIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoClassCredPresumidoIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoClassCredPresumidoIBS>%s</%sCodigoClassCredPresumidoIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.CodigoClassCredPresumidoIBS, input_name='CodigoClassCredPresumidoIBS'), namespaceprefix_ , eol_))
        if self.ValorPercCredPresumidoIBS is not None:
            namespaceprefix_ = self.ValorPercCredPresumidoIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPercCredPresumidoIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPercCredPresumidoIBS>%s</%sValorPercCredPresumidoIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorPercCredPresumidoIBS, input_name='ValorPercCredPresumidoIBS'), namespaceprefix_ , eol_))
        if self.ValorCredPresumidoIBS is not None:
            namespaceprefix_ = self.ValorCredPresumidoIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCredPresumidoIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCredPresumidoIBS>%s</%sValorCredPresumidoIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCredPresumidoIBS, input_name='ValorCredPresumidoIBS'), namespaceprefix_ , eol_))
        if self.CodigoClassCredPresumidoCBS is not None:
            namespaceprefix_ = self.CodigoClassCredPresumidoCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.CodigoClassCredPresumidoCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCodigoClassCredPresumidoCBS>%s</%sCodigoClassCredPresumidoCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.CodigoClassCredPresumidoCBS, input_name='CodigoClassCredPresumidoCBS'), namespaceprefix_ , eol_))
        if self.ValorPercCredPresumidoCBS is not None:
            namespaceprefix_ = self.ValorPercCredPresumidoCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorPercCredPresumidoCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorPercCredPresumidoCBS>%s</%sValorPercCredPresumidoCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorPercCredPresumidoCBS, input_name='ValorPercCredPresumidoCBS'), namespaceprefix_ , eol_))
        if self.ValorCredPresumidoCBS is not None:
            namespaceprefix_ = self.ValorCredPresumidoCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCredPresumidoCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCredPresumidoCBS>%s</%sValorCredPresumidoCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCredPresumidoCBS, input_name='ValorCredPresumidoCBS'), namespaceprefix_ , eol_))
        if self.ValorAliqEstadualRegularIBS is not None:
            namespaceprefix_ = self.ValorAliqEstadualRegularIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqEstadualRegularIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqEstadualRegularIBS>%s</%sValorAliqEstadualRegularIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqEstadualRegularIBS, input_name='ValorAliqEstadualRegularIBS'), namespaceprefix_ , eol_))
        if self.ValorAliqMunicipalRegularIBS is not None:
            namespaceprefix_ = self.ValorAliqMunicipalRegularIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqMunicipalRegularIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqMunicipalRegularIBS>%s</%sValorAliqMunicipalRegularIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqMunicipalRegularIBS, input_name='ValorAliqMunicipalRegularIBS'), namespaceprefix_ , eol_))
        if self.ValorAliqRegularCBS is not None:
            namespaceprefix_ = self.ValorAliqRegularCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqRegularCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqRegularCBS>%s</%sValorAliqRegularCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqRegularCBS, input_name='ValorAliqRegularCBS'), namespaceprefix_ , eol_))
        if self.ValorEstadualRegularIBS is not None:
            namespaceprefix_ = self.ValorEstadualRegularIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorEstadualRegularIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorEstadualRegularIBS>%s</%sValorEstadualRegularIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorEstadualRegularIBS, input_name='ValorEstadualRegularIBS'), namespaceprefix_ , eol_))
        if self.ValorMunicipalRegularIBS is not None:
            namespaceprefix_ = self.ValorMunicipalRegularIBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorMunicipalRegularIBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorMunicipalRegularIBS>%s</%sValorMunicipalRegularIBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorMunicipalRegularIBS, input_name='ValorMunicipalRegularIBS'), namespaceprefix_ , eol_))
        if self.ValorRegularCBS is not None:
            namespaceprefix_ = self.ValorRegularCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorRegularCBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorRegularCBS>%s</%sValorRegularCBS>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorRegularCBS, input_name='ValorRegularCBS'), namespaceprefix_ , eol_))
        if self.ValorTotalReeRepRes is not None:
            namespaceprefix_ = self.ValorTotalReeRepRes_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorTotalReeRepRes_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorTotalReeRepRes>%s</%sValorTotalReeRepRes>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorTotalReeRepRes, input_name='ValorTotalReeRepRes'), namespaceprefix_ , eol_))
        if self.ValorAliqEstadualIBSCompraGov is not None:
            namespaceprefix_ = self.ValorAliqEstadualIBSCompraGov_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqEstadualIBSCompraGov_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqEstadualIBSCompraGov>%s</%sValorAliqEstadualIBSCompraGov>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqEstadualIBSCompraGov, input_name='ValorAliqEstadualIBSCompraGov'), namespaceprefix_ , eol_))
        if self.ValorEstadualBSCompraGov is not None:
            namespaceprefix_ = self.ValorEstadualBSCompraGov_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorEstadualBSCompraGov_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorEstadualBSCompraGov>%s</%sValorEstadualBSCompraGov>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorEstadualBSCompraGov, input_name='ValorEstadualBSCompraGov'), namespaceprefix_ , eol_))
        if self.ValorAliqMunicipalIBSCompraGov is not None:
            namespaceprefix_ = self.ValorAliqMunicipalIBSCompraGov_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqMunicipalIBSCompraGov_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqMunicipalIBSCompraGov>%s</%sValorAliqMunicipalIBSCompraGov>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqMunicipalIBSCompraGov, input_name='ValorAliqMunicipalIBSCompraGov'), namespaceprefix_ , eol_))
        if self.ValorMunicipalIBSCompraGov is not None:
            namespaceprefix_ = self.ValorMunicipalIBSCompraGov_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorMunicipalIBSCompraGov_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorMunicipalIBSCompraGov>%s</%sValorMunicipalIBSCompraGov>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorMunicipalIBSCompraGov, input_name='ValorMunicipalIBSCompraGov'), namespaceprefix_ , eol_))
        if self.ValorAliqCBSCompraGov is not None:
            namespaceprefix_ = self.ValorAliqCBSCompraGov_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorAliqCBSCompraGov_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorAliqCBSCompraGov>%s</%sValorAliqCBSCompraGov>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorAliqCBSCompraGov, input_name='ValorAliqCBSCompraGov'), namespaceprefix_ , eol_))
        if self.ValorCBSCompraGov is not None:
            namespaceprefix_ = self.ValorCBSCompraGov_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorCBSCompraGov_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorCBSCompraGov>%s</%sValorCBSCompraGov>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorCBSCompraGov, input_name='ValorCBSCompraGov'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Adquirente':
            obj_ = tpInformacoesPessoa.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Adquirente = obj_
            obj_.original_tagname_ = 'Adquirente'
        elif nodeName_ == 'ValorBCIBSCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorBCIBSCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorBCIBSCBS')
            self.ValorBCIBSCBS = fval_
            self.ValorBCIBSCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorBCIBSCBS)
        elif nodeName_ == 'ValorAliqEstadualIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqEstadualIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqEstadualIBS')
            self.ValorAliqEstadualIBS = fval_
            self.ValorAliqEstadualIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqEstadualIBS)
        elif nodeName_ == 'ValorPercRedEstadualIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorPercRedEstadualIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorPercRedEstadualIBS')
            self.ValorPercRedEstadualIBS = fval_
            self.ValorPercRedEstadualIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorPercRedEstadualIBS)
        elif nodeName_ == 'ValorAliqEfetivaEstadualIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqEfetivaEstadualIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqEfetivaEstadualIBS')
            self.ValorAliqEfetivaEstadualIBS = fval_
            self.ValorAliqEfetivaEstadualIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqEfetivaEstadualIBS)
        elif nodeName_ == 'ValorEstadualIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorEstadualIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorEstadualIBS')
            self.ValorEstadualIBS = fval_
            self.ValorEstadualIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorEstadualIBS)
        elif nodeName_ == 'ValorAliqMunicipalIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqMunicipalIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqMunicipalIBS')
            self.ValorAliqMunicipalIBS = fval_
            self.ValorAliqMunicipalIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqMunicipalIBS)
        elif nodeName_ == 'ValorPercRedMunicipalIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorPercRedMunicipalIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorPercRedMunicipalIBS')
            self.ValorPercRedMunicipalIBS = fval_
            self.ValorPercRedMunicipalIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorPercRedMunicipalIBS)
        elif nodeName_ == 'ValorAliqEfetivaMunicipalIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqEfetivaMunicipalIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqEfetivaMunicipalIBS')
            self.ValorAliqEfetivaMunicipalIBS = fval_
            self.ValorAliqEfetivaMunicipalIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqEfetivaMunicipalIBS)
        elif nodeName_ == 'ValorMunicipalIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorMunicipalIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorMunicipalIBS')
            self.ValorMunicipalIBS = fval_
            self.ValorMunicipalIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorMunicipalIBS)
        elif nodeName_ == 'ValorIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorIBS')
            self.ValorIBS = fval_
            self.ValorIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorIBS)
        elif nodeName_ == 'ValorAliqCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqCBS')
            self.ValorAliqCBS = fval_
            self.ValorAliqCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqCBS)
        elif nodeName_ == 'ValorPercRedCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorPercRedCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorPercRedCBS')
            self.ValorPercRedCBS = fval_
            self.ValorPercRedCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorPercRedCBS)
        elif nodeName_ == 'ValorAliqEfetivaCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqEfetivaCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqEfetivaCBS')
            self.ValorAliqEfetivaCBS = fval_
            self.ValorAliqEfetivaCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqEfetivaCBS)
        elif nodeName_ == 'ValorCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCBS')
            self.ValorCBS = fval_
            self.ValorCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorCBS)
        elif nodeName_ == 'ValorPercDiferimentoEstadual' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorPercDiferimentoEstadual')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorPercDiferimentoEstadual')
            self.ValorPercDiferimentoEstadual = fval_
            self.ValorPercDiferimentoEstadual_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorPercDiferimentoEstadual)
        elif nodeName_ == 'ValorDiferimentoEstadual' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorDiferimentoEstadual')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorDiferimentoEstadual')
            self.ValorDiferimentoEstadual = fval_
            self.ValorDiferimentoEstadual_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorDiferimentoEstadual)
        elif nodeName_ == 'ValorPercDiferimentoMunicipal' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorPercDiferimentoMunicipal')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorPercDiferimentoMunicipal')
            self.ValorPercDiferimentoMunicipal = fval_
            self.ValorPercDiferimentoMunicipal_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorPercDiferimentoMunicipal)
        elif nodeName_ == 'ValorDiferimentoMunicipal' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorDiferimentoMunicipal')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorDiferimentoMunicipal')
            self.ValorDiferimentoMunicipal = fval_
            self.ValorDiferimentoMunicipal_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorDiferimentoMunicipal)
        elif nodeName_ == 'ValorPercDiferimentoCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorPercDiferimentoCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorPercDiferimentoCBS')
            self.ValorPercDiferimentoCBS = fval_
            self.ValorPercDiferimentoCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorPercDiferimentoCBS)
        elif nodeName_ == 'ValorDiferimentoCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorDiferimentoCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorDiferimentoCBS')
            self.ValorDiferimentoCBS = fval_
            self.ValorDiferimentoCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorDiferimentoCBS)
        elif nodeName_ == 'CodigoClassCredPresumidoIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'CodigoClassCredPresumidoIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'CodigoClassCredPresumidoIBS')
            self.CodigoClassCredPresumidoIBS = fval_
            self.CodigoClassCredPresumidoIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.CodigoClassCredPresumidoIBS)
        elif nodeName_ == 'ValorPercCredPresumidoIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorPercCredPresumidoIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorPercCredPresumidoIBS')
            self.ValorPercCredPresumidoIBS = fval_
            self.ValorPercCredPresumidoIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorPercCredPresumidoIBS)
        elif nodeName_ == 'ValorCredPresumidoIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCredPresumidoIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCredPresumidoIBS')
            self.ValorCredPresumidoIBS = fval_
            self.ValorCredPresumidoIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorCredPresumidoIBS)
        elif nodeName_ == 'CodigoClassCredPresumidoCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'CodigoClassCredPresumidoCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'CodigoClassCredPresumidoCBS')
            self.CodigoClassCredPresumidoCBS = fval_
            self.CodigoClassCredPresumidoCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.CodigoClassCredPresumidoCBS)
        elif nodeName_ == 'ValorPercCredPresumidoCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorPercCredPresumidoCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorPercCredPresumidoCBS')
            self.ValorPercCredPresumidoCBS = fval_
            self.ValorPercCredPresumidoCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorPercCredPresumidoCBS)
        elif nodeName_ == 'ValorCredPresumidoCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCredPresumidoCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCredPresumidoCBS')
            self.ValorCredPresumidoCBS = fval_
            self.ValorCredPresumidoCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorCredPresumidoCBS)
        elif nodeName_ == 'ValorAliqEstadualRegularIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqEstadualRegularIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqEstadualRegularIBS')
            self.ValorAliqEstadualRegularIBS = fval_
            self.ValorAliqEstadualRegularIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqEstadualRegularIBS)
        elif nodeName_ == 'ValorAliqMunicipalRegularIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqMunicipalRegularIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqMunicipalRegularIBS')
            self.ValorAliqMunicipalRegularIBS = fval_
            self.ValorAliqMunicipalRegularIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqMunicipalRegularIBS)
        elif nodeName_ == 'ValorAliqRegularCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqRegularCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqRegularCBS')
            self.ValorAliqRegularCBS = fval_
            self.ValorAliqRegularCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqRegularCBS)
        elif nodeName_ == 'ValorEstadualRegularIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorEstadualRegularIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorEstadualRegularIBS')
            self.ValorEstadualRegularIBS = fval_
            self.ValorEstadualRegularIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorEstadualRegularIBS)
        elif nodeName_ == 'ValorMunicipalRegularIBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorMunicipalRegularIBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorMunicipalRegularIBS')
            self.ValorMunicipalRegularIBS = fval_
            self.ValorMunicipalRegularIBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorMunicipalRegularIBS)
        elif nodeName_ == 'ValorRegularCBS' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorRegularCBS')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorRegularCBS')
            self.ValorRegularCBS = fval_
            self.ValorRegularCBS_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorRegularCBS)
        elif nodeName_ == 'ValorTotalReeRepRes' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorTotalReeRepRes')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorTotalReeRepRes')
            self.ValorTotalReeRepRes = fval_
            self.ValorTotalReeRepRes_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorTotalReeRepRes)
        elif nodeName_ == 'ValorAliqEstadualIBSCompraGov' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqEstadualIBSCompraGov')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqEstadualIBSCompraGov')
            self.ValorAliqEstadualIBSCompraGov = fval_
            self.ValorAliqEstadualIBSCompraGov_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqEstadualIBSCompraGov)
        elif nodeName_ == 'ValorEstadualBSCompraGov' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorEstadualBSCompraGov')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorEstadualBSCompraGov')
            self.ValorEstadualBSCompraGov = fval_
            self.ValorEstadualBSCompraGov_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorEstadualBSCompraGov)
        elif nodeName_ == 'ValorAliqMunicipalIBSCompraGov' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqMunicipalIBSCompraGov')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqMunicipalIBSCompraGov')
            self.ValorAliqMunicipalIBSCompraGov = fval_
            self.ValorAliqMunicipalIBSCompraGov_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqMunicipalIBSCompraGov)
        elif nodeName_ == 'ValorMunicipalIBSCompraGov' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorMunicipalIBSCompraGov')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorMunicipalIBSCompraGov')
            self.ValorMunicipalIBSCompraGov = fval_
            self.ValorMunicipalIBSCompraGov_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorMunicipalIBSCompraGov)
        elif nodeName_ == 'ValorAliqCBSCompraGov' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorAliqCBSCompraGov')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorAliqCBSCompraGov')
            self.ValorAliqCBSCompraGov = fval_
            self.ValorAliqCBSCompraGov_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorAliqCBSCompraGov)
        elif nodeName_ == 'ValorCBSCompraGov' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorCBSCompraGov')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorCBSCompraGov')
            self.ValorCBSCompraGov = fval_
            self.ValorCBSCompraGov_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorCBSCompraGov)
# end class tpRetornoComplementarIBSCBS


class tpTrib(GeneratedsSuper):
    """tpTrib -- Informa
    ç
    õ
    es relacionadas aos tributos IBS e
    à
    CBS.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('gIBSCBS', 'tpGIBSCBS', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'gIBSCBS', 'type': 'tpGIBSCBS'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, gIBSCBS=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.gIBSCBS = gIBSCBS
        self.gIBSCBS_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpTrib)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpTrib.subclass:
            return tpTrib.subclass(*args_, **kwargs_)
        else:
            return tpTrib(*args_, **kwargs_)
    factory = staticmethod(factory)
    def has__content(self):
        if (
            self.gIBSCBS is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpTrib', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpTrib')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpTrib':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpTrib')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpTrib', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpTrib'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpTrib', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.gIBSCBS is not None:
            namespaceprefix_ = self.gIBSCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.gIBSCBS_nsprefix_) else ''
            self.gIBSCBS.export(outfile, level, namespaceprefix_, namespacedef_='', name_='gIBSCBS', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'gIBSCBS':
            obj_ = tpGIBSCBS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.gIBSCBS = obj_
            obj_.original_tagname_ = 'gIBSCBS'
# end class tpTrib


class tpValores(GeneratedsSuper):
    """tpValores -- Informa
    ç
    õ
    es relacionadas aos valores do servi
    ç
    o prestado para IBS e
    à
    CBS.
    gReeRepRes -- Grupo de informa
    ç
    õ
    es relativas a valores inclu
    í
    dos neste documento e recebidos por
    motivo de estarem relacionadas a opera
    ç
    õ
    es de terceiros, objeto de reembolso, repasse ou
    ressarcimento pelo recebedor, j
    á
    tributados e aqui referenciados.
    trib -- Grupo de informa
    ç
    õ
    es relacionados aos tributos IBS e CBS.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('gReeRepRes', 'tpGrupoReeRepRes', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'gReeRepRes', 'type': 'tpGrupoReeRepRes'}, None),
        MemberSpec_('trib', 'tpTrib', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'trib', 'type': 'tpTrib'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, gReeRepRes=None, trib=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.gReeRepRes = gReeRepRes
        self.gReeRepRes_nsprefix_ = None
        self.trib = trib
        self.trib_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tpValores)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tpValores.subclass:
            return tpValores.subclass(*args_, **kwargs_)
        else:
            return tpValores(*args_, **kwargs_)
    factory = staticmethod(factory)
    def has__content(self):
        if (
            self.gReeRepRes is not None or
            self.trib is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpValores', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tpValores')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'tpValores':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpValores')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpValores', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpValores'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpValores', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.gReeRepRes is not None:
            namespaceprefix_ = self.gReeRepRes_nsprefix_ + ':' if (UseCapturedNS_ and self.gReeRepRes_nsprefix_) else ''
            self.gReeRepRes.export(outfile, level, namespaceprefix_, namespacedef_='', name_='gReeRepRes', pretty_print=pretty_print)
        if self.trib is not None:
            namespaceprefix_ = self.trib_nsprefix_ + ':' if (UseCapturedNS_ and self.trib_nsprefix_) else ''
            self.trib.export(outfile, level, namespaceprefix_, namespacedef_='', name_='trib', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'gReeRepRes':
            obj_ = tpGrupoReeRepRes.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.gReeRepRes = obj_
            obj_.original_tagname_ = 'gReeRepRes'
        elif nodeName_ == 'trib':
            obj_ = tpTrib.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.trib = obj_
            obj_.original_tagname_ = 'trib'
# end class tpValores


class tpNFe(GeneratedsSuper):
    """tpNFe -- Tipo que representa uma NFS-e
    Assinatura -- Assinatura digital da NFS-e.
    ChaveNFe -- Chave de identifica
    ç
    ã
    o da NFS-e.
    DataEmissaoNFe -- Data de emiss
    ã
    o da NFS-e
    NumeroLote -- N
    ú
    mero de lote gerador da NFS-e.
    ChaveRPS -- Chave do RPS que originou a NFS-e.
    TipoRPS -- Tipo do RPS emitido.
    DataEmissaoRPS -- Data de emiss
    ã
    o do RPS que originou a NFS-e.
    DataFatoGeradorNFe -- Data do fato gerador da NFS-e.
    CPFCNPJPrestador -- CPF/CNPJ do Prestador do servi
    ç
    o.
    RazaoSocialPrestador -- Nome/Raz
    ã
    o Social do Prestador.
    EnderecoPrestador -- Endere
    ç
    o do Prestador.
    EmailPrestador -- E-mail do Prestador.
    StatusNFe -- Status da NFS-e.
    DataCancelamento -- Data de cancelamento da NFS-e.
    TributacaoNFe -- Tributa
    ç
    ã
    o da NFS-e.
    OpcaoSimples -- Op
    ç
    ã
    o pelo Simples.
    NumeroGuia -- N
    ú
    mero da guia vinculada a NFS-e.
    DataQuitacaoGuia -- Data de quita
    ç
    ã
    o da guia vinculada a NFS-e.
    ValorServicos -- Valor dos servi
    ç
    os prestados.
    ValorDeducoes -- Valor das dedu
    ç
    õ
    es.
    ValorPIS -- Valor da reten
    ç
    ã
    o do PIS.
    ValorCOFINS -- Valor da reten
    ç
    ã
    o do COFINS.
    ValorINSS -- Valor da reten
    ç
    ã
    o do INSS.
    ValorIR -- Valor da reten
    ç
    ã
    o do IR.
    ValorCSLL -- Valor da reten
    ç
    ã
    o do CSLL.
    CodigoServico -- C
    ó
    digo do servi
    ç
    o.
    AliquotaServicos -- Valor da al
    í
    quota.
    ValorISS -- Valor do ISS.
    ValorCredito -- Valor do cr
    é
    dito gerado.
    ISSRetido -- Reten
    ç
    ã
    o do ISS.
    CPFCNPJTomador -- CPF/CNPJ do tomador do servi
    ç
    o.
    InscricaoMunicipalTomador -- Inscri
    ç
    ã
    o Municipal do Tomador.
    InscricaoEstadualTomador -- Inscri
    ç
    ã
    o Estadual do tomador.
    RazaoSocialTomador -- Nome/Raz
    ã
    o Social do tomador.
    EnderecoTomador -- Endere
    ç
    o do tomador.
    EmailTomador -- E-mail do tomador.
    CPFCNPJIntermediario -- CNPJ do intermedi
    á
    rio de servi
    ç
    o.
    InscricaoMunicipalIntermediario -- Inscri
    ç
    ã
    o Municipal do intermedi
    á
    rio de servi
    ç
    o.
    ISSRetidoIntermediario -- Reten
    ç
    ã
    o do ISS pelo intermedi
    á
    rio de servi
    ç
    o.
    EmailIntermediario -- E-mail do intermedi
    á
    rio de servi
    ç
    o.
    Discriminacao -- Descri
    ç
    ã
    o dos servi
    ç
    os.
    ValorCargaTributaria -- Valor da carga tribut
    á
    ria total em R$.
    PercentualCargaTributaria -- Valor percentual da carga tribut
    á
    ria.
    FonteCargaTributaria -- Fonte de informa
    ç
    ã
    o da carga tribut
    á
    ria.
    CodigoCEI -- C
    ó
    digo do CEI - Cadastro espec
    í
    fico do INSS.
    MatriculaObra -- C
    ó
    digo que representa a matr
    í
    cula da obra no sistema de cadastro de obras.
    MunicipioPrestacao -- C
    ó
    digo da cidade do munic
    í
    pio da presta
    ç
    ã
    o do servi
    ç
    o.
    NumeroEncapsulamento -- C
    ó
    digo que representa o n
    ú
    mero do encapsulamento da obra.
    ValorTotalRecebido -- Valor do total recebido.
    ValorInicialCobrado -- Valor inicial cobrado pela presta
    ç
    ã
    o do servi
    ç
    o, antes de tributos, multa e juros.
    "Valor dos servi
    ç
    os antes dos tributos". Corresponde ao valor cobrado pela presta
    ç
    ã
    o do servi
    ç
    o, antes de tributos, multa e juros.
    Informado para realizar o c
    á
    lculo dos tributos do in
    í
    cio para o fim.
    ValorFinalCobrado -- Valor final cobrado pela presta
    ç
    ã
    o do servi
    ç
    o, incluindo todos os tributos.
    "Valor total na nota". Corresponde ao valor final cobrado pela presta
    ç
    ã
    o do servi
    ç
    o, incluindo todos os tributos, multa e juros.
    Informado para realizar o c
    á
    lculo dos impostos do fim para o in
    í
    cio.
    ValorMulta -- Valor da multa.
    ValorJuros -- Valor dos juros.
    ValorIPI -- Valor de IPI.
    ExigibilidadeSuspensa -- Indica se
    é
    uma emiss
    ã
    o com exigibilidade suspensa.
    PagamentoParceladoAntecipado -- Indica de nota fiscal de pagamento parcelado antecipado (realizado antes do fornecimento).
    NCM -- Informe o n
    ú
    mero NCM (Nomenclatura Comum do Mercosul).
    NBS -- Informe o n
    ú
    mero NBS (Nomenclatura Brasileira de Servi
    ç
    os).
    atvEvento -- Informa
    ç
    õ
    es dos Tipos de evento.
    IBSCBS -- Informa
    ç
    õ
    es declaradas pelo emitente referentes ao IBS e
    à
    CBS.
    RetornoComplementarIBSCBS -- Informa
    ç
    õ
    es complementares referentes ao IBS e
    à
    CBS.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Assinatura', ['tpAssinatura', 'xs:base64Binary'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Assinatura', 'type': 'xs:base64Binary'}, None),
        MemberSpec_('ChaveNFe', 'tpChaveNFe', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ChaveNFe', 'type': 'tpChaveNFe'}, None),
        MemberSpec_('DataEmissaoNFe', 'xs:dateTime', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'DataEmissaoNFe', 'type': 'xs:dateTime'}, None),
        MemberSpec_('NumeroLote', ['tpNumero', 'xs:long'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'NumeroLote', 'type': 'xs:long'}, None),
        MemberSpec_('ChaveRPS', 'tpChaveRPS', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ChaveRPS', 'type': 'tpChaveRPS'}, None),
        MemberSpec_('TipoRPS', ['tpTipoRPS', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'TipoRPS', 'type': 'xs:string'}, None),
        MemberSpec_('DataEmissaoRPS', 'xs:date', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'DataEmissaoRPS', 'type': 'xs:date'}, None),
        MemberSpec_('DataFatoGeradorNFe', 'xs:dateTime', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'DataFatoGeradorNFe', 'type': 'xs:dateTime'}, None),
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
        MemberSpec_('CPFCNPJTomador', 'tpCPFCNPJNIF', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CPFCNPJTomador', 'type': 'tpCPFCNPJNIF'}, None),
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
        MemberSpec_('ValorInicialCobrado', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorInicialCobrado', 'type': 'xs:decimal'}, 9),
        MemberSpec_('ValorFinalCobrado', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorFinalCobrado', 'type': 'xs:decimal'}, 9),
        MemberSpec_('ValorMulta', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorMulta', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorJuros', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorJuros', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorIPI', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorIPI', 'type': 'xs:decimal'}, None),
        MemberSpec_('ExigibilidadeSuspensa', ['tpNaoSim', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ExigibilidadeSuspensa', 'type': 'xs:int'}, None),
        MemberSpec_('PagamentoParceladoAntecipado', ['tpNaoSim', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'PagamentoParceladoAntecipado', 'type': 'xs:int'}, None),
        MemberSpec_('NCM', ['tpCodigoNCM', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'NCM', 'type': 'xs:string'}, None),
        MemberSpec_('NBS', ['tpCodigoNBS', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'NBS', 'type': 'xs:string'}, None),
        MemberSpec_('atvEvento', 'tpAtividadeEvento', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'atvEvento', 'type': 'tpAtividadeEvento'}, None),
        MemberSpec_('cLocPrestacao', ['tpCidade', 'xs:int'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'cLocPrestacao', 'type': 'xs:int'}, None),
        MemberSpec_('cPaisPrestacao', ['tpCodigoPaisISO', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'cPaisPrestacao', 'type': 'xs:string'}, None),
        MemberSpec_('IBSCBS', 'tpIBSCBS', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'IBSCBS', 'type': 'tpIBSCBS'}, None),
        MemberSpec_('RetornoComplementarIBSCBS', 'tpRetornoComplementarIBSCBS', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'RetornoComplementarIBSCBS', 'type': 'tpRetornoComplementarIBSCBS'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Assinatura=None, ChaveNFe=None, DataEmissaoNFe=None, NumeroLote=None, ChaveRPS=None, TipoRPS=None, DataEmissaoRPS=None, DataFatoGeradorNFe=None, CPFCNPJPrestador=None, RazaoSocialPrestador=None, EnderecoPrestador=None, EmailPrestador=None, StatusNFe=None, DataCancelamento=None, TributacaoNFe=None, OpcaoSimples=None, NumeroGuia=None, DataQuitacaoGuia=None, ValorServicos=None, ValorDeducoes=None, ValorPIS=None, ValorCOFINS=None, ValorINSS=None, ValorIR=None, ValorCSLL=None, CodigoServico=None, AliquotaServicos=None, ValorISS=None, ValorCredito=None, ISSRetido=None, CPFCNPJTomador=None, InscricaoMunicipalTomador=None, InscricaoEstadualTomador=None, RazaoSocialTomador=None, EnderecoTomador=None, EmailTomador=None, CPFCNPJIntermediario=None, InscricaoMunicipalIntermediario=None, ISSRetidoIntermediario=None, EmailIntermediario=None, Discriminacao=None, ValorCargaTributaria=None, PercentualCargaTributaria=None, FonteCargaTributaria=None, CodigoCEI=None, MatriculaObra=None, MunicipioPrestacao=None, NumeroEncapsulamento=None, ValorTotalRecebido=None, ValorInicialCobrado=None, ValorFinalCobrado=None, ValorMulta=None, ValorJuros=None, ValorIPI=None, ExigibilidadeSuspensa=None, PagamentoParceladoAntecipado=None, NCM=None, NBS=None, atvEvento=None, cLocPrestacao=None, cPaisPrestacao=None, IBSCBS=None, RetornoComplementarIBSCBS=None, gds_collector_=None, **kwargs_):
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
        if isinstance(DataFatoGeradorNFe, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(DataFatoGeradorNFe, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = DataFatoGeradorNFe
        self.DataFatoGeradorNFe = initvalue_
        self.DataFatoGeradorNFe_nsprefix_ = None
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
        self.ValorInicialCobrado = ValorInicialCobrado
        self.validate_tpValor(self.ValorInicialCobrado)
        self.ValorInicialCobrado_nsprefix_ = None
        self.ValorFinalCobrado = ValorFinalCobrado
        self.validate_tpValor(self.ValorFinalCobrado)
        self.ValorFinalCobrado_nsprefix_ = None
        self.ValorMulta = ValorMulta
        self.validate_tpValor(self.ValorMulta)
        self.ValorMulta_nsprefix_ = None
        self.ValorJuros = ValorJuros
        self.validate_tpValor(self.ValorJuros)
        self.ValorJuros_nsprefix_ = None
        self.ValorIPI = ValorIPI
        self.validate_tpValor(self.ValorIPI)
        self.ValorIPI_nsprefix_ = None
        self.ExigibilidadeSuspensa = ExigibilidadeSuspensa
        self.validate_tpNaoSim(self.ExigibilidadeSuspensa)
        self.ExigibilidadeSuspensa_nsprefix_ = None
        self.PagamentoParceladoAntecipado = PagamentoParceladoAntecipado
        self.validate_tpNaoSim(self.PagamentoParceladoAntecipado)
        self.PagamentoParceladoAntecipado_nsprefix_ = None
        self.NCM = NCM
        self.validate_tpCodigoNCM(self.NCM)
        self.NCM_nsprefix_ = None
        self.NBS = NBS
        self.validate_tpCodigoNBS(self.NBS)
        self.NBS_nsprefix_ = None
        self.atvEvento = atvEvento
        self.atvEvento_nsprefix_ = None
        self.cLocPrestacao = cLocPrestacao
        self.validate_tpCidade(self.cLocPrestacao)
        self.cLocPrestacao_nsprefix_ = None
        self.cPaisPrestacao = cPaisPrestacao
        self.validate_tpCodigoPaisISO(self.cPaisPrestacao)
        self.cPaisPrestacao_nsprefix_ = None
        self.IBSCBS = IBSCBS
        self.IBSCBS_nsprefix_ = None
        self.RetornoComplementarIBSCBS = RetornoComplementarIBSCBS
        self.RetornoComplementarIBSCBS_nsprefix_ = None
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
            enumerations = ['0', '1', '2', '3', '4', '6']
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
    validate_tpInscricaoMunicipal_patterns_ = [['^([0-9]{1,12})$']]
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
    def validate_tpNaoSim(self, value):
        result = True
        # Validate type tpNaoSim, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [0, 1]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpNaoSim' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpNaoSim_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpNaoSim_patterns_, ))
                result = False
        return result
    validate_tpNaoSim_patterns_ = [['^([01]{1})$']]
    def validate_tpCodigoNCM(self, value):
        result = True
        # Validate type tpCodigoNCM, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCodigoNCM_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCodigoNCM_patterns_, ))
                result = False
        return result
    validate_tpCodigoNCM_patterns_ = [['^([0-9]{8})$']]
    def validate_tpCodigoNBS(self, value):
        result = True
        # Validate type tpCodigoNBS, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCodigoNBS_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCodigoNBS_patterns_, ))
                result = False
        return result
    validate_tpCodigoNBS_patterns_ = [['^([0-9]{9})$']]
    def validate_tpCodigoPaisISO(self, value):
        result = True
        # Validate type tpCodigoPaisISO, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCodigoPaisISO_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCodigoPaisISO_patterns_, ))
                result = False
        return result
    validate_tpCodigoPaisISO_patterns_ = [['^([A-Z]{2})$']]
    def has__content(self):
        if (
            self.Assinatura is not None or
            self.ChaveNFe is not None or
            self.DataEmissaoNFe is not None or
            self.NumeroLote is not None or
            self.ChaveRPS is not None or
            self.TipoRPS is not None or
            self.DataEmissaoRPS is not None or
            self.DataFatoGeradorNFe is not None or
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
            self.ValorTotalRecebido is not None or
            self.ValorInicialCobrado is not None or
            self.ValorFinalCobrado is not None or
            self.ValorMulta is not None or
            self.ValorJuros is not None or
            self.ValorIPI is not None or
            self.ExigibilidadeSuspensa is not None or
            self.PagamentoParceladoAntecipado is not None or
            self.NCM is not None or
            self.NBS is not None or
            self.atvEvento is not None or
            self.cLocPrestacao is not None or
            self.cPaisPrestacao is not None or
            self.IBSCBS is not None or
            self.RetornoComplementarIBSCBS is not None
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpNFe')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpNFe', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpNFe'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpNFe', fromsubclass_=False, pretty_print=True):
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
        if self.DataFatoGeradorNFe is not None:
            namespaceprefix_ = self.DataFatoGeradorNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.DataFatoGeradorNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDataFatoGeradorNFe>%s</%sDataFatoGeradorNFe>%s' % (namespaceprefix_ , self.gds_format_datetime(self.DataFatoGeradorNFe, input_name='DataFatoGeradorNFe'), namespaceprefix_ , eol_))
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
        if self.ValorInicialCobrado is not None:
            namespaceprefix_ = self.ValorInicialCobrado_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorInicialCobrado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorInicialCobrado>%s</%sValorInicialCobrado>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorInicialCobrado, input_name='ValorInicialCobrado'), namespaceprefix_ , eol_))
        if self.ValorFinalCobrado is not None:
            namespaceprefix_ = self.ValorFinalCobrado_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorFinalCobrado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorFinalCobrado>%s</%sValorFinalCobrado>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorFinalCobrado, input_name='ValorFinalCobrado'), namespaceprefix_ , eol_))
        if self.ValorMulta is not None:
            namespaceprefix_ = self.ValorMulta_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorMulta_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorMulta>%s</%sValorMulta>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorMulta, input_name='ValorMulta'), namespaceprefix_ , eol_))
        if self.ValorJuros is not None:
            namespaceprefix_ = self.ValorJuros_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorJuros_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorJuros>%s</%sValorJuros>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorJuros, input_name='ValorJuros'), namespaceprefix_ , eol_))
        if self.ValorIPI is not None:
            namespaceprefix_ = self.ValorIPI_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorIPI_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorIPI>%s</%sValorIPI>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorIPI, input_name='ValorIPI'), namespaceprefix_ , eol_))
        if self.ExigibilidadeSuspensa is not None:
            namespaceprefix_ = self.ExigibilidadeSuspensa_nsprefix_ + ':' if (UseCapturedNS_ and self.ExigibilidadeSuspensa_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sExigibilidadeSuspensa>%s</%sExigibilidadeSuspensa>%s' % (namespaceprefix_ , self.gds_format_integer(self.ExigibilidadeSuspensa, input_name='ExigibilidadeSuspensa'), namespaceprefix_ , eol_))
        if self.PagamentoParceladoAntecipado is not None:
            namespaceprefix_ = self.PagamentoParceladoAntecipado_nsprefix_ + ':' if (UseCapturedNS_ and self.PagamentoParceladoAntecipado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPagamentoParceladoAntecipado>%s</%sPagamentoParceladoAntecipado>%s' % (namespaceprefix_ , self.gds_format_integer(self.PagamentoParceladoAntecipado, input_name='PagamentoParceladoAntecipado'), namespaceprefix_ , eol_))
        if self.NCM is not None:
            namespaceprefix_ = self.NCM_nsprefix_ + ':' if (UseCapturedNS_ and self.NCM_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNCM>%s</%sNCM>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NCM), input_name='NCM')), namespaceprefix_ , eol_))
        if self.NBS is not None:
            namespaceprefix_ = self.NBS_nsprefix_ + ':' if (UseCapturedNS_ and self.NBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNBS>%s</%sNBS>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NBS), input_name='NBS')), namespaceprefix_ , eol_))
        if self.atvEvento is not None:
            namespaceprefix_ = self.atvEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.atvEvento_nsprefix_) else ''
            self.atvEvento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='atvEvento', pretty_print=pretty_print)
        if self.cLocPrestacao is not None:
            namespaceprefix_ = self.cLocPrestacao_nsprefix_ + ':' if (UseCapturedNS_ and self.cLocPrestacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scLocPrestacao>%s</%scLocPrestacao>%s' % (namespaceprefix_ , self.gds_format_integer(self.cLocPrestacao, input_name='cLocPrestacao'), namespaceprefix_ , eol_))
        if self.cPaisPrestacao is not None:
            namespaceprefix_ = self.cPaisPrestacao_nsprefix_ + ':' if (UseCapturedNS_ and self.cPaisPrestacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scPaisPrestacao>%s</%scPaisPrestacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cPaisPrestacao), input_name='cPaisPrestacao')), namespaceprefix_ , eol_))
        if self.IBSCBS is not None:
            namespaceprefix_ = self.IBSCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.IBSCBS_nsprefix_) else ''
            self.IBSCBS.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IBSCBS', pretty_print=pretty_print)
        if self.RetornoComplementarIBSCBS is not None:
            namespaceprefix_ = self.RetornoComplementarIBSCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.RetornoComplementarIBSCBS_nsprefix_) else ''
            self.RetornoComplementarIBSCBS.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RetornoComplementarIBSCBS', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
        elif nodeName_ == 'DataFatoGeradorNFe':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.DataFatoGeradorNFe = dval_
            self.DataFatoGeradorNFe_nsprefix_ = child_.prefix
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
            obj_ = tpCPFCNPJNIF.factory(parent_object_=self)
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
        elif nodeName_ == 'ValorInicialCobrado' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorInicialCobrado')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorInicialCobrado')
            self.ValorInicialCobrado = fval_
            self.ValorInicialCobrado_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorInicialCobrado)
        elif nodeName_ == 'ValorFinalCobrado' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorFinalCobrado')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorFinalCobrado')
            self.ValorFinalCobrado = fval_
            self.ValorFinalCobrado_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorFinalCobrado)
        elif nodeName_ == 'ValorMulta' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorMulta')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorMulta')
            self.ValorMulta = fval_
            self.ValorMulta_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorMulta)
        elif nodeName_ == 'ValorJuros' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorJuros')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorJuros')
            self.ValorJuros = fval_
            self.ValorJuros_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorJuros)
        elif nodeName_ == 'ValorIPI' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorIPI')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorIPI')
            self.ValorIPI = fval_
            self.ValorIPI_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorIPI)
        elif nodeName_ == 'ExigibilidadeSuspensa' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ExigibilidadeSuspensa')
            ival_ = self.gds_validate_integer(ival_, node, 'ExigibilidadeSuspensa')
            self.ExigibilidadeSuspensa = ival_
            self.ExigibilidadeSuspensa_nsprefix_ = child_.prefix
            # validate type tpNaoSim
            self.validate_tpNaoSim(self.ExigibilidadeSuspensa)
        elif nodeName_ == 'PagamentoParceladoAntecipado' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'PagamentoParceladoAntecipado')
            ival_ = self.gds_validate_integer(ival_, node, 'PagamentoParceladoAntecipado')
            self.PagamentoParceladoAntecipado = ival_
            self.PagamentoParceladoAntecipado_nsprefix_ = child_.prefix
            # validate type tpNaoSim
            self.validate_tpNaoSim(self.PagamentoParceladoAntecipado)
        elif nodeName_ == 'NCM':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NCM')
            value_ = self.gds_validate_string(value_, node, 'NCM')
            self.NCM = value_
            self.NCM_nsprefix_ = child_.prefix
            # validate type tpCodigoNCM
            self.validate_tpCodigoNCM(self.NCM)
        elif nodeName_ == 'NBS':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NBS')
            value_ = self.gds_validate_string(value_, node, 'NBS')
            self.NBS = value_
            self.NBS_nsprefix_ = child_.prefix
            # validate type tpCodigoNBS
            self.validate_tpCodigoNBS(self.NBS)
        elif nodeName_ == 'atvEvento':
            obj_ = tpAtividadeEvento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.atvEvento = obj_
            obj_.original_tagname_ = 'atvEvento'
        elif nodeName_ == 'cLocPrestacao' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'cLocPrestacao')
            ival_ = self.gds_validate_integer(ival_, node, 'cLocPrestacao')
            self.cLocPrestacao = ival_
            self.cLocPrestacao_nsprefix_ = child_.prefix
            # validate type tpCidade
            self.validate_tpCidade(self.cLocPrestacao)
        elif nodeName_ == 'cPaisPrestacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cPaisPrestacao')
            value_ = self.gds_validate_string(value_, node, 'cPaisPrestacao')
            self.cPaisPrestacao = value_
            self.cPaisPrestacao_nsprefix_ = child_.prefix
            # validate type tpCodigoPaisISO
            self.validate_tpCodigoPaisISO(self.cPaisPrestacao)
        elif nodeName_ == 'IBSCBS':
            obj_ = tpIBSCBS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IBSCBS = obj_
            obj_.original_tagname_ = 'IBSCBS'
        elif nodeName_ == 'RetornoComplementarIBSCBS':
            obj_ = tpRetornoComplementarIBSCBS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RetornoComplementarIBSCBS = obj_
            obj_.original_tagname_ = 'RetornoComplementarIBSCBS'
# end class tpNFe


class tpRPS(GeneratedsSuper):
    """tpRPS -- Tipo que representa um RPS.
    Assinatura -- Assinatura digital do RPS.
    ChaveRPS -- Informe a chave do RPS emitido.
    TipoRPS -- Informe o Tipo do RPS emitido.
    DataEmissao -- Informe a Data de emiss
    ã
    o do RPS.
    StatusRPS -- Informe o Status do RPS.
    TributacaoRPS -- Informe o tipo de tributa
    ç
    ã
    o do RPS.
    ValorDeducoes -- Informe o valor das dedu
    ç
    õ
    es.
    ValorPIS -- Informe o valor da reten
    ç
    ã
    o do PIS.
    ValorCOFINS -- Informe o valor da reten
    ç
    ã
    o do COFINS.
    ValorINSS -- Informe o valor da reten
    ç
    ã
    o do INSS.
    ValorIR -- Informe o valor da reten
    ç
    ã
    o do IR.
    ValorCSLL -- Informe o valor da reten
    ç
    ã
    o do CSLL.
    CodigoServico -- Informe o c
    ó
    digo do servi
    ç
    o do RPS. Este c
    ó
    digo deve pertencer
    à
    lista de servi
    ç
    os.
    AliquotaServicos -- Informe o valor da al
    í
    quota. Obs. O conte
    ú
    do deste campo ser
    á
    ignorado caso a tributa
    ç
    ã
    o ocorra no munic
    í
    pio (Situa
    ç
    ã
    o do RPS = T ).
    ISSRetido -- Informe a reten
    ç
    ã
    o.
    CPFCNPJTomador -- Informe o CPF/CNPJ do tomador do servi
    ç
    o. O conte
    ú
    do deste campo ser
    á
    ignorado caso o campo InscricaoMunicipalTomador esteja preenchido.
    InscricaoMunicipalTomador -- Informe a Inscri
    ç
    ã
    o Municipal do Tomador. ATEN
    Ç
    Ã
    O: Este campo s
    ó
    dever
    á
    ser preenchido para tomadores estabelecidos no munic
    í
    pio de S
    ã
    o Paulo (CCM). Quando este campo for preenchido, seu conte
    ú
    do ser
    á
    considerado como priorit
    á
    rio com rela
    ç
    ã
    o ao campo de CPF/CNPJ do Tomador, sendo utilizado para identificar o Tomador e recuperar seus dados da base de dados da Prefeitura.
    InscricaoEstadualTomador -- Informe a inscri
    ç
    ã
    o estadual do tomador. Este campo ser
    á
    ignorado caso seja fornecido um CPF/CNPJ ou a Inscri
    ç
    ã
    o Municipal do tomador perten
    ç
    a ao munic
    í
    pio de S
    ã
    o Paulo.
    RazaoSocialTomador -- Informe o Nome/Raz
    ã
    o Social do tomador. Este campo
    é
    obrigat
    ó
    rio apenas para tomadores Pessoa Jur
    í
    dica (CNPJ). Este campo ser
    á
    ignorado caso seja fornecido um CPF/CNPJ ou a Inscri
    ç
    ã
    o Municipal do tomador perten
    ç
    a ao munic
    í
    pio de S
    ã
    o Paulo.
    EnderecoTomador -- Informe o endere
    ç
    o do tomador. Os campos do endere
    ç
    o s
    ã
    o obrigat
    ó
    rios apenas para tomadores pessoa jur
    í
    dica (CNPJ informado). O conte
    ú
    do destes campos ser
    á
    ignorado caso seja fornecido um CPF/CNPJ ou a Inscri
    ç
    ã
    o Municipal do tomador perten
    ç
    a ao munic
    í
    pio de S
    ã
    o Paulo.
    EmailTomador -- Informe o e-mail do tomador.
    CPFCNPJIntermediario -- CNPJ do intermedi
    á
    rio de servi
    ç
    o.
    InscricaoMunicipalIntermediario -- Inscri
    ç
    ã
    o Municipal do intermedi
    á
    rio de servi
    ç
    o.
    ISSRetidoIntermediario -- Reten
    ç
    ã
    o do ISS pelo intermedi
    á
    rio de servi
    ç
    o.
    EmailIntermediario -- E-mail do intermedi
    á
    rio de servi
    ç
    o.
    Discriminacao -- Informe a discrimina
    ç
    ã
    o dos servi
    ç
    os.
    ValorCargaTributaria -- Valor da carga tribut
    á
    ria total em R$.
    PercentualCargaTributaria -- Valor percentual da carga tribut
    á
    ria.
    FonteCargaTributaria -- Fonte de informa
    ç
    ã
    o da carga tribut
    á
    ria.
    CodigoCEI -- C
    ó
    digo do CEI - Cadastro espec
    í
    fico do INSS.
    MatriculaObra -- C
    ó
    digo que representa a matr
    í
    cula da obra no sistema de cadastro de obras.
    MunicipioPrestacao -- C
    ó
    digo da cidade do munic
    í
    pio da presta
    ç
    ã
    o do servi
    ç
    o.
    NumeroEncapsulamento -- C
    ó
    digo que representa o n
    ú
    mero do encapsulamento da obra.
    ValorTotalRecebido -- Valor do total recebido.
    ValorInicialCobrado -- Valor inicial cobrado pela presta
    ç
    ã
    o do servi
    ç
    o, antes de tributos, multa e juros.
    "Valor dos servi
    ç
    os antes dos tributos". Corresponde ao valor cobrado pela presta
    ç
    ã
    o do servi
    ç
    o, antes de tributos, multa e juros.
    Informado para realizar o c
    á
    lculo dos tributos do in
    í
    cio para o fim.
    ValorFinalCobrado -- Valor final cobrado pela presta
    ç
    ã
    o do servi
    ç
    o, incluindo todos os tributos.
    "Valor total na nota". Corresponde ao valor final cobrado pela presta
    ç
    ã
    o do servi
    ç
    o, incluindo todos os tributos, multa e juros.
    Informado para realizar o c
    á
    lculo dos impostos do fim para o in
    í
    cio.
    ValorMulta -- Valor da multa.
    ValorJuros -- Valor dos juros.
    ValorIPI -- Valor de IPI.
    ExigibilidadeSuspensa -- Informe se
    é
    uma emiss
    ã
    o com exigibilidade suspensa.
    0 - N
    ã
    o.
    1 - Sim.
    PagamentoParceladoAntecipado -- Informe a nota fiscal de pagamento parcelado antecipado (realizado antes do fornecimento).
    0 - N
    ã
    o.
    1 - Sim.
    NCM -- Informe o n
    ú
    mero NCM (Nomenclatura Comum do Mercosul).
    NBS -- Informe o n
    ú
    mero NBS (Nomenclatura Brasileira de Servi
    ç
    os).
    atvEvento -- Informa
    ç
    õ
    es dos Tipos de evento.
    IBSCBS -- Informa
    ç
    õ
    es declaradas pelo emitente referentes ao IBS e
    à
    CBS.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Assinatura', ['tpAssinatura', 'xs:base64Binary'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'Assinatura', 'type': 'xs:base64Binary'}, None),
        MemberSpec_('ChaveRPS', 'tpChaveRPS', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ChaveRPS', 'type': 'tpChaveRPS'}, None),
        MemberSpec_('TipoRPS', ['tpTipoRPS', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'TipoRPS', 'type': 'xs:string'}, None),
        MemberSpec_('DataEmissao', 'xs:date', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'DataEmissao', 'type': 'xs:date'}, None),
        MemberSpec_('StatusRPS', ['tpStatusNFe', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'StatusRPS', 'type': 'xs:string'}, None),
        MemberSpec_('TributacaoRPS', ['tpTributacaoNFe', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'TributacaoRPS', 'type': 'xs:string'}, None),
        MemberSpec_('ValorDeducoes', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorDeducoes', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorPIS', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorPIS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorCOFINS', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorCOFINS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorINSS', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorINSS', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorIR', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorIR', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorCSLL', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorCSLL', 'type': 'xs:decimal'}, None),
        MemberSpec_('CodigoServico', ['tpCodigoServico', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'CodigoServico', 'type': 'xs:int'}, None),
        MemberSpec_('AliquotaServicos', ['tpAliquota', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'AliquotaServicos', 'type': 'xs:decimal'}, None),
        MemberSpec_('ISSRetido', 'xs:boolean', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ISSRetido', 'type': 'xs:boolean'}, None),
        MemberSpec_('CPFCNPJTomador', 'tpCPFCNPJNIF', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'CPFCNPJTomador', 'type': 'tpCPFCNPJNIF'}, None),
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
        MemberSpec_('ValorInicialCobrado', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorInicialCobrado', 'type': 'xs:decimal'}, 10),
        MemberSpec_('ValorFinalCobrado', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorFinalCobrado', 'type': 'xs:decimal'}, 10),
        MemberSpec_('ValorMulta', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorMulta', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorJuros', ['tpValor', 'xs:decimal'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ValorJuros', 'type': 'xs:decimal'}, None),
        MemberSpec_('ValorIPI', ['tpValor', 'xs:decimal'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ValorIPI', 'type': 'xs:decimal'}, None),
        MemberSpec_('ExigibilidadeSuspensa', ['tpNaoSim', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'ExigibilidadeSuspensa', 'type': 'xs:int'}, None),
        MemberSpec_('PagamentoParceladoAntecipado', ['tpNaoSim', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'PagamentoParceladoAntecipado', 'type': 'xs:int'}, None),
        MemberSpec_('NCM', ['tpCodigoNCM', 'xs:string'], 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'NCM', 'type': 'xs:string'}, None),
        MemberSpec_('NBS', ['tpCodigoNBS', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'NBS', 'type': 'xs:string'}, None),
        MemberSpec_('atvEvento', 'tpAtividadeEvento', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'atvEvento', 'type': 'tpAtividadeEvento'}, None),
        MemberSpec_('cLocPrestacao', ['tpCidade', 'xs:int'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'cLocPrestacao', 'type': 'xs:int'}, None),
        MemberSpec_('cPaisPrestacao', ['tpCodigoPaisISO', 'xs:string'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'cPaisPrestacao', 'type': 'xs:string'}, None),
        MemberSpec_('IBSCBS', 'tpIBSCBS', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'IBSCBS', 'type': 'tpIBSCBS'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Assinatura=None, ChaveRPS=None, TipoRPS=None, DataEmissao=None, StatusRPS=None, TributacaoRPS=None, ValorDeducoes=None, ValorPIS=None, ValorCOFINS=None, ValorINSS=None, ValorIR=None, ValorCSLL=None, CodigoServico=None, AliquotaServicos=None, ISSRetido=None, CPFCNPJTomador=None, InscricaoMunicipalTomador=None, InscricaoEstadualTomador=None, RazaoSocialTomador=None, EnderecoTomador=None, EmailTomador=None, CPFCNPJIntermediario=None, InscricaoMunicipalIntermediario=None, ISSRetidoIntermediario=None, EmailIntermediario=None, Discriminacao=None, ValorCargaTributaria=None, PercentualCargaTributaria=None, FonteCargaTributaria=None, CodigoCEI=None, MatriculaObra=None, MunicipioPrestacao=None, NumeroEncapsulamento=None, ValorTotalRecebido=None, ValorInicialCobrado=None, ValorFinalCobrado=None, ValorMulta=None, ValorJuros=None, ValorIPI=None, ExigibilidadeSuspensa=None, PagamentoParceladoAntecipado=None, NCM=None, NBS=None, atvEvento=None, cLocPrestacao=None, cPaisPrestacao=None, IBSCBS=None, gds_collector_=None, **kwargs_):
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
        self.ValorInicialCobrado = ValorInicialCobrado
        self.validate_tpValor(self.ValorInicialCobrado)
        self.ValorInicialCobrado_nsprefix_ = None
        self.ValorFinalCobrado = ValorFinalCobrado
        self.validate_tpValor(self.ValorFinalCobrado)
        self.ValorFinalCobrado_nsprefix_ = None
        self.ValorMulta = ValorMulta
        self.validate_tpValor(self.ValorMulta)
        self.ValorMulta_nsprefix_ = None
        self.ValorJuros = ValorJuros
        self.validate_tpValor(self.ValorJuros)
        self.ValorJuros_nsprefix_ = None
        self.ValorIPI = ValorIPI
        self.validate_tpValor(self.ValorIPI)
        self.ValorIPI_nsprefix_ = None
        self.ExigibilidadeSuspensa = ExigibilidadeSuspensa
        self.validate_tpNaoSim(self.ExigibilidadeSuspensa)
        self.ExigibilidadeSuspensa_nsprefix_ = None
        self.PagamentoParceladoAntecipado = PagamentoParceladoAntecipado
        self.validate_tpNaoSim(self.PagamentoParceladoAntecipado)
        self.PagamentoParceladoAntecipado_nsprefix_ = None
        self.NCM = NCM
        self.validate_tpCodigoNCM(self.NCM)
        self.NCM_nsprefix_ = None
        self.NBS = NBS
        self.validate_tpCodigoNBS(self.NBS)
        self.NBS_nsprefix_ = None
        self.atvEvento = atvEvento
        self.atvEvento_nsprefix_ = None
        self.cLocPrestacao = cLocPrestacao
        self.validate_tpCidade(self.cLocPrestacao)
        self.cLocPrestacao_nsprefix_ = None
        self.cPaisPrestacao = cPaisPrestacao
        self.validate_tpCodigoPaisISO(self.cPaisPrestacao)
        self.cPaisPrestacao_nsprefix_ = None
        self.IBSCBS = IBSCBS
        self.IBSCBS_nsprefix_ = None
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
    validate_tpInscricaoMunicipal_patterns_ = [['^([0-9]{1,12})$']]
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
    def validate_tpNaoSim(self, value):
        result = True
        # Validate type tpNaoSim, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = [0, 1]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on tpNaoSim' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpNaoSim_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpNaoSim_patterns_, ))
                result = False
        return result
    validate_tpNaoSim_patterns_ = [['^([01]{1})$']]
    def validate_tpCodigoNCM(self, value):
        result = True
        # Validate type tpCodigoNCM, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCodigoNCM_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCodigoNCM_patterns_, ))
                result = False
        return result
    validate_tpCodigoNCM_patterns_ = [['^([0-9]{8})$']]
    def validate_tpCodigoNBS(self, value):
        result = True
        # Validate type tpCodigoNBS, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCodigoNBS_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCodigoNBS_patterns_, ))
                result = False
        return result
    validate_tpCodigoNBS_patterns_ = [['^([0-9]{9})$']]
    def validate_tpCodigoPaisISO(self, value):
        result = True
        # Validate type tpCodigoPaisISO, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpCodigoPaisISO_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpCodigoPaisISO_patterns_, ))
                result = False
        return result
    validate_tpCodigoPaisISO_patterns_ = [['^([A-Z]{2})$']]
    def has__content(self):
        if (
            self.Assinatura is not None or
            self.ChaveRPS is not None or
            self.TipoRPS is not None or
            self.DataEmissao is not None or
            self.StatusRPS is not None or
            self.TributacaoRPS is not None or
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
            self.ValorTotalRecebido is not None or
            self.ValorInicialCobrado is not None or
            self.ValorFinalCobrado is not None or
            self.ValorMulta is not None or
            self.ValorJuros is not None or
            self.ValorIPI is not None or
            self.ExigibilidadeSuspensa is not None or
            self.PagamentoParceladoAntecipado is not None or
            self.NCM is not None or
            self.NBS is not None or
            self.atvEvento is not None or
            self.cLocPrestacao is not None or
            self.cPaisPrestacao is not None or
            self.IBSCBS is not None
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tpRPS')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tpRPS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tipos:', name_='tpRPS'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='tipos:', namespacedef_='', name_='tpRPS', fromsubclass_=False, pretty_print=True):
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
        if self.ValorInicialCobrado is not None:
            namespaceprefix_ = self.ValorInicialCobrado_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorInicialCobrado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorInicialCobrado>%s</%sValorInicialCobrado>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorInicialCobrado, input_name='ValorInicialCobrado'), namespaceprefix_ , eol_))
        if self.ValorFinalCobrado is not None:
            namespaceprefix_ = self.ValorFinalCobrado_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorFinalCobrado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorFinalCobrado>%s</%sValorFinalCobrado>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorFinalCobrado, input_name='ValorFinalCobrado'), namespaceprefix_ , eol_))
        if self.ValorMulta is not None:
            namespaceprefix_ = self.ValorMulta_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorMulta_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorMulta>%s</%sValorMulta>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorMulta, input_name='ValorMulta'), namespaceprefix_ , eol_))
        if self.ValorJuros is not None:
            namespaceprefix_ = self.ValorJuros_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorJuros_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorJuros>%s</%sValorJuros>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorJuros, input_name='ValorJuros'), namespaceprefix_ , eol_))
        if self.ValorIPI is not None:
            namespaceprefix_ = self.ValorIPI_nsprefix_ + ':' if (UseCapturedNS_ and self.ValorIPI_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValorIPI>%s</%sValorIPI>%s' % (namespaceprefix_ , self.gds_format_decimal(self.ValorIPI, input_name='ValorIPI'), namespaceprefix_ , eol_))
        if self.ExigibilidadeSuspensa is not None:
            namespaceprefix_ = self.ExigibilidadeSuspensa_nsprefix_ + ':' if (UseCapturedNS_ and self.ExigibilidadeSuspensa_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sExigibilidadeSuspensa>%s</%sExigibilidadeSuspensa>%s' % (namespaceprefix_ , self.gds_format_integer(self.ExigibilidadeSuspensa, input_name='ExigibilidadeSuspensa'), namespaceprefix_ , eol_))
        if self.PagamentoParceladoAntecipado is not None:
            namespaceprefix_ = self.PagamentoParceladoAntecipado_nsprefix_ + ':' if (UseCapturedNS_ and self.PagamentoParceladoAntecipado_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPagamentoParceladoAntecipado>%s</%sPagamentoParceladoAntecipado>%s' % (namespaceprefix_ , self.gds_format_integer(self.PagamentoParceladoAntecipado, input_name='PagamentoParceladoAntecipado'), namespaceprefix_ , eol_))
        if self.NCM is not None:
            namespaceprefix_ = self.NCM_nsprefix_ + ':' if (UseCapturedNS_ and self.NCM_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNCM>%s</%sNCM>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NCM), input_name='NCM')), namespaceprefix_ , eol_))
        if self.NBS is not None:
            namespaceprefix_ = self.NBS_nsprefix_ + ':' if (UseCapturedNS_ and self.NBS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNBS>%s</%sNBS>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.NBS), input_name='NBS')), namespaceprefix_ , eol_))
        if self.atvEvento is not None:
            namespaceprefix_ = self.atvEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.atvEvento_nsprefix_) else ''
            self.atvEvento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='atvEvento', pretty_print=pretty_print)
        if self.cLocPrestacao is not None:
            namespaceprefix_ = self.cLocPrestacao_nsprefix_ + ':' if (UseCapturedNS_ and self.cLocPrestacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scLocPrestacao>%s</%scLocPrestacao>%s' % (namespaceprefix_ , self.gds_format_integer(self.cLocPrestacao, input_name='cLocPrestacao'), namespaceprefix_ , eol_))
        if self.cPaisPrestacao is not None:
            namespaceprefix_ = self.cPaisPrestacao_nsprefix_ + ':' if (UseCapturedNS_ and self.cPaisPrestacao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scPaisPrestacao>%s</%scPaisPrestacao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cPaisPrestacao), input_name='cPaisPrestacao')), namespaceprefix_ , eol_))
        if self.IBSCBS is not None:
            namespaceprefix_ = self.IBSCBS_nsprefix_ + ':' if (UseCapturedNS_ and self.IBSCBS_nsprefix_) else ''
            self.IBSCBS.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IBSCBS', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
            obj_ = tpCPFCNPJNIF.factory(parent_object_=self)
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
        elif nodeName_ == 'ValorInicialCobrado' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorInicialCobrado')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorInicialCobrado')
            self.ValorInicialCobrado = fval_
            self.ValorInicialCobrado_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorInicialCobrado)
        elif nodeName_ == 'ValorFinalCobrado' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorFinalCobrado')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorFinalCobrado')
            self.ValorFinalCobrado = fval_
            self.ValorFinalCobrado_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorFinalCobrado)
        elif nodeName_ == 'ValorMulta' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorMulta')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorMulta')
            self.ValorMulta = fval_
            self.ValorMulta_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorMulta)
        elif nodeName_ == 'ValorJuros' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorJuros')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorJuros')
            self.ValorJuros = fval_
            self.ValorJuros_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorJuros)
        elif nodeName_ == 'ValorIPI' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'ValorIPI')
            fval_ = self.gds_validate_decimal(fval_, node, 'ValorIPI')
            self.ValorIPI = fval_
            self.ValorIPI_nsprefix_ = child_.prefix
            # validate type tpValor
            self.validate_tpValor(self.ValorIPI)
        elif nodeName_ == 'ExigibilidadeSuspensa' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'ExigibilidadeSuspensa')
            ival_ = self.gds_validate_integer(ival_, node, 'ExigibilidadeSuspensa')
            self.ExigibilidadeSuspensa = ival_
            self.ExigibilidadeSuspensa_nsprefix_ = child_.prefix
            # validate type tpNaoSim
            self.validate_tpNaoSim(self.ExigibilidadeSuspensa)
        elif nodeName_ == 'PagamentoParceladoAntecipado' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'PagamentoParceladoAntecipado')
            ival_ = self.gds_validate_integer(ival_, node, 'PagamentoParceladoAntecipado')
            self.PagamentoParceladoAntecipado = ival_
            self.PagamentoParceladoAntecipado_nsprefix_ = child_.prefix
            # validate type tpNaoSim
            self.validate_tpNaoSim(self.PagamentoParceladoAntecipado)
        elif nodeName_ == 'NCM':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NCM')
            value_ = self.gds_validate_string(value_, node, 'NCM')
            self.NCM = value_
            self.NCM_nsprefix_ = child_.prefix
            # validate type tpCodigoNCM
            self.validate_tpCodigoNCM(self.NCM)
        elif nodeName_ == 'NBS':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'NBS')
            value_ = self.gds_validate_string(value_, node, 'NBS')
            self.NBS = value_
            self.NBS_nsprefix_ = child_.prefix
            # validate type tpCodigoNBS
            self.validate_tpCodigoNBS(self.NBS)
        elif nodeName_ == 'atvEvento':
            obj_ = tpAtividadeEvento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.atvEvento = obj_
            obj_.original_tagname_ = 'atvEvento'
        elif nodeName_ == 'cLocPrestacao' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'cLocPrestacao')
            ival_ = self.gds_validate_integer(ival_, node, 'cLocPrestacao')
            self.cLocPrestacao = ival_
            self.cLocPrestacao_nsprefix_ = child_.prefix
            # validate type tpCidade
            self.validate_tpCidade(self.cLocPrestacao)
        elif nodeName_ == 'cPaisPrestacao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cPaisPrestacao')
            value_ = self.gds_validate_string(value_, node, 'cPaisPrestacao')
            self.cPaisPrestacao = value_
            self.cPaisPrestacao_nsprefix_ = child_.prefix
            # validate type tpCodigoPaisISO
            self.validate_tpCodigoPaisISO(self.cPaisPrestacao)
        elif nodeName_ == 'IBSCBS':
            obj_ = tpIBSCBS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IBSCBS = obj_
            obj_.original_tagname_ = 'IBSCBS'
# end class tpRPS


class SignatureType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional', 'name': 'Id'}),
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
        self.SignedInfo_nsprefix_ = "ds"
        self.SignatureValue = SignatureValue
        self.SignatureValue_nsprefix_ = "ds"
        self.KeyInfo = KeyInfo
        self.KeyInfo_nsprefix_ = "ds"
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureType', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional', 'name': 'Id'}),
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureValueType')
        outfile.write('>')
        self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_, pretty_print=pretty_print)
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureValueType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValueType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SignatureValueType


class SignedInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional', 'name': 'Id'}),
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
        self.Reference_nsprefix_ = "ds"
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignedInfoType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignedInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignedInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignedInfoType', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional', 'name': 'Id'}),
        MemberSpec_('URI', 'xs:anyURI', 0, 1, {'use': 'optional', 'name': 'URI'}),
        MemberSpec_('Type', 'xs:anyURI', 0, 1, {'use': 'optional', 'name': 'Type'}),
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
        self.Transforms_nsprefix_ = "ds"
        self.DigestMethod = DigestMethod
        self.DigestMethod_nsprefix_ = None
        self.DigestValue = DigestValue
        self.validate_DigestValueType(self.DigestValue)
        self.DigestValue_nsprefix_ = "ds"
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReferenceType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReferenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='ReferenceType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            outfile.write(' URI=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.URI), input_name='URI')), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Type), input_name='Type')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='ReferenceType', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
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
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
        self.Transform_nsprefix_ = "ds"
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformsType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransformsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformsType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformsType', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transform':
            obj_ = TransformType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transform.append(obj_)
            obj_.original_tagname_ = 'Transform'
# end class TransformsType


class TransformType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'xs:anyURI', 0, 0, {'use': 'required', 'name': 'Algorithm'}),
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransformType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Algorithm), input_name='Algorithm')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformType', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional', 'name': 'Id'}),
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
        self.X509Data_nsprefix_ = "ds"
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyInfoType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='KeyInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='KeyInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyInfoType', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyValueType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='KeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='KeyValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyValueType', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='X509DataType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='X509DataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='X509DataType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509DataType', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
    """CabecalhoType -- Cabe
    ç
    alho do retorno.
    Versao -- Vers
    ã
    o do Schema XML utilizado.
    Sucesso -- Campo indicativo do sucesso do pedido do servi
    ç
    o.

    """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Versao', 'tipos:tpVersao', 0, 0, {'use': 'required', 'name': 'Versao'}),
        MemberSpec_('Sucesso', ['tpSucesso', 'xs:boolean'], 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'Sucesso', 'type': 'xs:boolean'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Versao=None, Sucesso=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Versao = _cast(None, Versao)
        self.Versao_nsprefix_ = None
        self.Sucesso = Sucesso
        self.validate_tpSucesso(self.Sucesso)
        self.Sucesso_nsprefix_ = None
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
    def validate_tpSucesso(self, value):
        result = True
        # Validate type tpSucesso, a restriction on xs:boolean.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
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
    def has__content(self):
        if (
            self.Sucesso is not None
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CabecalhoType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CabecalhoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CabecalhoType'):
        if self.Versao is not None and 'Versao' not in already_processed:
            already_processed.add('Versao')
            outfile.write(' Versao="%s"' % self.gds_format_integer(self.Versao, input_name='Versao'))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CabecalhoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Sucesso is not None:
            namespaceprefix_ = self.Sucesso_nsprefix_ + ':' if (UseCapturedNS_ and self.Sucesso_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSucesso>%s</%sSucesso>%s' % (namespaceprefix_ , self.gds_format_boolean(self.Sucesso, input_name='Sucesso'), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Versao', node)
        if value is not None and 'Versao' not in already_processed:
            already_processed.add('Versao')
            self.Versao = self.gds_parse_integer(value, node, 'Versao')
            self.validate_tpVersao(self.Versao)    # validate type tpVersao
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Sucesso':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'Sucesso')
            ival_ = self.gds_validate_boolean(ival_, node, 'Sucesso')
            self.Sucesso = ival_
            self.Sucesso_nsprefix_ = child_.prefix
            # validate type tpSucesso
            self.validate_tpSucesso(self.Sucesso)
# end class CabecalhoType


class CanonicalizationMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'xs:anyURI', 0, 0, {'use': 'required', 'name': 'Algorithm'}),
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CanonicalizationMethodType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CanonicalizationMethodType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CanonicalizationMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Algorithm), input_name='Algorithm')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CanonicalizationMethodType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CanonicalizationMethodType


class SignatureMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'xs:anyURI', 0, 0, {'use': 'required', 'name': 'Algorithm'}),
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureMethodType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureMethodType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SignatureMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Algorithm), input_name='Algorithm')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SignatureMethodType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SignatureMethodType


class DigestMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'xs:anyURI', 0, 0, {'use': 'required', 'name': 'Algorithm'}),
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DigestMethodType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DigestMethodType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DigestMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Algorithm), input_name='Algorithm')), ))
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DigestMethodType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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
    def has__content(self):
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
        self._exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RSAKeyValueType')
        if self.has__content():
            outfile.write('>%s' % (eol_, ))
            self._exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RSAKeyValueType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def _exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RSAKeyValueType'):
        pass
    def _exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='RSAKeyValueType', fromsubclass_=False, pretty_print=True):
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
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def _buildAttributes(self, node, attrs, already_processed):
        pass
    def _buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
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


#
# End data representation classes.
#


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
    prefix_tag = TagNamePrefix + tag
    rootClass = GDSClassesMapping.get(prefix_tag)
    if rootClass is None:
        rootClass = globals().get(prefix_tag)
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
        rootTag = 'RetornoConsulta'
        rootClass = RetornoConsulta
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
               mapping=None, reverse_mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'RetornoConsulta'
        rootClass = RetornoConsulta
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
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
    return rootObj, rootElement, mapping, reverse_node_mapping


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
        rootTag = 'RetornoConsulta'
        rootClass = RetornoConsulta
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
        rootTag = 'RetornoConsulta'
        rootClass = RetornoConsulta
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from RetornoConsulta import *\n\n')
        sys.stdout.write('import RetornoConsulta as model_\n\n')
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
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpAssinatura',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpAssinaturaCancelamento',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpBairro',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCCIB',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpClassificacaoTributaria',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCEP',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCidade',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpChaveNotaNacional',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCNPJ',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCodigoServico',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCodigoEvento',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCodigoEndPostal',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCodigoNBS',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCodigoNCM',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCodigoPaisISO',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCodigoVerificacao',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpComplementoEndereco',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpEnteGov',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCPF',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpDescricaoEvento',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpDiscriminacao',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpEmail',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpEstadoProvinciaRegiao',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpFonteCargaTributaria',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpInscricaoEstadual',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpInscricaoMunicipal',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpLogradouro',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpNaoNIF',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpNaoSim',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpNIF',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpNomeCidade',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpNumero',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpNumeroEndereco',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpOpcaoSimples',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpPercentualCargaTributaria',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpQuantidade',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpRazaoSocialObrigatorio',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpRazaoSocial',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpReferencia',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpSerieRPS',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpStatusNFe',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpSucesso',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpTempoProcessamento',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpTipoLogradouro',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpTipoNotaReferenciada',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpTipoRPS',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpTributacaoNFe',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpUF',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpValor',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpVersao',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpFinNFSe',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCIndOp',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpOper',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpIndDest',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpCObra',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpInscImobFisc',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpTipoChaveDFE',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpXTipoChaveDFe',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpChaveDFe',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpNumeroDescricaoDocumento',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpReeRepRes',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpXTpReeRepRes',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpXNomeEvt',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'ST'),
                                               ('tpEvento',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpCPFCNPJ',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpCPFCNPJNIF',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpChaveNFeRPS',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpChaveNFe',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpChaveRPS',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpEnderecoExterior',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpEnderecoNacional',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpEndereco',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpEnderecoIBSCBS',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpEnderecoSimplesIBSCBS',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpInformacoesLote',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpInformacoesPessoa',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpGRefNFSe',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpGrupoReeRepRes',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpImovelObra',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpDocumento',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpDFeNacional',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpDocFiscalOutro',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpDocOutro',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpFornecedor',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpAtividadeEvento',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpIBSCBS',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpGIBSCBS',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpGTribRegular',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpRetornoComplementarIBSCBS',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpTrib',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpValores',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpNFe',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT'),
                                               ('tpRPS',
                                                'schemas/nfse/TiposNFe_v02.xsd',
                                                'CT')],
 'http://www.w3.org/2000/09/xmldsig#': [('CryptoBinary',
                                         'schemas/nfse/xmldsig-core-schema_v02.xsd',
                                         'ST'),
                                        ('DigestValueType',
                                         'schemas/nfse/xmldsig-core-schema_v02.xsd',
                                         'ST'),
                                        ('SignatureType',
                                         'schemas/nfse/xmldsig-core-schema_v02.xsd',
                                         'CT'),
                                        ('SignatureValueType',
                                         'schemas/nfse/xmldsig-core-schema_v02.xsd',
                                         'CT'),
                                        ('SignedInfoType',
                                         'schemas/nfse/xmldsig-core-schema_v02.xsd',
                                         'CT'),
                                        ('ReferenceType',
                                         'schemas/nfse/xmldsig-core-schema_v02.xsd',
                                         'CT'),
                                        ('TransformsType',
                                         'schemas/nfse/xmldsig-core-schema_v02.xsd',
                                         'CT'),
                                        ('TransformType',
                                         'schemas/nfse/xmldsig-core-schema_v02.xsd',
                                         'CT'),
                                        ('KeyInfoType',
                                         'schemas/nfse/xmldsig-core-schema_v02.xsd',
                                         'CT'),
                                        ('KeyValueType',
                                         'schemas/nfse/xmldsig-core-schema_v02.xsd',
                                         'CT'),
                                        ('X509DataType',
                                         'schemas/nfse/xmldsig-core-schema_v02.xsd',
                                         'CT')]}

__all__ = [
    "CabecalhoType",
    "CanonicalizationMethodType",
    "DigestMethodType",
    "KeyInfoType",
    "KeyValueType",
    "RSAKeyValueType",
    "ReferenceType",
    "RetornoConsulta",
    "SignatureMethodType",
    "SignatureType",
    "SignatureValueType",
    "SignedInfoType",
    "TransformType",
    "TransformsType",
    "X509DataType",
    "tpAtividadeEvento",
    "tpCPFCNPJ",
    "tpCPFCNPJNIF",
    "tpChaveNFe",
    "tpChaveNFeRPS",
    "tpChaveRPS",
    "tpDFeNacional",
    "tpDocFiscalOutro",
    "tpDocOutro",
    "tpDocumento",
    "tpEndereco",
    "tpEnderecoExterior",
    "tpEnderecoIBSCBS",
    "tpEnderecoNacional",
    "tpEnderecoSimplesIBSCBS",
    "tpEvento",
    "tpFornecedor",
    "tpGIBSCBS",
    "tpGRefNFSe",
    "tpGTribRegular",
    "tpGrupoReeRepRes",
    "tpIBSCBS",
    "tpImovelObra",
    "tpInformacoesLote",
    "tpInformacoesPessoa",
    "tpNFe",
    "tpRPS",
    "tpRetornoComplementarIBSCBS",
    "tpTrib",
    "tpValores"
]
