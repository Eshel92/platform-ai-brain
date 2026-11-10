<!-- Converted from management/field-formatters/string-formatter.asciidoc (AsciiDoc). Includes are inlined. -->

The *String* field formatter enables you to apply transforms to the field.

Supported transformations include:

* Convert to lowercase

* Convert to uppercase

* Convert to title case

* Apply the short dots transformation, which replaces the content before the `.` character with the first character of
the content. For example:

*Original*:: *Becomes*
`com.organizations.project.ClassName`:: `c.o.p.ClassName`

* Base64 decode

* URL param decode
