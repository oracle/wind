## Copyright © 2021, Oracle and/or its affiliates.
## Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.

""" Library for Oracle integration """

import base64

import json

import requests

import urllib3
from robot.api import logger
from robot.api.deco import keyword
from urllib3.exceptions import HTTPError

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Marketplace:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self, verify_ssl=False):
        """Initialize an Instance of OCI Marketplace class."""
        self.auth_token = ""
        self.params = {}
        self.apis = {}
        self.username = ""
        self.base_api_url = ""
        self.max_records = 50
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-type": "application/x-www-form-urlencoded",
                "charset": "UTF-8",
                "X-USER-IDENTITY-DOMAIN-NAME": "usoracle30650",
                "cache-control": "no-cache",
            }
        )

    @keyword("Generate Auth Token", tags=["Common", "Login"])
    def generate_auth_token(
        self, base_api_url, client_id, secret_key, username, max_records=None
    ):
        """Generate Auth Token for OCI Marketplace APIs."""
        self.base_api_url = base_api_url
        self.username = username
        self._initialize_apis(Marketplace.api_url(self.base_api_url))
        auth_string = client_id + ":" + secret_key
        encoded = base64.b64encode(auth_string.encode("ascii"))
        encoded_string = encoded.decode("ascii")
        self.session.headers.update({"Authorization": f"Basic {encoded_string}"})
        response = self.session.get(self.apis["auth"])
        if response.status_code >= 200 and response.status_code < 300:
            self.auth_token = json.loads(response.text).get("access_token")
            if max_records:
                self.max_records = max_records
            self.params["limit"] = self.max_records
            self.session.headers.update(
                {
                    "Content-type": "application/json",
                    "Authorization": f"Bearer {self.auth_token}",
                    "X-Oracle-UserId": self.username,
                }
            )
            return self.auth_token
        else:
            raise Exception(json.loads(response.text))

    @keyword("List OCI Tenancies", tags=["Common", "Tenancies"])
    def list_oci_tenancies(self):
        """List OCI Tenancies present in your Marketplace Publisher Account."""
        response = self.session.get(self.apis["tenancies"], params=self.params)
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Create OCI Tenancy", tags=["Common", "Tenancy"])
    def create_oci_tenancy(
        self, tenancy_name, tenancy_ocid, tenancy_home_region_code, compartment_ocid
    ):
        """Add OCI Tenancy to your Marketplace Publisher Account."""
        tenancy_data = {
            "tenancyName": tenancy_name,
            "tenancyOCID": tenancy_ocid,
            "homeRegion": tenancy_home_region_code,
            "appCatalogSetting": {"compartmentOCID": compartment_ocid},
        }
        response = self.session.post(
            self.apis["tenancies"], data=json.dumps(tenancy_data)
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Update OCI Tenancy", tags=["Common", "Tenancy"])
    def update_oci_tenancy(
        self,
        tenancy_id,
        tenancy_name=None,
        tenancy_ocid=None,
        tenancy_home_region_code=None,
        compartment_ocid=None,
    ):
        """Update OCI Tenancy to your Marketplace Publisher Account."""
        tenancy_data = {}
        tenancy_data = {
            "tenancyName": tenancy_name,
            "tenancyOCID": tenancy_ocid,
            "homeRegion": tenancy_home_region_code,
            "appCatalogSetting": {"compartmentOCID": compartment_ocid},
        }
        response = self.session.put(
            self.apis["tenancies"] + "/" + tenancy_id, data=json.dumps(tenancy_data)
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Get Tenancy Details", tags=["Common", "Tenancy"])
    def get_tenancy_details(self, tenancy_id):
        """Get OCI Tenancy Details from Marketplace Publisher Account."""
        response = self.session.get(
            self.apis["tenancies"] + "/" + tenancy_id,
            params=self.params,
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(
                '> WIND ERROR :: Tenancy with ID "{}" is not found in the system'.format(
                    tenancy_id
                )
            )

    @keyword("Delete Tenancy", tags=["Common", "Tenancy"])
    def delete_tenancy(self, tenancy_id):
        """Delete Particular Tenancy from Marketplace Publisher Account."""
        response = self.session.delete(
            self.apis["tenancies"] + "/" + tenancy_id,
            params=self.params,
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Get Tenancy Compute Images", tags=["Common", "Tenancy"])
    def get_tenancy_compute_images(
        self, tenancy_id, tenancy_home_region_code, compartment_ocid
    ):
        """Get OCI Tenancy Compute Images from Marketplace Publisher Account."""
        response = self.session.get(
            self.apis["tenancies"]
            + "/"
            + tenancy_id
            + "/computeimages"
            + "?regionCode="
            + tenancy_home_region_code
            + "&compartmentOCID="
            + compartment_ocid,
            params=self.params,
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Create Terms of Use", tags=["Common", "Terms"])
    def create_terms_of_use(self, version_value, term_file_path):
        """Create New Terms which are exposed to end users."""
        with open(term_file_path, "r") as term_file:
            term_value = term_file.read()
        term_data = {
            "versionName": version_value,
            "contentDescription": term_value,
        }
        term_file.close()
        response = self.session.post(self.apis["terms"], data=json.dumps(term_data))
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Create New Version of Terms of Use", tags=["Common", "Terms"])
    def create_terms_version(self, terms_id, version_value, term_file_path):
        """Create Existing Term version which are exposed to end users."""
        with open(term_file_path, "r") as term_file:
            term_value = term_file.read()
        term_data = {
            "versionName": version_value,
            "contentDescription": term_value,
        }
        term_file.close()
        response = self.session.post(
            self.apis["terms"] + "/" + terms_id + "/version", data=json.dumps(term_data)
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Get All Terms of Use", tags=["Common", "Terms"])
    def get_all_terms_of_use(self):
        """Create New Terms which are exposed to end users."""
        response = self.session.get(self.apis["terms"])
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Get Terms Version", tags=["Common", "Terms"])
    def get_terms_of_use(self, terms_id, terms_version_id):
        """Create New Terms which are exposed to end users."""
        response = self.session.get(
            self.apis["terms"] + "/" + terms_id + "/version/" + terms_version_id
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Update Version of Terms of Use", tags=["Common", "Terms"])
    def update_terms_of_use(self, version_value, term_file_path, terms_id):
        """Update New Terms which are exposed to end users."""
        with open(term_file_path, "r") as term_file:
            term_value = term_file.read()
        term_data = {
            "versionName": version_value,
            "contentDescription": term_value,
        }
        term_file.close()
        response = self.session.post(
            self.apis["terms"] + "/" + terms_id, data=json.dumps(term_data)
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Delete Version of Terms of Use", tags=["Common", "Terms"])
    def delete_terms_of_use(self, terms_id, terms_version_id):
        """Delete New Terms which are exposed to end users."""
        response = self.session.delete(
            self.apis["terms"] + "/" + terms_id + "/version/" + terms_version_id
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Activate Terms of Use", tags=["Common", "Terms"])
    def activate_terms_of_use(self, terms_id):
        """Activate New Terms which are exposed to end users."""
        term_data = {"status": "ACTIVE"}
        response = self.session.patch(
            self.apis["terms"] + "/" + terms_id, data=json.dumps(term_data)
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Deactivate Terms of Use", tags=["Common", "Terms"])
    def deactivate_terms_of_use(self, terms_id):
        """Activate New Terms which are exposed to end users."""
        term_data = {"status": "INACTIVE"}
        response = self.session.patch(
            self.apis["terms"] + "/" + terms_id, data=json.dumps(term_data)
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("List All Artifacts", tags=["Common", "Artifacts"])
    def list_all_artifacts(self, limit=None):
        """List All Artifacts."""
        api_path = ""
        if limit:
            api_path = "?&limit=" + limit
        else:
            api_path = "?&limit=" + str(self.max_records)
        response = self.session.get(self.apis["artifacts"] + api_path)
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("List Image Artifacts", tags=["Common", "Artifacts"])
    def list_image_artifacts(self, limit=None):
        """List Image Artifacts."""
        api_path = ""
        if limit:
            api_path = "?artifactType=OCI_COMPUTE_IMAGE&limit=" + limit
        else:
            api_path = "?artifactType=OCI_COMPUTE_IMAGE"
        response = self.session.get(self.apis["artifacts"] + api_path)
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("List Stack Artifacts", tags=["Common", "Artifacts"])
    def list_stack_artifacts(self, limit=None):
        """List Stack Artifacts."""
        api_path = ""
        if limit:
            api_path = "?artifactType=TERRAFORM_TEMPLATE&limit=" + limit
        else:
            api_path = "?artifactType=TERRAFORM_TEMPLATE"
        response = self.session.get(self.apis["artifacts"] + api_path)
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Create Image Artifact", tags=["Common", "Artifacts"])
    def create_image_artifact(
        self,
        artifact_name,
        artifact_region_code_name,
        artifact_image_ocid,
        compartment_ocid,
        tenancy_id,
        compatible_shapes,
    ):
        """Create Image Artifact and It returns message Ok value with artifact ID."""
        shapes = {}
        compatible_shapes_list = []
        for each in compatible_shapes.split(","):
            shapes["shape"] = each
            compatible_shapes_list.append(dict(shapes))
        artifact_data = {
            "name": artifact_name,
            "artifactType": "OCI_COMPUTE_IMAGE",
            "source": {
                "regionCode": artifact_region_code_name,
                "uniqueIdentifier": artifact_image_ocid,
            },
            "artifactProperties": [
                {
                    "artifactTypePropertyName": "compartmentOCID",
                    "value": compartment_ocid,
                },
                {"artifactTypePropertyName": "ociTenancyID", "value": tenancy_id},
            ],
            "compatibleShapes": compatible_shapes_list,
        }
        response = self.session.post(
            self.apis["artifacts"], data=json.dumps(artifact_data)
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Create Stack Artifact", tags=["Common", "Artifacts"])
    def create_stack_artifact(
        self, artifact_name, artifact_file_name, artifact_file_path
    ):
        """Create Artifact."""
        payload = {}
        files = [
            (
                "file",
                (artifact_file_name, open(artifact_file_path, "rb"), "application/zip"),
            )
        ]
        payload = {
            "json": '{"name": "artifact_name123" ,"artifactType":"TERRAFORM_TEMPLATE"}'
        }
        update_artifact = json.loads(payload["json"])
        update_artifact["name"] = artifact_name
        payload = {"json": json.dumps(update_artifact)}
        del self.session.headers["Content-type"]
        response = self.session.post(self.apis["artifacts"], data=payload, files=files)
        if response.status_code >= 200 and response.status_code < 300:
            self.session.headers.update({"Content-type": "application/json"})
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Get Artifact Details", tags=["Common", "Artifact"])
    def get_artificat_details(self, artifact_id):
        """Get Artifact Details."""
        response = self.session.get(self.apis["artifacts"] + "/" + artifact_id)
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Delete Artifact", tags=["Common", "Artifact"])
    def delete_artifact(self, artifact_id):
        """Delete Artifact Details by ID."""
        response = self.session.delete(self.apis["artifacts"] + "/" + artifact_id)
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("List Applications", tags=["Common", "Applications"])
    def list_applications(self, status=None):
        """List Applications."""
        query_params = "?"
        if status:
            query_params += "status=" + status
        response = self.session.get(
            self.apis["applications"] + query_params, params=self.params
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Create Application", tags=["Common", "Application"])
    def create_oci_application_listing(
        self,
        name,
        short_description,
        long_description,
        usage_information,
        tags,
        pricing_type,
        cataegory_name,
        tag_line,
        demo_url=None,
        version_number=None,
        version_description=None,
        release_date=None,
        support_contact_name=None,
        support_contact_email=None,
        support_contact_subject=None,
        support_link_name=None,
        system_requirements_details=None,
        support_link_url=None,
        support_contact_phone=None,
    ):
        """Create Application."""
        list_data = {
            "name": name,
            "shortDescription": short_description,
            "longDescription": long_description,
            "usageInformation": usage_information,
            "tags": tags,
            "tagLine": tag_line,
            "versionDetails": {
                "versionNumber": version_number,
                "description": version_description,
                "releaseDate": release_date,
            },
            "languages": [{"code": "en_US"}],
            "products": [
                {"code": "oci", "categories": [{"code": cataegory_name}]},
            ],
            "deviceType": {"code": "BROWSER"},
            "demoURL": demo_url,
            "markets": [
                {
                    "code": "US",
                    "name": "US Commercial",
                    "category": "Commercial",
                    "billToCountries": ["United States"],
                }
            ],
            "downloadInfo": {"type": "TEXT", "value": "getapp"},
            "systemRequirements": system_requirements_details,
        }
        if support_contact_name:
            list_data["support"] = {
                "contacts": [
                    {
                        "name": support_contact_name,
                        "phone": support_contact_phone,
                        "email": support_contact_email,
                        "subject": support_contact_subject,
                    }
                ],
                "links": [{"name": support_link_name, "url": support_link_url}],
            }
        if pricing_type == "PAYGO":
            list_data["pricing"] = {
                "type": pricing_type,
                "name": "PAID",
                "ociListing": True,
            }
        if pricing_type == "BYOL":
            list_data["pricing"] = {
                "type": pricing_type,
                "name": "BYOL",
                "ociListing": True,
            }
        if pricing_type == "FREE":
            list_data["pricing"] = {
                "type": pricing_type,
                "name": "Free",
                "ociListing": True,
            }
        response = self.session.post(
            self.apis["applications"], data=json.dumps(list_data)
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword(
        "Add Image Artifact to Application Package",
        tags=["Common", "Application", "Package"],
    )
    def add_image_artifact_to_application_package(
        self, application_name, package_id, image_artifact_name, image_artifact_id
    ):
        """Add Image Artifact to Application Package."""
        applications = self.list_applications()
        json_dict = {}
        json_dict = {
            "service": "OCI",
            "resources": [
                {
                    "serviceType": "OCI",
                    "type": "ocimachineimage",
                    "properties": [
                        {
                            "name": "artifact",
                            "value": image_artifact_id,
                            "valueProperties": [
                                {"name": "name", "value": image_artifact_name}
                            ],
                        }
                    ],
                }
            ],
        }
        files = {"json": json.dumps(json_dict)}
        for value in applications["items"]:
            if value["listingSummary"]["name"] == application_name:
                del self.session.headers["Content-type"]
                response = self.session.put(
                    self.apis["packages"]
                    + "/"
                    + str(value["listingSummary"]["listingVersionId"])
                    + "/packages"
                    + "/"
                    + package_id,
                    files=files,
                )
                if response.status_code >= 200 and response.status_code < 300:
                    self.session.headers.update({"Content-type": "application/json"})
                    return json.loads(response.text)
                else:
                    raise Exception(json.loads(response.text))
        raise Exception(
            '> WIND ERROR :: Application with Name "{}" is not found in the system'.format(
                application_name
            )
        )

    @keyword(
        "Add Stack Artifact to Application Package",
        tags=["Common", "Application", "Package"],
    )
    def add_stack_artifact_to_application_package(
        self, application_name, package_id, stack_artifact_id, stack_artifact_name
    ):
        """Add Stack Artifact to Application Package."""
        applications = self.list_applications()
        json_dict = {}
        json_dict = {
            "service": "OCIOrchestration",
            "resources": [
                {
                    "serviceType": "OCIOrchestration",
                    "type": "terraform",
                    "properties": [
                        {
                            "name": "artifact",
                            "value": stack_artifact_id,
                            "valueProperties": [
                                {"name": "name", "value": stack_artifact_name}
                            ],
                        }
                    ],
                }
            ],
        }
        files = {"json": json.dumps(json_dict)}
        for value in applications["items"]:
            if value["listingSummary"]["name"] == application_name:
                del self.session.headers["Content-type"]
                response = self.session.put(
                    self.apis["packages"]
                    + "/"
                    + str(value["listingSummary"]["listingVersionId"])
                    + "/packages"
                    + "/"
                    + package_id,
                    files=files,
                )
                if response.status_code >= 200 and response.status_code < 300:
                    self.session.headers.update({"Content-type": "application/json"})
                    return json.loads(response.text)
                else:
                    raise Exception(json.loads(response.text))
        raise Exception(
            '> WIND ERROR :: Application with Name "{}" is not found in the system'.format(
                application_name
            )
        )

    @keyword("Create Application Package", tags=["Common", "Application", "Package"])
    def create_application_package(
        self,
        application_name,
        description,
        version,
        package_type,
        terms_id,
        is_security_fix=None,
    ):
        """Create Application Package."""
        applications = self.list_applications()
        json_dict = {}
        json_dict = {
            "description": description,
            "version": version,
            "serviceType": package_type,
            "namespacePrefix": "",
            "tncId": terms_id,
            "isSecurityFix": True if is_security_fix == "YES" else False,
        }
        files = {"json": json.dumps(json_dict)}
        for value in applications["items"]:
            if value["listingSummary"]["name"] == application_name:
                del self.session.headers["Content-type"]
                response = self.session.post(
                    self.apis["packages"]
                    + "/"
                    + str(value["listingSummary"]["listingVersionId"])
                    + "/packages",
                    files=files,
                )
                if response.status_code >= 200 and response.status_code < 300:
                    self.session.headers.update({"Content-type": "application/json"})
                    return json.loads(response.text)
                else:
                    raise Exception(json.loads(response.text))
        raise Exception(
            '> WIND ERROR :: Application with Name "{}" is not found in the system'.format(
                application_name
            )
        )

    @keyword("Delete Application Package", tags=["Common", "Application", "Package"])
    def delete_application_package(self, application_name, package_id):
        """Delete Application Package."""
        applications = self.list_applications()
        for value in applications["items"]:
            if value["listingSummary"]["name"] == application_name:
                del self.session.headers["Content-type"]
                response = self.session.delete(
                    self.apis["packages"]
                    + "/"
                    + str(value["listingSummary"]["listingVersionId"])
                    + "/packages"
                    + "/"
                    + package_id
                )
                if response.status_code >= 200 and response.status_code < 300:
                    self.session.headers.update({"Content-type": "application/json"})
                    return json.loads(response.text)
                else:
                    raise Exception(json.loads(response.text))
        raise Exception(
            '> WIND ERROR :: Application with Name "{}" is not found in the system'.format(
                application_name
            )
        )

    @keyword("Get Application Packages", tags=["Common", "Application", "Package"])
    def get_application_packages(
        self,
        application_name,
    ):
        """Get Application Packages."""
        applications = self.list_applications()
        for value in applications["items"]:
            if value["listingSummary"]["name"] == application_name:
                response = self.session.get(
                    self.apis["packages"]
                    + "/"
                    + str(value["listingSummary"]["listingVersionId"])
                    + "/packages"
                )
                if response.status_code >= 200 and response.status_code < 300:
                    return json.loads(response.text)
                else:
                    raise Exception(json.loads(response.text))
        raise Exception(
            '> WIND ERROR :: Application with Name "{}" is not found in the system'.format(
                application_name
            )
        )

    @keyword("Add Application Icon", tags=["Common", "Application"])
    def add_application_icon(self, application_name, icon_file_name, icon_path):
        """Add Logo Icon to Application."""
        applications = self.list_applications()
        payload = {}
        for value in applications["items"]:
            if value["listingSummary"]["name"] == application_name:
                files = [
                    ("image", (icon_file_name, open(icon_path, "rb"), "image/png"))
                ]
                del self.session.headers["Content-type"]
                response = self.session.post(
                    self.apis["applications"]
                    + "/"
                    + str(value["listingSummary"]["listingVersionId"])
                    + "/icon",
                    data=payload,
                    files=files,
                )
                if response.status_code >= 200 and response.status_code < 300:
                    self.session.headers.update({"Content-type": "application/json"})
                    return json.loads(response.text)
                else:
                    raise Exception(json.loads(response.text))
        raise Exception(
            '> WIND ERROR :: Application with Name "{}" is not found in the system'.format(
                application_name
            )
        )

    @keyword("Add Application Banner", tags=["Common", "Application"])
    def add_application_banner(
        self, application_name, banner_name, icon_file_name, icon_path
    ):
        """Add Banner to Application."""
        applications = self.list_applications()
        payload = {"json": '{"name": "banner_name"}'}
        update_banner = json.loads(payload["json"])
        update_banner["name"] = banner_name
        payload = {"json": json.dumps(update_banner)}
        for value in applications["items"]:
            if value["listingSummary"]["name"] == application_name:
                files = [("file", (icon_file_name, open(icon_path, "rb"), "image/png"))]
                del self.session.headers["Content-type"]
                response = self.session.post(
                    self.apis["applications"]
                    + "/"
                    + str(value["listingSummary"]["listingVersionId"])
                    + "/banner",
                    data=payload,
                    files=files,
                )
                if response.status_code >= 200 and response.status_code < 300:
                    self.session.headers.update({"Content-type": "application/json"})
                    return json.loads(response.text)
                else:
                    raise Exception(json.loads(response.text))

        raise Exception(
            '> WIND ERROR :: Application with Name "{}" is not found in the system'.format(
                application_name
            )
        )

    @keyword("Create Application Version", tags=["Common", "Application"])
    def create_application_version(self, application_id):
        """Get Application."""
        response = self.session.post(
            self.apis["applications"] + "/" + application_id + "/version",
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Get Application Details", tags=["Common", "Application"])
    def get_application_details(self, application_name):
        """Get Application."""
        applications = self.list_applications()
        for value in applications["items"]:
            if value["listingSummary"]["name"] == application_name:
                return value

        raise Exception(
            '> WIND ERROR :: Application with Name "{}" is not found in the system'.format(
                application_name
            )
        )

    @keyword("Get Application Status", tags=["Common", "Application"])
    def get_application_status(self, application_name):
        """Get Application Status."""
        applications = self.list_applications()
        for value in applications["items"]:
            if value["listingSummary"]["name"] == application_name:
                return value["listingSummary"]["status"]

        raise Exception(
            '> WIND ERROR :: Application with Name "{}" is not found in the system'.format(
                application_name
            )
        )

    @keyword("Submit Application", tags=["Common", "Application"])
    def submit_application(self, application_name, submitting_note):
        """Submit Application."""
        applications = self.list_applications()
        for value in applications["items"]:
            if value["listingSummary"]["name"] == application_name:
                submit_data = {
                    "action": "submit",
                    "note": submitting_note,
                }
                response = self.session.patch(
                    self.apis["applications"]
                    + "/"
                    + str(value["listingSummary"]["listingVersionId"]),
                    data=json.dumps(submit_data),
                )
                if response.status_code >= 200 and response.status_code < 300:
                    return json.loads(response.text)
                else:
                    raise Exception(json.loads(response.text))

        raise Exception(
            '> WIND ERROR :: Application with Name "{}" is not found in the system'.format(
                application_name
            )
        )

    @keyword("Publish Application", tags=["Common", "Application"])
    def publish_application_by_id(self, application_id):
        """Publish Application."""
        publish_data = {"action": "publish"}
        response = self.session.patch(
            self.apis["applications"] + "/" + application_id,
            data=json.dumps(publish_data),
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Withdraw Application", tags=["Common", "Application"])
    def withdraw_application_by_id(self, application_id):
        """Withdraw Application."""
        publish_data = {"action": "withdraw"}
        response = self.session.patch(
            self.apis["applications"] + "/" + application_id,
            data=json.dumps(publish_data),
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Delete Application", tags=["Common", "Application"])
    def delete_application(self, application_name):
        """Delete Application."""
        applications = self.list_applications()
        for value in applications["items"]:
            if value["listingSummary"]["name"] == application_name:
                response = self.session.delete(
                    self.apis["applications"]
                    + "/"
                    + str(value["listingSummary"]["listingVersionId"])
                )
                if response.status_code >= 200 and response.status_code < 300:
                    return json.loads(response.text)
                else:
                    raise Exception(json.loads(response.text))

        raise Exception(
            '> WIND ERROR :: Application with Name "{}" is not found in the system'.format(
                application_name
            )
        )

    @keyword("Get Application Install Requests", tags=["Common", "Requests"])
    def get_install_requests(
        self,
        install_status=None,
        request_on_range_start=None,
        request_on_range_end=None,
        listing_id=None,
    ):
        """Get Customer App Installs for your Published Listings"""
        query_params = "?"
        if install_status:
            query_params += "installstatus=" + install_status
        if request_on_range_start:
            query_params += "&requestedOnRangeStart=" + request_on_range_start
        if request_on_range_end:
            query_params += "&requestedOnRangeEnd=" + request_on_range_end
        if listing_id:
            query_params += "&listingid=" + listing_id
        response = self.session.get(self.apis["requests"] + query_params)
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Get Leads", tags=["Common", "Leads"])
    def get_leads(
        self,
        createdOnRangeStart=None,
        createdOnRangeEnd=None,
        orderby=None,
        sortorder=None,
        keywordValue=None,
        listingtype=None,
        status=None,
    ):
        """Get Leads Status."""
        query_params = "?"
        if createdOnRangeStart:
            query_params = "&createdonrangestart=" + createdOnRangeStart
        if createdOnRangeEnd:
            query_params += "&createdonrangeend=" + createdOnRangeEnd
        if orderby:
            query_params += "&orderby=" + orderby
        if sortorder:
            query_params += "&sortorder=" + sortorder
        if keywordValue:
            query_params += "&keyword=" + keywordValue
        if listingtype:
            query_params += "&listingtype=" + listingtype
        if status:
            query_params += "&status=" + status
        response = self.session.get(self.apis["leads"] + query_params)
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Get Leads Reports", tags=["Common", "Leads"])
    def get_lead_reports(
        self,
        group_by,
        time_type=None,
        createdOnRangeStart=None,
        createdOnRangeEnd=None,
    ):
        """Get Leads Reports."""
        query_params = "?"
        if group_by:
            query_params += "groupby=" + group_by
        if time_type and group_by.upper() == "DATE":
            query_params += "&timetype=" + time_type
        if createdOnRangeStart:
            query_params += "&createdonrangestart=" + createdOnRangeStart
        if createdOnRangeEnd:
            query_params += "&createdonrangeend=" + createdOnRangeEnd
        response = self.session.get(self.apis["leads"] + query_params)
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Create Lead Notes", tags=["Common", "Leads"])
    def create_lead_notes(self, lead_id, message):
        """Create Lead Notes."""
        note_message = {"note": message}
        response = self.session.post(
            self.apis["leads"] + "/" + lead_id + "/notes", data=json.dumps(note_message)
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("List Lead Notes", tags=["Common", "Leads"])
    def list_lead_notes(self, lead_id):
        """List Lead Notes."""
        response = self.session.get(self.apis["leads"] + "/" + lead_id + "/notes")
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Update Lead Status", tags=["Common", "Leads"])
    def update_lead_status(self, lead_id, status):
        """Update Lead Status."""
        lead_status = {"status": status}
        response = self.session.patch(
            self.apis["leads"] + "/" + lead_id, data=json.dumps(lead_status)
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @keyword("Delete Lead", tags=["Common", "Leads"])
    def delete_lead(self, lead_id):
        """Delete Lead."""
        response = self.session.delete(self.apis["leads"] + "/" + lead_id)
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
            raise Exception(json.loads(response.text))

    @staticmethod
    def api_url(base_api_url):
        """OCI Marketplace API Build URL."""
        return base_api_url

    def _initialize_apis(self, api_path):
        """Initialize APIs endpoints required for each keywords."""
        self.apis["auth"] = api_path + "/appstore/publisher/v1/authenticate"
        self.apis["tenancies"] = api_path + "/appstore/publisher/v1/ocitenancies"
        self.apis["applications"] = api_path + "/appstore/publisher/v1/applications"
        self.apis["artifacts"] = api_path + "/appstore/publisher/v1/artifacts"
        self.apis["leads"] = api_path + "/appstore/publisher/v1/leads"
        self.apis["terms"] = api_path + "/appstore/publisher/v1/terms"
        self.apis["requests"] = api_path + "/appstore/publisher/v1/installrequests"
        self.apis["packages"] = api_path + "/appstore/publisher/v2/applications"
