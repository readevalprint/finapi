# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.64.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from finapi.models.category import Category  # noqa: F401,E501
from finapi.models.label import Label  # noqa: F401,E501
from finapi.models.paypal_transaction_data import PaypalTransactionData  # noqa: F401,E501


class Transaction(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'parent_id': 'int',
        'account_id': 'int',
        'value_date': 'str',
        'bank_booking_date': 'str',
        'finapi_booking_date': 'str',
        'amount': 'float',
        'purpose': 'str',
        'counterpart_name': 'str',
        'counterpart_account_number': 'str',
        'counterpart_iban': 'str',
        'counterpart_blz': 'str',
        'counterpart_bic': 'str',
        'counterpart_bank_name': 'str',
        'counterpart_mandate_reference': 'str',
        'counterpart_customer_reference': 'str',
        'counterpart_creditor_id': 'str',
        'type': 'str',
        'type_code_zka': 'str',
        'type_code_swift': 'str',
        'sepa_purpose_code': 'str',
        'primanota': 'str',
        'category': 'Category',
        'labels': 'list[Label]',
        'is_potential_duplicate': 'bool',
        'is_adjusting_entry': 'bool',
        'is_new': 'bool',
        'import_date': 'str',
        'children': 'list[int]',
        'paypal_data': 'PaypalTransactionData',
        'end_to_end_reference': 'str'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parentId',
        'account_id': 'accountId',
        'value_date': 'valueDate',
        'bank_booking_date': 'bankBookingDate',
        'finapi_booking_date': 'finapiBookingDate',
        'amount': 'amount',
        'purpose': 'purpose',
        'counterpart_name': 'counterpartName',
        'counterpart_account_number': 'counterpartAccountNumber',
        'counterpart_iban': 'counterpartIban',
        'counterpart_blz': 'counterpartBlz',
        'counterpart_bic': 'counterpartBic',
        'counterpart_bank_name': 'counterpartBankName',
        'counterpart_mandate_reference': 'counterpartMandateReference',
        'counterpart_customer_reference': 'counterpartCustomerReference',
        'counterpart_creditor_id': 'counterpartCreditorId',
        'type': 'type',
        'type_code_zka': 'typeCodeZka',
        'type_code_swift': 'typeCodeSwift',
        'sepa_purpose_code': 'sepaPurposeCode',
        'primanota': 'primanota',
        'category': 'category',
        'labels': 'labels',
        'is_potential_duplicate': 'isPotentialDuplicate',
        'is_adjusting_entry': 'isAdjustingEntry',
        'is_new': 'isNew',
        'import_date': 'importDate',
        'children': 'children',
        'paypal_data': 'paypalData',
        'end_to_end_reference': 'endToEndReference'
    }

    def __init__(self, id=None, parent_id=None, account_id=None, value_date=None, bank_booking_date=None, finapi_booking_date=None, amount=None, purpose=None, counterpart_name=None, counterpart_account_number=None, counterpart_iban=None, counterpart_blz=None, counterpart_bic=None, counterpart_bank_name=None, counterpart_mandate_reference=None, counterpart_customer_reference=None, counterpart_creditor_id=None, type=None, type_code_zka=None, type_code_swift=None, sepa_purpose_code=None, primanota=None, category=None, labels=None, is_potential_duplicate=None, is_adjusting_entry=None, is_new=None, import_date=None, children=None, paypal_data=None, end_to_end_reference=None):  # noqa: E501
        """Transaction - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._parent_id = None
        self._account_id = None
        self._value_date = None
        self._bank_booking_date = None
        self._finapi_booking_date = None
        self._amount = None
        self._purpose = None
        self._counterpart_name = None
        self._counterpart_account_number = None
        self._counterpart_iban = None
        self._counterpart_blz = None
        self._counterpart_bic = None
        self._counterpart_bank_name = None
        self._counterpart_mandate_reference = None
        self._counterpart_customer_reference = None
        self._counterpart_creditor_id = None
        self._type = None
        self._type_code_zka = None
        self._type_code_swift = None
        self._sepa_purpose_code = None
        self._primanota = None
        self._category = None
        self._labels = None
        self._is_potential_duplicate = None
        self._is_adjusting_entry = None
        self._is_new = None
        self._import_date = None
        self._children = None
        self._paypal_data = None
        self._end_to_end_reference = None
        self.discriminator = None

        self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        self.account_id = account_id
        self.value_date = value_date
        self.bank_booking_date = bank_booking_date
        self.finapi_booking_date = finapi_booking_date
        self.amount = amount
        if purpose is not None:
            self.purpose = purpose
        if counterpart_name is not None:
            self.counterpart_name = counterpart_name
        if counterpart_account_number is not None:
            self.counterpart_account_number = counterpart_account_number
        if counterpart_iban is not None:
            self.counterpart_iban = counterpart_iban
        if counterpart_blz is not None:
            self.counterpart_blz = counterpart_blz
        if counterpart_bic is not None:
            self.counterpart_bic = counterpart_bic
        if counterpart_bank_name is not None:
            self.counterpart_bank_name = counterpart_bank_name
        if counterpart_mandate_reference is not None:
            self.counterpart_mandate_reference = counterpart_mandate_reference
        if counterpart_customer_reference is not None:
            self.counterpart_customer_reference = counterpart_customer_reference
        if counterpart_creditor_id is not None:
            self.counterpart_creditor_id = counterpart_creditor_id
        if type is not None:
            self.type = type
        if type_code_zka is not None:
            self.type_code_zka = type_code_zka
        if type_code_swift is not None:
            self.type_code_swift = type_code_swift
        if sepa_purpose_code is not None:
            self.sepa_purpose_code = sepa_purpose_code
        if primanota is not None:
            self.primanota = primanota
        if category is not None:
            self.category = category
        if labels is not None:
            self.labels = labels
        self.is_potential_duplicate = is_potential_duplicate
        self.is_adjusting_entry = is_adjusting_entry
        self.is_new = is_new
        self.import_date = import_date
        if children is not None:
            self.children = children
        if paypal_data is not None:
            self.paypal_data = paypal_data
        if end_to_end_reference is not None:
            self.end_to_end_reference = end_to_end_reference

    @property
    def id(self):
        """Gets the id of this Transaction.  # noqa: E501

        Transaction identifier  # noqa: E501

        :return: The id of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transaction.

        Transaction identifier  # noqa: E501

        :param id: The id of this Transaction.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this Transaction.  # noqa: E501

        Parent transaction identifier  # noqa: E501

        :return: The parent_id of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Transaction.

        Parent transaction identifier  # noqa: E501

        :param parent_id: The parent_id of this Transaction.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def account_id(self):
        """Gets the account_id of this Transaction.  # noqa: E501

        Account identifier  # noqa: E501

        :return: The account_id of this Transaction.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Transaction.

        Account identifier  # noqa: E501

        :param account_id: The account_id of this Transaction.  # noqa: E501
        :type: int
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def value_date(self):
        """Gets the value_date of this Transaction.  # noqa: E501

        Value date in the format 'YYYY-MM-DD HH:MM:SS.SSS' (german time).  # noqa: E501

        :return: The value_date of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._value_date

    @value_date.setter
    def value_date(self, value_date):
        """Sets the value_date of this Transaction.

        Value date in the format 'YYYY-MM-DD HH:MM:SS.SSS' (german time).  # noqa: E501

        :param value_date: The value_date of this Transaction.  # noqa: E501
        :type: str
        """
        if value_date is None:
            raise ValueError("Invalid value for `value_date`, must not be `None`")  # noqa: E501

        self._value_date = value_date

    @property
    def bank_booking_date(self):
        """Gets the bank_booking_date of this Transaction.  # noqa: E501

        Bank booking date in the format 'YYYY-MM-DD HH:MM:SS.SSS' (german time).  # noqa: E501

        :return: The bank_booking_date of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._bank_booking_date

    @bank_booking_date.setter
    def bank_booking_date(self, bank_booking_date):
        """Sets the bank_booking_date of this Transaction.

        Bank booking date in the format 'YYYY-MM-DD HH:MM:SS.SSS' (german time).  # noqa: E501

        :param bank_booking_date: The bank_booking_date of this Transaction.  # noqa: E501
        :type: str
        """
        if bank_booking_date is None:
            raise ValueError("Invalid value for `bank_booking_date`, must not be `None`")  # noqa: E501

        self._bank_booking_date = bank_booking_date

    @property
    def finapi_booking_date(self):
        """Gets the finapi_booking_date of this Transaction.  # noqa: E501

        finAPI Booking date in the format 'YYYY-MM-DD HH:MM:SS.SSS' (german time). NOTE: In some cases, banks may deliver transactions that are booked in future, but already included in the current account balance. To keep the account balance consistent with the set of transactions, such \"future transactions\" will be imported with their finapiBookingDate set to the current date (i.e.: date of import). The finapiBookingDate will automatically get adjusted towards the bankBookingDate each time the associated bank account is updated. Example: A transaction is imported on July, 3rd, with a bank reported booking date of July, 6th. The transaction will be imported with its finapiBookingDate set to July, 3rd. Then, on July 4th, the associated account is updated. During this update, the transaction's finapiBookingDate will be automatically adjusted to July 4th. This adjustment of the finapiBookingDate takes place on each update until the bank account is updated on July 6th or later, in which case the transaction's finapiBookingDate will be adjusted to its final value, July 6th.<br/> The finapiBookingDate is the date that is used by the finAPI PFM services. E.g. when you calculate the spendings of an account for the current month, and have a transaction with finapiBookingDate in the current month but bankBookingDate at the beginning of the next month, then this transaction is included in the calculations (as the bank has this transaction's amount included in the current account balance as well).  # noqa: E501

        :return: The finapi_booking_date of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._finapi_booking_date

    @finapi_booking_date.setter
    def finapi_booking_date(self, finapi_booking_date):
        """Sets the finapi_booking_date of this Transaction.

        finAPI Booking date in the format 'YYYY-MM-DD HH:MM:SS.SSS' (german time). NOTE: In some cases, banks may deliver transactions that are booked in future, but already included in the current account balance. To keep the account balance consistent with the set of transactions, such \"future transactions\" will be imported with their finapiBookingDate set to the current date (i.e.: date of import). The finapiBookingDate will automatically get adjusted towards the bankBookingDate each time the associated bank account is updated. Example: A transaction is imported on July, 3rd, with a bank reported booking date of July, 6th. The transaction will be imported with its finapiBookingDate set to July, 3rd. Then, on July 4th, the associated account is updated. During this update, the transaction's finapiBookingDate will be automatically adjusted to July 4th. This adjustment of the finapiBookingDate takes place on each update until the bank account is updated on July 6th or later, in which case the transaction's finapiBookingDate will be adjusted to its final value, July 6th.<br/> The finapiBookingDate is the date that is used by the finAPI PFM services. E.g. when you calculate the spendings of an account for the current month, and have a transaction with finapiBookingDate in the current month but bankBookingDate at the beginning of the next month, then this transaction is included in the calculations (as the bank has this transaction's amount included in the current account balance as well).  # noqa: E501

        :param finapi_booking_date: The finapi_booking_date of this Transaction.  # noqa: E501
        :type: str
        """
        if finapi_booking_date is None:
            raise ValueError("Invalid value for `finapi_booking_date`, must not be `None`")  # noqa: E501

        self._finapi_booking_date = finapi_booking_date

    @property
    def amount(self):
        """Gets the amount of this Transaction.  # noqa: E501

        Transaction amount  # noqa: E501

        :return: The amount of this Transaction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Transaction.

        Transaction amount  # noqa: E501

        :param amount: The amount of this Transaction.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def purpose(self):
        """Gets the purpose of this Transaction.  # noqa: E501

        Transaction purpose. Maximum length: 2000  # noqa: E501

        :return: The purpose of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this Transaction.

        Transaction purpose. Maximum length: 2000  # noqa: E501

        :param purpose: The purpose of this Transaction.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def counterpart_name(self):
        """Gets the counterpart_name of this Transaction.  # noqa: E501

        Counterpart name. Maximum length: 80  # noqa: E501

        :return: The counterpart_name of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_name

    @counterpart_name.setter
    def counterpart_name(self, counterpart_name):
        """Sets the counterpart_name of this Transaction.

        Counterpart name. Maximum length: 80  # noqa: E501

        :param counterpart_name: The counterpart_name of this Transaction.  # noqa: E501
        :type: str
        """

        self._counterpart_name = counterpart_name

    @property
    def counterpart_account_number(self):
        """Gets the counterpart_account_number of this Transaction.  # noqa: E501

        Counterpart account number  # noqa: E501

        :return: The counterpart_account_number of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_account_number

    @counterpart_account_number.setter
    def counterpart_account_number(self, counterpart_account_number):
        """Sets the counterpart_account_number of this Transaction.

        Counterpart account number  # noqa: E501

        :param counterpart_account_number: The counterpart_account_number of this Transaction.  # noqa: E501
        :type: str
        """

        self._counterpart_account_number = counterpart_account_number

    @property
    def counterpart_iban(self):
        """Gets the counterpart_iban of this Transaction.  # noqa: E501

        Counterpart IBAN  # noqa: E501

        :return: The counterpart_iban of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_iban

    @counterpart_iban.setter
    def counterpart_iban(self, counterpart_iban):
        """Sets the counterpart_iban of this Transaction.

        Counterpart IBAN  # noqa: E501

        :param counterpart_iban: The counterpart_iban of this Transaction.  # noqa: E501
        :type: str
        """

        self._counterpart_iban = counterpart_iban

    @property
    def counterpart_blz(self):
        """Gets the counterpart_blz of this Transaction.  # noqa: E501

        Counterpart BLZ  # noqa: E501

        :return: The counterpart_blz of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_blz

    @counterpart_blz.setter
    def counterpart_blz(self, counterpart_blz):
        """Sets the counterpart_blz of this Transaction.

        Counterpart BLZ  # noqa: E501

        :param counterpart_blz: The counterpart_blz of this Transaction.  # noqa: E501
        :type: str
        """

        self._counterpart_blz = counterpart_blz

    @property
    def counterpart_bic(self):
        """Gets the counterpart_bic of this Transaction.  # noqa: E501

        Counterpart BIC  # noqa: E501

        :return: The counterpart_bic of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_bic

    @counterpart_bic.setter
    def counterpart_bic(self, counterpart_bic):
        """Sets the counterpart_bic of this Transaction.

        Counterpart BIC  # noqa: E501

        :param counterpart_bic: The counterpart_bic of this Transaction.  # noqa: E501
        :type: str
        """

        self._counterpart_bic = counterpart_bic

    @property
    def counterpart_bank_name(self):
        """Gets the counterpart_bank_name of this Transaction.  # noqa: E501

        Counterpart Bank name  # noqa: E501

        :return: The counterpart_bank_name of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_bank_name

    @counterpart_bank_name.setter
    def counterpart_bank_name(self, counterpart_bank_name):
        """Sets the counterpart_bank_name of this Transaction.

        Counterpart Bank name  # noqa: E501

        :param counterpart_bank_name: The counterpart_bank_name of this Transaction.  # noqa: E501
        :type: str
        """

        self._counterpart_bank_name = counterpart_bank_name

    @property
    def counterpart_mandate_reference(self):
        """Gets the counterpart_mandate_reference of this Transaction.  # noqa: E501

        The mandate reference of the counterpart  # noqa: E501

        :return: The counterpart_mandate_reference of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_mandate_reference

    @counterpart_mandate_reference.setter
    def counterpart_mandate_reference(self, counterpart_mandate_reference):
        """Sets the counterpart_mandate_reference of this Transaction.

        The mandate reference of the counterpart  # noqa: E501

        :param counterpart_mandate_reference: The counterpart_mandate_reference of this Transaction.  # noqa: E501
        :type: str
        """

        self._counterpart_mandate_reference = counterpart_mandate_reference

    @property
    def counterpart_customer_reference(self):
        """Gets the counterpart_customer_reference of this Transaction.  # noqa: E501

        The customer reference of the counterpart  # noqa: E501

        :return: The counterpart_customer_reference of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_customer_reference

    @counterpart_customer_reference.setter
    def counterpart_customer_reference(self, counterpart_customer_reference):
        """Sets the counterpart_customer_reference of this Transaction.

        The customer reference of the counterpart  # noqa: E501

        :param counterpart_customer_reference: The counterpart_customer_reference of this Transaction.  # noqa: E501
        :type: str
        """

        self._counterpart_customer_reference = counterpart_customer_reference

    @property
    def counterpart_creditor_id(self):
        """Gets the counterpart_creditor_id of this Transaction.  # noqa: E501

        The creditor ID of the counterpart  # noqa: E501

        :return: The counterpart_creditor_id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_creditor_id

    @counterpart_creditor_id.setter
    def counterpart_creditor_id(self, counterpart_creditor_id):
        """Sets the counterpart_creditor_id of this Transaction.

        The creditor ID of the counterpart  # noqa: E501

        :param counterpart_creditor_id: The counterpart_creditor_id of this Transaction.  # noqa: E501
        :type: str
        """

        self._counterpart_creditor_id = counterpart_creditor_id

    @property
    def type(self):
        """Gets the type of this Transaction.  # noqa: E501

        Transaction type, according to the bank. If set, this will contain a German term that you can display to the user. Some examples of common values are: \"Lastschrift\", \"Auslands&uuml;berweisung\", \"Geb&uuml;hren\", \"Zinsen\". The maximum possible length of this field is 255 characters.  # noqa: E501

        :return: The type of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Transaction.

        Transaction type, according to the bank. If set, this will contain a German term that you can display to the user. Some examples of common values are: \"Lastschrift\", \"Auslands&uuml;berweisung\", \"Geb&uuml;hren\", \"Zinsen\". The maximum possible length of this field is 255 characters.  # noqa: E501

        :param type: The type of this Transaction.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def type_code_zka(self):
        """Gets the type_code_zka of this Transaction.  # noqa: E501

        ZKA business transaction code which relates to the transaction's type. Possible values range from 1 through 999. If no information about the ZKA type code is available, then this field will be null.  # noqa: E501

        :return: The type_code_zka of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._type_code_zka

    @type_code_zka.setter
    def type_code_zka(self, type_code_zka):
        """Sets the type_code_zka of this Transaction.

        ZKA business transaction code which relates to the transaction's type. Possible values range from 1 through 999. If no information about the ZKA type code is available, then this field will be null.  # noqa: E501

        :param type_code_zka: The type_code_zka of this Transaction.  # noqa: E501
        :type: str
        """

        self._type_code_zka = type_code_zka

    @property
    def type_code_swift(self):
        """Gets the type_code_swift of this Transaction.  # noqa: E501

        SWIFT transaction type code. If no information about the SWIFT code is available, then this field will be null.  # noqa: E501

        :return: The type_code_swift of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._type_code_swift

    @type_code_swift.setter
    def type_code_swift(self, type_code_swift):
        """Sets the type_code_swift of this Transaction.

        SWIFT transaction type code. If no information about the SWIFT code is available, then this field will be null.  # noqa: E501

        :param type_code_swift: The type_code_swift of this Transaction.  # noqa: E501
        :type: str
        """

        self._type_code_swift = type_code_swift

    @property
    def sepa_purpose_code(self):
        """Gets the sepa_purpose_code of this Transaction.  # noqa: E501

        SEPA purpose code, according to ISO 20022  # noqa: E501

        :return: The sepa_purpose_code of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._sepa_purpose_code

    @sepa_purpose_code.setter
    def sepa_purpose_code(self, sepa_purpose_code):
        """Sets the sepa_purpose_code of this Transaction.

        SEPA purpose code, according to ISO 20022  # noqa: E501

        :param sepa_purpose_code: The sepa_purpose_code of this Transaction.  # noqa: E501
        :type: str
        """

        self._sepa_purpose_code = sepa_purpose_code

    @property
    def primanota(self):
        """Gets the primanota of this Transaction.  # noqa: E501

        Transaction primanota (bank side identification number)  # noqa: E501

        :return: The primanota of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._primanota

    @primanota.setter
    def primanota(self, primanota):
        """Sets the primanota of this Transaction.

        Transaction primanota (bank side identification number)  # noqa: E501

        :param primanota: The primanota of this Transaction.  # noqa: E501
        :type: str
        """

        self._primanota = primanota

    @property
    def category(self):
        """Gets the category of this Transaction.  # noqa: E501

        Transaction category, if any is assigned. Note: Recently imported transactions that have currently no category assigned might still get categorized by the background categorization process. To check the status of the background categorization, see GET /bankConnections. Manual category assignments to a transaction will remove the transaction from the background categorization process (i.e. the background categorization process will never overwrite a manual category assignment).  # noqa: E501

        :return: The category of this Transaction.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Transaction.

        Transaction category, if any is assigned. Note: Recently imported transactions that have currently no category assigned might still get categorized by the background categorization process. To check the status of the background categorization, see GET /bankConnections. Manual category assignments to a transaction will remove the transaction from the background categorization process (i.e. the background categorization process will never overwrite a manual category assignment).  # noqa: E501

        :param category: The category of this Transaction.  # noqa: E501
        :type: Category
        """

        self._category = category

    @property
    def labels(self):
        """Gets the labels of this Transaction.  # noqa: E501

        Array of assigned labels  # noqa: E501

        :return: The labels of this Transaction.  # noqa: E501
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Transaction.

        Array of assigned labels  # noqa: E501

        :param labels: The labels of this Transaction.  # noqa: E501
        :type: list[Label]
        """

        self._labels = labels

    @property
    def is_potential_duplicate(self):
        """Gets the is_potential_duplicate of this Transaction.  # noqa: E501

        While finAPI uses a well-elaborated algorithm for uniquely identifying transactions, there is still the possibility that during an account update, a transaction that was imported previously may be imported a second time as a new transaction. For example, this can happen if some transaction data changes on the bank server side. However, finAPI also includes an algorithm of identifying such \"potential duplicate\" transactions. If this field is set to true, it means that finAPI detected a similar transaction that might actually be the same. It is recommended to communicate this information to the end user, and give him an option to delete the transaction in case he confirms that it really is a duplicate.  # noqa: E501

        :return: The is_potential_duplicate of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_potential_duplicate

    @is_potential_duplicate.setter
    def is_potential_duplicate(self, is_potential_duplicate):
        """Sets the is_potential_duplicate of this Transaction.

        While finAPI uses a well-elaborated algorithm for uniquely identifying transactions, there is still the possibility that during an account update, a transaction that was imported previously may be imported a second time as a new transaction. For example, this can happen if some transaction data changes on the bank server side. However, finAPI also includes an algorithm of identifying such \"potential duplicate\" transactions. If this field is set to true, it means that finAPI detected a similar transaction that might actually be the same. It is recommended to communicate this information to the end user, and give him an option to delete the transaction in case he confirms that it really is a duplicate.  # noqa: E501

        :param is_potential_duplicate: The is_potential_duplicate of this Transaction.  # noqa: E501
        :type: bool
        """
        if is_potential_duplicate is None:
            raise ValueError("Invalid value for `is_potential_duplicate`, must not be `None`")  # noqa: E501

        self._is_potential_duplicate = is_potential_duplicate

    @property
    def is_adjusting_entry(self):
        """Gets the is_adjusting_entry of this Transaction.  # noqa: E501

        Indicating whether this transaction is an adjusting entry ('Zwischensaldo').<br/><br/>Adjusting entries do not originate from the bank, but are added by finAPI during an account update when the bank reported account balance does not add up to the set of transactions that finAPI receives for the account. In this case, the adjusting entry will fix the deviation between the balance and the received transactions so that both adds up again.<br/><br/>Possible causes for such deviations are:<br/>- Inconsistencies in how the bank calculates the balance, for instance when not yet booked transactions are already included in the balance, but not included in the set of transactions<br/>- Gaps in the transaction history that finAPI receives, for instance because the account has not been updated for a while and older transactions are no longer available  # noqa: E501

        :return: The is_adjusting_entry of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_adjusting_entry

    @is_adjusting_entry.setter
    def is_adjusting_entry(self, is_adjusting_entry):
        """Sets the is_adjusting_entry of this Transaction.

        Indicating whether this transaction is an adjusting entry ('Zwischensaldo').<br/><br/>Adjusting entries do not originate from the bank, but are added by finAPI during an account update when the bank reported account balance does not add up to the set of transactions that finAPI receives for the account. In this case, the adjusting entry will fix the deviation between the balance and the received transactions so that both adds up again.<br/><br/>Possible causes for such deviations are:<br/>- Inconsistencies in how the bank calculates the balance, for instance when not yet booked transactions are already included in the balance, but not included in the set of transactions<br/>- Gaps in the transaction history that finAPI receives, for instance because the account has not been updated for a while and older transactions are no longer available  # noqa: E501

        :param is_adjusting_entry: The is_adjusting_entry of this Transaction.  # noqa: E501
        :type: bool
        """
        if is_adjusting_entry is None:
            raise ValueError("Invalid value for `is_adjusting_entry`, must not be `None`")  # noqa: E501

        self._is_adjusting_entry = is_adjusting_entry

    @property
    def is_new(self):
        """Gets the is_new of this Transaction.  # noqa: E501

        Indicating whether this transaction is 'new' or not. Any newly imported transaction will have this flag initially set to true. How you use this field is up to your interpretation. For example, you might want to set it to false once a user has clicked on/seen the transaction. You can change this flag to 'false' with the PATCH method.  # noqa: E501

        :return: The is_new of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_new

    @is_new.setter
    def is_new(self, is_new):
        """Sets the is_new of this Transaction.

        Indicating whether this transaction is 'new' or not. Any newly imported transaction will have this flag initially set to true. How you use this field is up to your interpretation. For example, you might want to set it to false once a user has clicked on/seen the transaction. You can change this flag to 'false' with the PATCH method.  # noqa: E501

        :param is_new: The is_new of this Transaction.  # noqa: E501
        :type: bool
        """
        if is_new is None:
            raise ValueError("Invalid value for `is_new`, must not be `None`")  # noqa: E501

        self._is_new = is_new

    @property
    def import_date(self):
        """Gets the import_date of this Transaction.  # noqa: E501

        Date of transaction import, in the format 'YYYY-MM-DD HH:MM:SS.SSS' (german time).  # noqa: E501

        :return: The import_date of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._import_date

    @import_date.setter
    def import_date(self, import_date):
        """Sets the import_date of this Transaction.

        Date of transaction import, in the format 'YYYY-MM-DD HH:MM:SS.SSS' (german time).  # noqa: E501

        :param import_date: The import_date of this Transaction.  # noqa: E501
        :type: str
        """
        if import_date is None:
            raise ValueError("Invalid value for `import_date`, must not be `None`")  # noqa: E501

        self._import_date = import_date

    @property
    def children(self):
        """Gets the children of this Transaction.  # noqa: E501

        Sub-transactions identifiers (if this transaction is split)  # noqa: E501

        :return: The children of this Transaction.  # noqa: E501
        :rtype: list[int]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this Transaction.

        Sub-transactions identifiers (if this transaction is split)  # noqa: E501

        :param children: The children of this Transaction.  # noqa: E501
        :type: list[int]
        """

        self._children = children

    @property
    def paypal_data(self):
        """Gets the paypal_data of this Transaction.  # noqa: E501

        Additional, PayPal-specific transaction data. This field is only set for transactions that belong to an account of the 'PayPal' bank (BLZ 'PAYPAL').  # noqa: E501

        :return: The paypal_data of this Transaction.  # noqa: E501
        :rtype: PaypalTransactionData
        """
        return self._paypal_data

    @paypal_data.setter
    def paypal_data(self, paypal_data):
        """Sets the paypal_data of this Transaction.

        Additional, PayPal-specific transaction data. This field is only set for transactions that belong to an account of the 'PayPal' bank (BLZ 'PAYPAL').  # noqa: E501

        :param paypal_data: The paypal_data of this Transaction.  # noqa: E501
        :type: PaypalTransactionData
        """

        self._paypal_data = paypal_data

    @property
    def end_to_end_reference(self):
        """Gets the end_to_end_reference of this Transaction.  # noqa: E501

        End-To-End reference  # noqa: E501

        :return: The end_to_end_reference of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._end_to_end_reference

    @end_to_end_reference.setter
    def end_to_end_reference(self, end_to_end_reference):
        """Sets the end_to_end_reference of this Transaction.

        End-To-End reference  # noqa: E501

        :param end_to_end_reference: The end_to_end_reference of this Transaction.  # noqa: E501
        :type: str
        """

        self._end_to_end_reference = end_to_end_reference

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Transaction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Transaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
