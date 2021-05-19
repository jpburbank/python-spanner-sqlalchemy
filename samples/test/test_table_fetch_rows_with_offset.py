# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from .. import table_fetch_rows_with_offset


def test_table_fetch_rows_with_offset(capsys, table_id):
    rows = table_fetch_rows_with_offset.fetch_rows_with_offset(table_id)

    out, err = capsys.readouterr()
    assert "The rows are:" in out
    assert len(rows) is 3
