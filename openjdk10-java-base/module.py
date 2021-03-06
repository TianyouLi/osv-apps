#
# Copyright (C) 2014 Cloudius Systems, Ltd.
#
# This work is open source software, licensed under the terms of the
# BSD license as described in the LICENSE file in the top-level directory.
#

from osv.modules.filemap import FileMap
from osv.modules import api

api.require('java-non-isolated')
provides = ['java','java8','java9','java10']

usr_files = FileMap()
usr_files.add('${OSV_BASE}/apps/openjdk10-java-base/install').to('/').allow_symlink()
usr_files.add('${OSV_BASE}/apps/openjdk10-java-base/install/usr/lib/jvm/java') \
    .to('/usr/lib/jvm/java') \
    .allow_symlink()
