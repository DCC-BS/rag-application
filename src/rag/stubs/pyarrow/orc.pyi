"""
This type stub file was generated by pyright.
"""

class ORCFile:
    """
    Reader interface for a single ORC file

    Parameters
    ----------
    source : str or pyarrow.NativeFile
        Readable source. For passing Python file objects or byte buffers,
        see pyarrow.io.PythonFileInterface or pyarrow.io.BufferReader.
    """
    def __init__(self, source) -> None: ...
    @property
    def metadata(self):
        """The file metadata, as an arrow KeyValueMetadata"""
        ...

    @property
    def schema(self):
        """The file schema, as an arrow schema"""
        ...

    @property
    def nrows(self):
        """The number of rows in the file"""
        ...

    @property
    def nstripes(self):
        """The number of stripes in the file"""
        ...

    @property
    def file_version(self):
        """Format version of the ORC file, must be 0.11 or 0.12"""
        ...

    @property
    def software_version(self):
        """Software instance and version that wrote this file"""
        ...

    @property
    def compression(self):
        """Compression codec of the file"""
        ...

    @property
    def compression_size(self):
        """Number of bytes to buffer for the compression codec in the file"""
        ...

    @property
    def writer(self):
        """Name of the writer that wrote this file.
        If the writer is unknown then its Writer ID
        (a number) is returned"""
        ...

    @property
    def writer_version(self):
        """Version of the writer"""
        ...

    @property
    def row_index_stride(self):
        """Number of rows per an entry in the row index or 0
        if there is no row index"""
        ...

    @property
    def nstripe_statistics(self):
        """Number of stripe statistics"""
        ...

    @property
    def content_length(self):
        """Length of the data stripes in the file in bytes"""
        ...

    @property
    def stripe_statistics_length(self):
        """The number of compressed bytes in the file stripe statistics"""
        ...

    @property
    def file_footer_length(self):
        """The number of compressed bytes in the file footer"""
        ...

    @property
    def file_postscript_length(self):
        """The number of bytes in the file postscript"""
        ...

    @property
    def file_length(self):
        """The number of bytes in the file"""
        ...

    def read_stripe(self, n, columns=...):
        """Read a single stripe from the file.

        Parameters
        ----------
        n : int
            The stripe index
        columns : list
            If not None, only these columns will be read from the stripe. A
            column name may be a prefix of a nested field, e.g. 'a' will select
            'a.b', 'a.c', and 'a.d.e'

        Returns
        -------
        pyarrow.RecordBatch
            Content of the stripe as a RecordBatch.
        """
        ...

    def read(self, columns=...):
        """Read the whole file.

        Parameters
        ----------
        columns : list
            If not None, only these columns will be read from the file. A
            column name may be a prefix of a nested field, e.g. 'a' will select
            'a.b', 'a.c', and 'a.d.e'. Output always follows the
            ordering of the file and not the `columns` list.

        Returns
        -------
        pyarrow.Table
            Content of the file as a Table.
        """
        ...

_orc_writer_args_docs = ...

class ORCWriter:
    __doc__ = ...
    is_open = ...
    def __init__(
        self,
        where,
        *,
        file_version=...,
        batch_size=...,
        stripe_size=...,
        compression=...,
        compression_block_size=...,
        compression_strategy=...,
        row_index_stride=...,
        padding_tolerance=...,
        dictionary_key_size_threshold=...,
        bloom_filter_columns=...,
        bloom_filter_fpp=...,
    ) -> None: ...
    def __del__(self):  # -> None:
        ...
    def __enter__(self):  # -> Self:
        ...
    def __exit__(self, *args, **kwargs):  # -> None:
        ...
    def write(self, table):  # -> None:
        """
        Write the table into an ORC file. The schema of the table must
        be equal to the schema used when opening the ORC file.

        Parameters
        ----------
        table : pyarrow.Table
            The table to be written into the ORC file
        """
        ...

    def close(self):  # -> None:
        """
        Close the ORC file
        """
        ...

def read_table(source, columns=..., filesystem=...): ...
def write_table(
    table,
    where,
    *,
    file_version=...,
    batch_size=...,
    stripe_size=...,
    compression=...,
    compression_block_size=...,
    compression_strategy=...,
    row_index_stride=...,
    padding_tolerance=...,
    dictionary_key_size_threshold=...,
    bloom_filter_columns=...,
    bloom_filter_fpp=...,
):  # -> None:
    ...
