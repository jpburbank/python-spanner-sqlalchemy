# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .. import create_table


def test_create_table(capsys, db_url, random_table_id):
    table = create_table.create_table(db_url, random_table_id)
    out, err = capsys.readouterr()
    assert "created successfully" in out
    assert table.name == random_table_id
    assert table.exists() is True

    table.drop()
