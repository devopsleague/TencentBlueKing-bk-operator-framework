"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2023 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

import sys

from bk_operator_framework.generator.cli_actions import echo
from bk_operator_framework.generator.kits import template
from bk_operator_framework.generator.project import project


def main(domain: str) -> None:
    echo.info("Writing scaffold for you to edit...")
    if project.is_initialized:
        echo.fata("Failed to initialize project: already initialized")
        echo.info("Next: define a resource with:\n$ bof create api")
        sys.exit(1)

    template.init_project_dir()

    project.init_basc_info(domain)
    project.render_desc_file()

    echo.info("Project initialization completed!")
    echo.info("Update dependencies:\n$ pip install -r requirements.txt")
    echo.info("Next: define a resource with:\n$ bof create api")
