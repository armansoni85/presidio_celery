"""Predefined recognizers package. Holds all the default recognizers."""

from presidio_analyzer.predefined_recognizers.transformers_recognizer import (
    TransformersRecognizer,
)
from .aba_routing_recognizer import AbaRoutingRecognizer
from .credit_card_recognizer import CreditCardRecognizer
from .crypto_recognizer import CryptoRecognizer
from .date_recognizer import DateRecognizer
from .email_recognizer import EmailRecognizer
from .es_nif_recognizer import EsNifRecognizer
from .iban_recognizer import IbanRecognizer
from .ip_recognizer import IpRecognizer
from .it_driver_license_recognizer import ItDriverLicenseRecognizer
from .it_fiscal_code_recognizer import ItFiscalCodeRecognizer
from .it_identity_card_recognizer import ItIdentityCardRecognizer
from .it_passport_recognizer import ItPassportRecognizer
from .it_vat_code import ItVatCodeRecognizer
from .medical_license_recognizer import MedicalLicenseRecognizer
from .phone_recognizer import PhoneRecognizer
from .sg_fin_recognizer import SgFinRecognizer
from .spacy_recognizer import SpacyRecognizer
from .stanza_recognizer import StanzaRecognizer
from .uk_nhs_recognizer import NhsRecognizer
from .url_recognizer import UrlRecognizer
from .us_bank_recognizer import UsBankRecognizer
from .us_driver_license_recognizer import UsLicenseRecognizer
from .us_itin_recognizer import UsItinRecognizer
from .us_passport_recognizer import UsPassportRecognizer
from .us_ssn_recognizer import UsSsnRecognizer
from .au_abn_recognizer import AuAbnRecognizer
from .au_acn_recognizer import AuAcnRecognizer
from .au_tfn_recognizer import AuTfnRecognizer
# from .au_medicare_recognizer import AuMedicareRecognizer
# from .in_pan_recognizer import InPanRecognizer
from .pl_pesel_recognizer import PlPeselRecognizer
from .azure_ai_language import AzureAILanguageRecognizer
from .in_aadhaar_recognizer import InAadhaarRecognizer
from .in_vehicle_registration_recognizer import InVehicleRegistrationRecognizer
from .medical_number_recognizer import MedicalNumberRecognizer
from .medical_record_number_recognizer import MedicalRecordNumberRecognizer
from .date_of_birth_recognizer import DateOfBirthRecognizer
from .encounter_number_recognizer import EncounterNumberRecognizer
from .word_list_recognizer import WordlistRecognizer
from .health_insurance_claim_number_recognizer import HICNRecognizer
from .australia_bank_account_numbers_recognizer import AustraliaBankAccountRecognizer
from .bank_state_branch_code_recognizer import BSBCodeRecognizer
# from .australiabusiness_and_companynumbers_recognizer import AustraliaBusinessCompanyNumberRecognizer
from .australia_medicare_card_numbers_recognizer import AustraliaMedicareCardRecognizer
from .au_bic_swift_numbers_reconizer import AustraliaBICRecognizer
from .canada_bic_swift_numbers_reconizer import CanadaBICRecognizer
from .canada_driving_license_recognizer import CanadaDriversLicenceRecognizer
from .canada_social_insurance_numbers_recognizer import CanadaSINRecognizer
from .france_national_identification_numbers_recognizer import FranceNationalIdRecognizer
from .france_driving_licence_numbers_recognizer import FranceDriversLicenceRecognizer
from .hipaa_and_hitech_drug_recognizer import DrugRecognizer
from .hipaa_and_hitech_ingredients_recognizer import IngredientRecognizer
from .hipaa_and_hitech_ICD9_recognizer import ICD9Recognizer
from .hipaa_and_hitech_ICD10_recognizer import ICD10Recognizer
from .us_pin_recognizer import PatientIDRecognizer
from .hipaa_and_hitech_low_threshold_recognizer import LowThresholdHIPAARecognizer
from .business_terminology_recognizer import BusinessTerminologyRecognizer
from .us_formatted_ssn import US_Formatted_SSN_Recognizer
from .us_privacy_et_SSNTIN_recognizer import SSNAndTINRecognizer
# from .hipaa_and_hitech_high import UnifiedRecognizer
from .us_privacy_formatted_and_unformatted_ssn import SSN_Formatted_Unformatted_Recognizer
from .germany_driving_licence_numbers_recognizer import GermanDriversLicenseRecognizer
from .germany_national_identification_number_recognizer import GermanIDCardRecognizer
from .germany_passport_numbers_recognizer import GermanPassportRecognizer
from .german_iban_number_recognizer import GermanIBANRecognizer
from .german_vat_number_recognizer import GermanVATRecognizer
from .us_et_ferpa import FerpaRecognizer
from .all_credit_card_number_recognizer import AllCreditCardNumberRecognizer
from .cc_numbers_Issuer_recognizer import CreditCardIssuerRecognizer
from .cc_track_data_attachments_recognizer import CCTrackDataRecognizer
from .us_driving_license_number_recognizer import USDriversLicenseRecognizer
from .italy_BIC_swift_number_recognizer import ItalyBICSwiftRecognizer
from .us_PCI_DSS_recognizer import PCI_DSS_CreditCardAndTrackDataRecognizer
from .us_AZSB1338_recognizer import US_AZSB1338Recognizer
from .ca_CASB1386_recognizer import CASB1386Recognizer
from .us_COHB1119_recognizer import COHB1119Recognizer
from .us_CTSB650_recognizer import ConnecticutDLPRecognizer
from .us_DCCB16810_recognizer import ColumbiaDLPRecognizer
from .us_FLHB481_recognizer import FLHB481Recognizer
from .us_IDSB1374_recognizer import IdahoSB1374Recognizer
from .us_LASB205_recognizer import LouisianaRecognizer
from .us_MASS201_recognizer import MassachusettsDataRecognizer
from .us_HF2121_recognizer import MinnesotaRecognizer
from .us_NVSB347_recognizer import NevadaRecognizer
from .us_NJA4001_recognizer import NewJerseyDLPRecognizer
from .us_NHHB1660_recognizer import NewHampshirePolicyRecognizer
from .us_NYAB4254_recognizer import NewYorkDataRecognizer
from .us_OHHB104_recognizer import OhioDataRecognizer
from .us_OKHB2357_recognizer import OklahomaRecognizer
from .us_PASB712_recognizer import PennsylvaniaRecognizer
from .us_TXSB122_recognizer import TexasPolicyRecognizer
from .us_UTSB69_recognizer import UtahPolicyRecognizer
from .us_WASB6043_recognizer import WashingtonStateRecognizer

NLP_RECOGNIZERS = {
    "spacy": SpacyRecognizer,
    "stanza": StanzaRecognizer,
    "transformers": TransformersRecognizer,
}

__all__ = [
    "AbaRoutingRecognizer",
    "CreditCardRecognizer",
    "CryptoRecognizer",
    "DateRecognizer",
    "EmailRecognizer",
    "IbanRecognizer",
    "IpRecognizer",
    "NhsRecognizer",
    "MedicalLicenseRecognizer",
    "PhoneRecognizer",
    "SgFinRecognizer",
    "UrlRecognizer",
    "UsBankRecognizer",
    "UsItinRecognizer",
    "UsLicenseRecognizer",
    "UsPassportRecognizer",
    "UsSsnRecognizer",
    "EsNifRecognizer",
    "SpacyRecognizer",
    "StanzaRecognizer",
    "NLP_RECOGNIZERS",
    "AuAbnRecognizer",
    "AuAcnRecognizer",
    "AuTfnRecognizer",
    #"AuMedicareRecognizer",
    "TransformersRecognizer",
    "ItDriverLicenseRecognizer",
    "ItFiscalCodeRecognizer",
    "ItVatCodeRecognizer",
    "ItIdentityCardRecognizer",
    "ItPassportRecognizer",
    # "InPanRecognizer",
    "PlPeselRecognizer",
    "AzureAILanguageRecognizer",
    "InAadhaarRecognizer",
    "InVehicleRegistrationRecognizer",
    "MedicalNumberRecognizer",
    "MedicalRecordNumberRecognizer",
    "DateOfBirthRecognizer",
    "EncounterNumberRecognizer",
    "WordlistRecognizer",
    "HICNRecognizer",
    "AustraliaBankAccountRecognizer",
    "BSBCodeRecognizer",
    # "AustraliaBusinessCompanyNumberRecognizer",
    "AustraliaMedicareCardRecognizer",
    "AustraliaBICRecognizer",
    "CanadaBICRecognizer",
    "CanadaDriversLicenceRecognizer",
    "CanadaSINRecognizer",
    "FranceNationalIdRecognizer",
    "FranceDriversLicenceRecognizer",
    "DrugRecognizer",
    "IngredientRecognizer",
    "ICD9Recognizer",
    "ICD10Recognizer",
    "PatientIDRecognizer",
    "LowThresholdHIPAARecognizer",
    "BusinessTerminologyRecognizer",
    "US_Formatted_SSN_Recognizer",
    # "UnifiedRecognizer",
    "SSNAndTINRecognizer",
    "SSN_Formatted_Unformatted_Recognizer",
    "GermanDriversLicenseRecognizer",
    "GermanIDCardRecognizer",
    "GermanPassportRecognizer",
    "GermanIBANRecognizer",
    "GermanVATRecognizer",
    "FerpaRecognizer",
    "AllCreditCardNumberRecognizer",
    "CreditCardIssuerRecognizer",
    "CCTrackDataRecognizer",
    "USDriversLicenseRecognizer",
    "ItalyBICSwiftRecognizer",
    "PCI_DSS_CreditCardAndTrackDataRecognizer",
    "US_AZSB1338Recognizer",
    "CASB1386Recognizer",
    "COHB1119Recognizer",
    "ConnecticutDLPRecognizer",
    "ColumbiaDLPRecognizer",
    "FLHB481Recognizer",
    "IdahoSB1374Recognizer",
    "LouisianaRecognizer",
    "MassachusettsDataRecognizer",
    "MinnesotaRecognizer",
    "NevadaRecognizer",
    "NewJerseyDLPRecognizer",
    "NewHampshirePolicyRecognizer",
    "NewYorkDataRecognizer",
    "OhioDataRecognizer",
    "OklahomaRecognizer",
    "PennsylvaniaRecognizer",
    "TexasPolicyRecognizer",
    "UtahPolicyRecognizer",
    "WashingtonStateRecognizer",
    
]
