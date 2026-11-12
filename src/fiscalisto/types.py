# Generado por `bun run openapi` desde la especificación OpenAPI de la API: no lo edite.
"""Los tipos de la API: cada objeto y cada cuerpo, como diccionarios (TypedDict)."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, Literal, TypedDict, Union

# Only type checkers read NotRequired before 3.11: the annotations are never evaluated.
if sys.version_info >= (3, 11):
    from typing import NotRequired
elif TYPE_CHECKING:  # pragma: no cover
    from typing_extensions import NotRequired

__all__ = [
    "Account",
    "AccountKey",
    "Advance",
    "AdvanceCustomer",
    "AdvanceList",
    "AdvanceTestClockParams",
    "ApiError",
    "ApiErrorError",
    "ApplyAdvanceParams",
    "ApplyAdvanceParamsRemainder",
    "ApproveExpenseReportParams",
    "Balance",
    "BalanceAutoRecharge",
    "BalanceLowEvent",
    "BalancePacksItem",
    "BankImport",
    "BankTransaction",
    "BankTransactionList",
    "BankTransactionSuggestedMatch",
    "Branch",
    "BranchAddress",
    "BranchList",
    "BranchSeries",
    "CancelInvoiceParams",
    "CancelRetentionParams",
    "CancelSalesOrderDeliveryParams",
    "CancelSalesOrderParams",
    "CheckSatListsParams",
    "ClassifyBankTransactionParams",
    "CloseSalesOrderParams",
    "ComplianceOpinion",
    "CostCenter",
    "CostCenterList",
    "CreateAdvanceParams",
    "CreateAdvanceParamsCustomer",
    "CreateAdvanceParamsCustomerForeign",
    "CreateBankTransactionsParams",
    "CreateBankTransactionsParamsTransactionsItem",
    "CreateBranchParams",
    "CreateBranchParamsAddress",
    "CreateBranchParamsSeries",
    "CreateCostCenterParams",
    "CreateCreditNoteParams",
    "CreateCustomerDataRequestParams",
    "CreateCustomerGroupParams",
    "CreateCustomerParams",
    "CreateCustomerParamsForeign",
    "CreateEmployeeParams",
    "CreateExpenseItemParams",
    "CreateExpenseMovementParams",
    "CreateExpensePersonLinkParams",
    "CreateExpensePersonParams",
    "CreateExpenseReportParams",
    "CreateImssFilesParams",
    "CreateImssMovementParams",
    "CreateInvoiceBatchParams",
    "CreateInvoiceBatchParamsInvoicesItem",
    "CreateIssuerOnboardingLinkParams",
    "CreateIssuerParams",
    "CreateIssuerParamsDonationAuthorization",
    "CreatePaymentParams",
    "CreatePaymentParamsDocumentsItem",
    "CreatePayrollBankFileParams",
    "CreatePayrollBatchParams",
    "CreatePayrollBatchParamsExternalReceiptsItem",
    "CreatePayrollBatchParamsPeriod",
    "CreatePayrollBatchParamsReceiptsItem",
    "CreatePayrollBatchParamsReceiptsItemPeriod",
    "CreatePayrollReceiptParams",
    "CreatePayrollReceiptParamsPeriod",
    "CreatePriceListParams",
    "CreatePriceListParamsItemsItem",
    "CreateProductParams",
    "CreateProductParamsLocalTaxesItem",
    "CreatePurchaseReceiptParams",
    "CreatePurchaseReceiptParamsFieldsItem",
    "CreateQuoteParams",
    "CreateQuoteParamsCustomer1",
    "CreateQuoteParamsCustomer1Foreign",
    "CreateQuoteParamsCustomer2",
    "CreateQuoteParamsItemsItem",
    "CreateQuoteParamsItemsItemIedu",
    "CreateQuoteParamsItemsItemThirdParty",
    "CreateQuoteParamsItemsItemUsedVehicle",
    "CreateQuoteParamsItemsItemUsedVehicleCustomsItem",
    "CreateRecurringInvoiceParams",
    "CreateRecurringInvoiceParamsInvoice",
    "CreateRecurringInvoiceParamsSchedule",
    "CreateRetentionParams",
    "CreateRetentionParamsDividends",
    "CreateRetentionParamsFinancialDerivatives",
    "CreateRetentionParamsForeignPayment",
    "CreateRetentionParamsInterest",
    "CreateRetentionParamsMortgageInterest",
    "CreateRetentionParamsPeriod",
    "CreateRetentionParamsPlatform",
    "CreateRetentionParamsPlatformServicesItem",
    "CreateRetentionParamsPlatformServicesItemCommission",
    "CreateRetentionParamsPlatformServicesItemContribution",
    "CreateRetentionParamsPrize",
    "CreateRetentionParamsRecipient",
    "CreateRetentionParamsRetirementPlan",
    "CreateRetentionParamsRetirementPlanContributionsItem",
    "CreateRetentionParamsShareSale",
    "CreateRetentionParamsTaxesItem",
    "CreateRetentionParamsTotals",
    "CreateRetentionParamsTrust",
    "CreateRetentionParamsTrustDeductions",
    "CreateRetentionParamsTrustIncome",
    "CreateRetentionParamsTrustLease",
    "CreateRetentionParamsTrustWithholding",
    "CreateSalesOrderDeliveryParams",
    "CreateSalesOrderDeliveryParamsItemsItem",
    "CreateSalesOrderParams",
    "CreateSalesOrderParamsCustomer",
    "CreateSalesOrderParamsCustomerForeign",
    "CreateSalesOrderParamsItemsItem",
    "CreateSalesOrderParamsItemsItemIedu",
    "CreateSalesOrderParamsItemsItemThirdParty",
    "CreateSalesOrderParamsItemsItemUsedVehicle",
    "CreateSalesOrderParamsItemsItemUsedVehicleCustomsItem",
    "CreateSandboxParams",
    "CreateSatDownloadParams",
    "CreateStockAdjustmentParams",
    "CreateStockAdjustmentParamsLinesItem",
    "CreateStoreConnectionParams",
    "CreateStoreConnectionParamsSettings",
    "CreateTestClockParams",
    "CreateTicketParams",
    "CreateTicketParamsBuyer",
    "CreateTicketParamsLinesItem",
    "CreateWebhookEndpointParams",
    "CrossCheckCfdi",
    "CrossCheckCfdiCfdiItem",
    "CrossChecks",
    "CrossChecksMonthsItem",
    "CrossChecksMonthsItemChecksItem",
    "CrossChecksTaxRegimes",
    "CrossChecksTaxRegimesInvoicedItem",
    "CrossChecksVatBalanceInFavor",
    "CrossChecksVatBalanceInFavorPeriodsItem",
    "Customer",
    "CustomerDataRequest",
    "CustomerDataRequestCompletedEvent",
    "CustomerDataRequestList",
    "CustomerDataRequestSubmission",
    "CustomerForeign",
    "CustomerGroup",
    "CustomerGroupList",
    "CustomerList",
    "CustomerPaymentBehavior",
    "CustomerPaymentBehaviorLastPayment",
    "CustomerPaymentBehaviorMonthsItem",
    "CustomerPaymentBehaviorOpenInvoicesItem",
    "CustomerPaymentBehaviorPaymentFormsItem",
    "CustomerPaymentBehaviorTrend",
    "DeleteCostCenterParams",
    "Deleted",
    "Diot",
    "DiotLinesItem",
    "DiotLinesItemPaid",
    "DiotLinesItemReturns",
    "Employee",
    "EmployeeList",
    "Event",
    "EventList",
    "EventType",
    "ExpenseItem",
    "ExpenseItemIssuesItem",
    "ExpenseMovement",
    "ExpensePerson",
    "ExpensePersonLink",
    "ExpensePersonList",
    "ExpensePolicy",
    "ExpensePolicyLimitsValue",
    "ExpenseReport",
    "ExpenseReportIssuesItem",
    "ExpenseReportList",
    "ExpenseReportPayroll",
    "ExternalPayrollReceiptCreate",
    "ExternalPayrollReceiptCreateDeductionsItem",
    "ExternalPayrollReceiptCreateDisabilitiesItem",
    "ExternalPayrollReceiptCreateEmployee",
    "ExternalPayrollReceiptCreateEmployeeSubcontractingItem",
    "ExternalPayrollReceiptCreateEmployer",
    "ExternalPayrollReceiptCreateEmployerSncf",
    "ExternalPayrollReceiptCreateOtherPaymentsItem",
    "ExternalPayrollReceiptCreateOtherPaymentsItemBalanceCompensation",
    "ExternalPayrollReceiptCreatePerceptionsItem",
    "ExternalPayrollReceiptCreatePerceptionsItemOvertimeItem",
    "ExternalPayrollReceiptCreatePerceptionsItemStockOptions",
    "ExternalPayrollReceiptCreatePeriod",
    "ExternalPayrollReceiptCreateReferences",
    "ExternalPayrollReceiptCreateRetirement",
    "ExternalPayrollReceiptCreateSeparation",
    "ExternalPayrollReceiptCreateTotals",
    "ExternalPayrollReceiptPreview",
    "ExternalPayrollReceiptPreviewCustomer",
    "ExternalPayrollReceiptPreviewWarningsItem",
    "FinancialStatements",
    "FinancialStatementsBalanceSheet",
    "FinancialStatementsBalanceSheetAssets",
    "FinancialStatementsBalanceSheetAssetsGroupsItem",
    "FinancialStatementsBalanceSheetAssetsGroupsItemAccountsItem",
    "FinancialStatementsBalanceSheetEquity",
    "FinancialStatementsBalanceSheetEquityGroupsItem",
    "FinancialStatementsBalanceSheetEquityGroupsItemAccountsItem",
    "FinancialStatementsBalanceSheetLiabilities",
    "FinancialStatementsBalanceSheetLiabilitiesGroupsItem",
    "FinancialStatementsBalanceSheetLiabilitiesGroupsItemAccountsItem",
    "FinancialStatementsIncomeStatement",
    "FinancialStatementsIncomeStatementMonth",
    "FinancialStatementsIncomeStatementMonthSectionsItem",
    "FinancialStatementsIncomeStatementMonthSectionsItemGroupsItem",
    "FinancialStatementsIncomeStatementMonthSectionsItemGroupsItemAccountsItem",
    "FinancialStatementsIncomeStatementYearToDate",
    "FinancialStatementsIncomeStatementYearToDateSectionsItem",
    "FinancialStatementsIncomeStatementYearToDateSectionsItemGroupsItem",
    "FinancialStatementsIncomeStatementYearToDateSectionsItemGroupsItemAccountsItem",
    "GetCrossCheckCfdiParams",
    "GetCrossChecksParams",
    "GetDiotFileParams",
    "GetDiotParams",
    "GetElectronicAccountingParams",
    "GetExpensePolicyParams",
    "GetFinancialStatementsParams",
    "GetInvoiceParams",
    "GetInvoicePdfParams",
    "GetInvoiceXmlParams",
    "GetRetentionParams",
    "GetRetentionPdfParams",
    "GetRetentionXmlParams",
    "GetSatCatalogParams",
    "GetSatDeclarationCalendarParams",
    "GetTrialBalanceParams",
    "GetVatRefundParams",
    "ImportStoreOrdersParams",
    "ImssFiles",
    "ImssFilesFilesItem",
    "ImssFilesRefusedItem",
    "ImssMovement",
    "ImssMovementList",
    "Invoice",
    "InvoiceAdvanceApplication",
    "InvoiceBatch",
    "InvoiceBatchCompletedEvent",
    "InvoiceBatchInvoicesItem",
    "InvoiceBatchList",
    "InvoiceCanceledEvent",
    "InvoiceCancellation",
    "InvoiceCancellationPendingEvent",
    "InvoiceCancellationRejectedEvent",
    "InvoiceCreate",
    "InvoiceCreateAddenda",
    "InvoiceCreateCartaPorte",
    "InvoiceCreateCartaPorteAir",
    "InvoiceCreateCartaPorteAirShipper",
    "InvoiceCreateCartaPorteAirShipperForeign",
    "InvoiceCreateCartaPorteDestinationsItem",
    "InvoiceCreateCartaPorteDestinationsItemAddress",
    "InvoiceCreateCartaPorteDestinationsItemForeign",
    "InvoiceCreateCartaPorteDestinationsItemStation",
    "InvoiceCreateCartaPorteDriversItem",
    "InvoiceCreateCartaPorteDriversItemForeign",
    "InvoiceCreateCartaPorteFiguresItem",
    "InvoiceCreateCartaPorteFiguresItemAddress",
    "InvoiceCreateCartaPorteFiguresItemForeign",
    "InvoiceCreateCartaPorteGoodsItem",
    "InvoiceCreateCartaPorteGoodsItemCofepris",
    "InvoiceCreateCartaPorteGoodsItemCustomsDocsItem",
    "InvoiceCreateCartaPorteGoodsItemDetail",
    "InvoiceCreateCartaPorteGoodsItemGuidesItem",
    "InvoiceCreateCartaPorteGoodsItemHazmat",
    "InvoiceCreateCartaPorteGoodsItemMaterial",
    "InvoiceCreateCartaPorteGoodsItemQuantitiesItem",
    "InvoiceCreateCartaPorteInternational",
    "InvoiceCreateCartaPorteIstmo",
    "InvoiceCreateCartaPorteOrigin",
    "InvoiceCreateCartaPorteOriginAddress",
    "InvoiceCreateCartaPorteOriginForeign",
    "InvoiceCreateCartaPorteOriginStation",
    "InvoiceCreateCartaPorteRail",
    "InvoiceCreateCartaPorteRailCarsItem",
    "InvoiceCreateCartaPorteRailCarsItemContainersItem",
    "InvoiceCreateCartaPorteRailRightsItem",
    "InvoiceCreateCartaPorteSea",
    "InvoiceCreateCartaPorteSeaContainersItem",
    "InvoiceCreateCartaPorteSeaContainersItemTrailersItem",
    "InvoiceCreateCartaPorteVehicle",
    "InvoiceCreateCartaPorteVehicleTrailersItem",
    "InvoiceCreateComercioExterior",
    "InvoiceCreateComercioExteriorGoodsItem",
    "InvoiceCreateComercioExteriorIssuerAddress",
    "InvoiceCreateComercioExteriorOwnersItem",
    "InvoiceCreateComercioExteriorReceiverAddress",
    "InvoiceCreateComercioExteriorRecipient",
    "InvoiceCreateComercioExteriorRecipientAddress",
    "InvoiceCreateCustomer",
    "InvoiceCreateCustomerForeign",
    "InvoiceCreateDonation",
    "InvoiceCreateGlobal",
    "InvoiceCreateIne",
    "InvoiceCreateIneEntitiesItem",
    "InvoiceCreateItemsItem",
    "InvoiceCreateItemsItemIedu",
    "InvoiceCreateItemsItemThirdParty",
    "InvoiceCreateItemsItemUsedVehicle",
    "InvoiceCreateItemsItemUsedVehicleCustomsItem",
    "InvoiceCreateLeyendasItem",
    "InvoiceCreateLocalTaxesItem",
    "InvoiceCreateRelated",
    "InvoiceCustomer",
    "InvoiceEmail",
    "InvoiceEmailBouncedEvent",
    "InvoiceEmailComplainedEvent",
    "InvoiceEmailRecipientsItem",
    "InvoiceError",
    "InvoiceFailedEvent",
    "InvoiceItem",
    "InvoiceList",
    "InvoicePaidEvent",
    "InvoicePartiallyPaidEvent",
    "InvoicePayment",
    "InvoicePaymentDocumentsItem",
    "InvoicePayroll",
    "InvoicePayrollDeductionsItem",
    "InvoicePayrollDisabilitiesItem",
    "InvoicePayrollEmployee",
    "InvoicePayrollEmployeeSubcontractingItem",
    "InvoicePayrollEmployer",
    "InvoicePayrollEmployerSncf",
    "InvoicePayrollOtherPaymentsItem",
    "InvoicePayrollOtherPaymentsItemBalanceCompensation",
    "InvoicePayrollPerceptionsItem",
    "InvoicePayrollPerceptionsItemOvertimeItem",
    "InvoicePayrollPerceptionsItemStockOptions",
    "InvoicePayrollPeriod",
    "InvoicePayrollReferences",
    "InvoicePayrollRetirement",
    "InvoicePayrollSeparation",
    "InvoicePayrollTotals",
    "InvoiceSalesOrderParams",
    "InvoiceSalesOrderParamsItemsItem",
    "InvoiceStampedEvent",
    "InvoiceSubstitutes",
    "InvoiceTaxes",
    "Issuer",
    "IssuerCertificate",
    "IssuerDonationAuthorization",
    "IssuerList",
    "IssuerOnboardingLink",
    "IssuerReadyEvent",
    "IssuerSatDownloads",
    "IssuerTestClock",
    "JournalEntry",
    "JournalEntryLinesItem",
    "JournalEntryList",
    "LedgerAccount",
    "LedgerAccountList",
    "ListAdvancesParams",
    "ListBankTransactionsParams",
    "ListBranchesParams",
    "ListCostCentersParams",
    "ListCustomerDataRequestsParams",
    "ListCustomerGroupsParams",
    "ListCustomersParams",
    "ListEmployeesParams",
    "ListEventsParams",
    "ListExpensePeopleParams",
    "ListExpenseReportsParams",
    "ListImssMovementsParams",
    "ListInvoiceBatchesParams",
    "ListInvoicesParams",
    "ListIssuersParams",
    "ListJournalEntriesParams",
    "ListLedgerAccountsParams",
    "ListPayrollBatchesParams",
    "ListPortalSuppliersParams",
    "ListPriceListsParams",
    "ListProductsParams",
    "ListPurchaseReceiptsParams",
    "ListQuotesParams",
    "ListReceivablesParams",
    "ListRecurringInvoicesParams",
    "ListRetentionsParams",
    "ListSalesOrdersParams",
    "ListSatDeclarationsParams",
    "ListSatDownloadsParams",
    "ListSatFindingCounterpartiesParams",
    "ListSatFindingsParams",
    "ListSatInvoicesParams",
    "ListSatMailboxMessagesParams",
    "ListSatRetentionsParams",
    "ListStockAdjustmentsParams",
    "ListStockMovementsParams",
    "ListStoreConnectionsParams",
    "ListSupplierInvoicesParams",
    "ListTicketsParams",
    "ListWarehouseStockParams",
    "ListWarehousesParams",
    "ListWebhookEndpointsParams",
    "MarkInvoicePaidParams",
    "MarkPurchaseReceiptInvoicedParams",
    "MarkSupplierInvoicePaidParams",
    "MatchBankTransactionParams",
    "PayrollBankFile",
    "PayrollBankFileExcludedItem",
    "PayrollBankFilePaymentsItem",
    "PayrollBatch",
    "PayrollBatchCompletedEvent",
    "PayrollBatchList",
    "PayrollBatchReceiptsItem",
    "PayrollBatchReceiptsItemError",
    "PayrollReceiptPreview",
    "PayrollReceiptPreviewDeductionsItem",
    "PayrollReceiptPreviewIsr",
    "PayrollReceiptPreviewIsrAdjustment",
    "PayrollReceiptPreviewOtherPaymentsItem",
    "PayrollReceiptPreviewOtherPaymentsItemBalanceCompensation",
    "PayrollReceiptPreviewPerceptionsItem",
    "PayrollReceiptPreviewPerceptionsItemOvertimeItem",
    "PayrollReceiptPreviewPerceptionsItemStockOptions",
    "PayrollReceiptPreviewPeriod",
    "PayrollReceiptPreviewTotals",
    "PayrollReceiptPreviewWarningsItem",
    "PortalSupplier",
    "PortalSupplierApprovedEvent",
    "PortalSupplierBankAccount",
    "PortalSupplierDocuments",
    "PortalSupplierList",
    "PortalSupplierScore",
    "PortalSupplierScorePartsItem",
    "PreviewPayrollReceiptParams",
    "PreviewPayrollReceiptParamsPeriod",
    "PriceList",
    "PriceListItemsItem",
    "PriceListList",
    "PriceQuote",
    "PriceQuoteItemsItem",
    "PriceQuoteItemsItemNextStep",
    "Product",
    "ProductList",
    "ProductLocalTaxesItem",
    "PurchaseReceipt",
    "PurchaseReceiptFieldsItem",
    "PurchaseReceiptList",
    "PurchaseReceiptRequested",
    "PurchaseReceiptStore",
    "Quote",
    "QuoteAcceptedEvent",
    "QuoteChangesRequestedEvent",
    "QuoteCustomer",
    "QuoteItemsItem",
    "QuoteList",
    "QuotePricesParams",
    "QuotePricesParamsItemsItem",
    "QuoteRejectedEvent",
    "QuoteViewedEvent",
    "QuoteWithdrawnEvent",
    "Receivable",
    "ReceivableCustomer",
    "ReceivableList",
    "RecurringInvoice",
    "RecurringInvoiceCustomer",
    "RecurringInvoiceFailedEvent",
    "RecurringInvoiceItemsItem",
    "RecurringInvoiceLastError",
    "RecurringInvoiceList",
    "RecurringInvoiceSchedule",
    "RefreshSatDeclarationsParams",
    "RejectQuoteParams",
    "ReportImssMovementsParams",
    "RequestPurchaseReceiptInvoiceParams",
    "ResetTestDataParams",
    "Retention",
    "RetentionCanceledEvent",
    "RetentionCancellation",
    "RetentionEmail",
    "RetentionError",
    "RetentionFailedEvent",
    "RetentionList",
    "RetentionPeriod",
    "RetentionRecipient",
    "RetentionStampedEvent",
    "RetentionTaxesItem",
    "RetentionTotals",
    "ReturnExpenseReportParams",
    "RollWebhookSecretParams",
    "SalesOrder",
    "SalesOrderCanceledEvent",
    "SalesOrderConfirmedEvent",
    "SalesOrderCustomer",
    "SalesOrderCustomerConfirmedEvent",
    "SalesOrderDeliveredEvent",
    "SalesOrderDelivery",
    "SalesOrderDeliveryItemsItem",
    "SalesOrderInvoicesItem",
    "SalesOrderItemsItem",
    "SalesOrderList",
    "SalesOrderPaidEvent",
    "Sandbox",
    "SandboxKey",
    "SandboxList",
    "SatCatalogEntry",
    "SatCatalogEntryList",
    "SatDeclaration",
    "SatDeclarationCalendar",
    "SatDeclarationCalendarMonthsItem",
    "SatDeclarationCalendarMonthsItemObligationsItem",
    "SatDeclarationCreatedEvent",
    "SatDeclarationFiles",
    "SatDeclarationList",
    "SatDeclarationReceipt",
    "SatDeclarationReceiptConceptsItem",
    "SatDeclarationSectionsItem",
    "SatDeclarationSectionsItemFieldsItem",
    "SatDeclarationSummary",
    "SatDeclarationSummaryObligationsItem",
    "SatDeclarationUpdatedEvent",
    "SatDeclarationsRefresh",
    "SatDownload",
    "SatDownloadCompletedEvent",
    "SatDownloadFailedEvent",
    "SatDownloadList",
    "SatFinding",
    "SatFindingCounterparty",
    "SatFindingCounterpartyFindingsItem",
    "SatFindingCounterpartyList",
    "SatFindingList",
    "SatInvoice",
    "SatInvoiceIssuedBy",
    "SatInvoiceIssuedTo",
    "SatInvoiceList",
    "SatInvoiceTaxes",
    "SatListCheck",
    "SatListCheckList",
    "SatListCheckListsItem",
    "SatMailboxMessage",
    "SatMailboxMessageList",
    "SatRefresh",
    "SatRetention",
    "SatRetentionIssuedBy",
    "SatRetentionIssuedTo",
    "SatRetentionList",
    "SatRetentionPeriod",
    "SatRetentionTotals",
    "SatRetentionWithheldTaxesItem",
    "ScheduleSupplierInvoiceParams",
    "SelfInvoicing",
    "SendInvoiceParams",
    "SendQuoteParams",
    "SendRetentionParams",
    "SendSalesOrderParams",
    "SignEfirmaParams",
    "StockAdjustment",
    "StockAdjustmentLinesItem",
    "StockAdjustmentList",
    "StockLevel",
    "StockLevelList",
    "StockMovement",
    "StockMovementList",
    "StockMovementSource",
    "StoreConnection",
    "StoreConnectionLastError",
    "StoreConnectionList",
    "StoreConnectionSettings",
    "StoreImport",
    "StoreImportSkippedItem",
    "SupplierInvoice",
    "SupplierInvoiceApprovedEvent",
    "SupplierInvoiceList",
    "SupplierInvoicePaidEvent",
    "SupplierInvoiceReceivedEvent",
    "SupplierInvoiceRejectedEvent",
    "SupplierInvoiceScheduledEvent",
    "SupplierInvoiceWarningsItem",
    "TaxIdValidation",
    "TaxIdValidationErrorsItem",
    "TaxIdValidationSatRecord",
    "TaxIdValidationWarningsItem",
    "TaxStatusCertificate",
    "TaxStatusCertificateTaxSystemsItem",
    "TestClock",
    "TestClockAdvanced",
    "TestClockReadyEvent",
    "TestDataReset",
    "TestWebhookEndpointParams",
    "Ticket",
    "TicketBuyer",
    "TicketCustomer",
    "TicketIncludedInGlobalEvent",
    "TicketInvoicedEvent",
    "TicketLinesItem",
    "TicketList",
    "TrialBalance",
    "TrialBalanceAccountsItem",
    "TrialBalanceTotals",
    "UpdateAccountParams",
    "UpdateBranchParams",
    "UpdateBranchParamsAddress",
    "UpdateBranchParamsSeries",
    "UpdateCostCenterParams",
    "UpdateCustomerGroupParams",
    "UpdateCustomerParams",
    "UpdateCustomerParamsForeign",
    "UpdateEmployeeParams",
    "UpdateExpenseItemParams",
    "UpdateExpensePersonParams",
    "UpdateExpensePolicyParams",
    "UpdateExpensePolicyParamsLimitsValue",
    "UpdateExpenseReportParams",
    "UpdateImssMovementParams",
    "UpdateInvoiceParams",
    "UpdateIssuerParams",
    "UpdateIssuerParamsDonationAuthorization",
    "UpdatePriceListParams",
    "UpdatePriceListParamsItemsItem",
    "UpdateProductParams",
    "UpdateProductParamsLocalTaxesItem",
    "UpdatePurchaseReceiptParams",
    "UpdatePurchaseReceiptParamsFieldsItem",
    "UpdateQuoteParams",
    "UpdateQuoteParamsCustomer1",
    "UpdateQuoteParamsCustomer1Foreign",
    "UpdateQuoteParamsCustomer2",
    "UpdateQuoteParamsItemsItem",
    "UpdateQuoteParamsItemsItemIedu",
    "UpdateQuoteParamsItemsItemThirdParty",
    "UpdateQuoteParamsItemsItemUsedVehicle",
    "UpdateQuoteParamsItemsItemUsedVehicleCustomsItem",
    "UpdateRecurringInvoiceParams",
    "UpdateRecurringInvoiceParamsInvoice",
    "UpdateRecurringInvoiceParamsSchedule",
    "UpdateSalesOrderParams",
    "UpdateSalesOrderParamsCustomer",
    "UpdateSalesOrderParamsCustomerForeign",
    "UpdateSalesOrderParamsItemsItem",
    "UpdateSalesOrderParamsItemsItemIedu",
    "UpdateSalesOrderParamsItemsItemThirdParty",
    "UpdateSalesOrderParamsItemsItemUsedVehicle",
    "UpdateSalesOrderParamsItemsItemUsedVehicleCustomsItem",
    "UpdateSatInvoiceParams",
    "UpdateSelfInvoicingParams",
    "UpdateStoreConnectionParams",
    "UpdateStoreConnectionParamsSettings",
    "UpdateWebhookEndpointParams",
    "UploadCertificateParams",
    "Usage",
    "UsageHighEvent",
    "ValidateTaxIdParams",
    "VatRefund",
    "VatRefundBalancesItem",
    "VatRefundBalancesItemCreditedInItem",
    "VatRefundReview",
    "VatRefundReviewChecksItem",
    "VatRefundReviewCustomers",
    "VatRefundReviewSuppliers",
    "Warehouse",
    "WarehouseList",
    "WebhookEndpoint",
    "WebhookEndpointList",
    "WebhookTest",
    "WebhookTestDelivery",
    "WithdrawQuoteParams",
]


class AccountKey(TypedDict):
    """La llave con que se hizo la solicitud: id, nombre y emisores a los que se limita."""
    id: str
    """Id de la llave."""
    name: str
    """Nombre de la llave."""
    issuers: list[str] | None
    """Emisores a los que se limita la llave; null si puede usar todos."""
    read_only: bool
    """true si la llave solo consulta (key_read_only en lo demás)."""
    expires_at: str | None
    """Cuándo deja de funcionar: la vigencia elegida al crearla, o el fin del traslape al cambiarla. null si no vence."""
    sandbox: str | None
    """El entorno de prueba (sbx_…) de la llave: solo ve sus emisores, webhooks y eventos. null si es de la cuenta."""


class Account(TypedDict):
    """La cuenta API de la llave que hizo la solicitud."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["account"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    name: str
    """El nombre de la cuenta API."""
    api_version: str
    """La versión de la API de la cuenta (la de sus solicitudes sin Fiscalisto-Version). Ver Versiones."""
    latest_api_version: str
    """La versión más reciente de la API."""
    key: AccountKey
    """La llave con que se hizo la solicitud: id, nombre y emisores a los que se limita."""


class BalanceAutoRecharge(TypedDict):
    timbres: int
    """Timbres del paquete que se compra."""
    at: int
    """Se compra con esta cantidad o menos."""
    max_per_month: int
    """Como máximo tantas compras al mes."""


class BalancePacksItem(TypedDict):
    timbres: int
    """Timbres del paquete."""
    remaining: int
    """Los que le quedan."""
    purchased_at: str | None
    """Cuándo se compró."""
    expires_at: str | None
    """Cuándo vencen; null si no vencen."""


class Balance(TypedDict):
    """Timbres de producción de la cuenta, por paquete, el que vence antes primero."""
    object: Literal["balance"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    available: int
    """Timbres disponibles en total."""
    unlimited: bool
    """true si la cuenta timbra sin usar timbres."""
    low_balance_at: int
    """Con esta cantidad o menos llega balance.low (y otra vez al acabarse). Se elige en Desarrolladores › Timbres."""
    auto_recharge: BalanceAutoRecharge | None
    """La recarga automática con la tarjeta guardada, o null si está apagada."""
    packs: list[BalancePacksItem]
    """Los paquetes con timbres, el que vence antes primero (en ese orden se usan)."""


class Usage(TypedDict):
    """Las solicitudes de producción de los últimos 30 días contra las que tiene."""
    object: Literal["usage"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """Siempre true: solo cuenta producción."""
    period_days: int
    """Los días que cuenta: los últimos 30."""
    requests: int
    """Solicitudes de producción en esos días."""
    allowance: int
    """Las que tiene: 10,000 en el plan Gratis o 100,000 con un plan de paga, más 500 por cada timbre de la API que usó en esos días."""
    percent_used: Literal[80] | Literal[100]
    """Llega al usar el 80 % y otra vez al 100 %."""
    plan: Literal["free", "paid"]
    """free: la empresa está en Gratis (o en su prueba); paid: tiene un plan de paga."""
    over_allowance: Literal["refused", "slowed"]
    """Qué pasa al pasarlas: refused (Gratis: 429 monthly_allowance) o slowed (de paga: 10 solicitudes cada 10 segundos)."""


class IssuerCertificate(TypedDict):
    serial_number: str | None
    """Número de serie (NoCertificado)."""
    expires_at: str | None
    """Cuándo vence."""


class IssuerSatDownloads(TypedDict):
    """Si puede pedirle al SAT sus facturas (POST /v1/sat_downloads): available es true en pruebas, y en producción mientras su e.firma guardada esté vigente (efirma_expires_at)."""
    available: bool
    """true si puede pedir descargas al SAT ahora: siempre en pruebas; en producción con su e.firma guardada y vigente."""
    efirma_expires_at: str | None
    """Cuándo vence la e.firma guardada para las descargas, o null si no hay una."""


class IssuerDonationAuthorization(TypedDict):
    number: str
    """Número del oficio de autorización, hasta 100 caracteres."""
    date: str | None
    """Fecha del oficio, AAAA-MM-DD; no puede ser futura."""


class IssuerTestClock(TypedDict):
    frozen_time: str
    """La hora del reloj."""


class Issuer(TypedDict):
    """Un emisor: un RFC que timbra desde su cuenta API."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["issuer"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    source: Literal["api", "empresa"]
    """api si lo creó con la API o en Desarrolladores; empresa si es una empresa de la app conectada a su cuenta (Desarrolladores › Emisores › Conectar una empresa): con ella solo se usa su Portal de proveedores, y status siempre es active."""
    type: Literal["own", "connected", "portal"]
    """own: un RFC de la empresa de esta API (lo da de alta la empresa en la app; no se archiva por la API). connected: un emisor conectado, que su plataforma agregó con POST /v1/issuers. portal: otra empresa de Fiscalisto conectada por su Portal de proveedores."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str | None
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str | None
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    status: Literal["active", "needs_certificate", "certificate_expired", "needs_efirma", "archived"]
    """active: puede timbrar. needs_certificate: falta su CSD. needs_efirma: falta firmar una vez el contrato con el PAC con su e.firma (solo en producción). certificate_expired: su CSD venció. archived: archivado."""
    requirement: str | None
    """Qué le falta al emisor para timbrar, y cómo dárselo."""
    certificate: IssuerCertificate | None
    """El sello digital (CSD) cargado: número de serie y vencimiento."""
    sat_downloads: IssuerSatDownloads
    """Si puede pedirle al SAT sus facturas (POST /v1/sat_downloads): available es true en pruebas, y en producción mientras su e.firma guardada esté vigente (efirma_expires_at)."""
    employer_registration: str | None
    """Registro patronal ante el IMSS (RegistroPatronal), 11 caracteres. Necesario para timbrar nómina."""
    curp: str | None
    """CURP, 18 caracteres."""
    donation_authorization: IssuerDonationAuthorization | None
    """Donataria autorizada (régimen 603): el oficio del SAT que la autoriza a recibir donativos deducibles (o su renovación). Va en cada recibo de donativo (`donation` de POST /v1/invoices); null lo quita. El emisor debe tener tax_system 603. En pruebas sirve cualquier número y una fecha pasada."""
    stamps_as: str
    """RFC con el que se timbra: el del emisor en producción y el de pruebas del SAT (EKU9003173C9) en pruebas, con régimen 601 o, si el emisor es donataria (tax_system 603), 603."""
    sandbox: str | None
    """El entorno de prueba (sbx_…) al que pertenece, o null si es de la cuenta. Vea /v1/sandboxes."""
    test_clock: IssuerTestClock | None
    """Su reloj de prueba (solo emisores de prueba): la hora que es «hoy» para él, o null si va con la hora real. Vea POST /v1/issuers/{id}/test_clock."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    archived_at: str | None
    """Cuándo se archivó (ya no timbra), o null."""
    metadata: dict[str, str]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class InvoiceItem(TypedDict):
    """Un concepto, con los mismos campos con que se mandó."""
    pass


class InvoicePayrollPeriod(TypedDict):
    """Periodo pagado: FechaInicialPago, FechaFinalPago y FechaPago."""
    start: str
    """Primer día del periodo (FechaInicialPago), AAAA-MM-DD."""
    end: str
    """Último día del periodo (FechaFinalPago), AAAA-MM-DD."""
    payment_date: str
    """Fecha de pago (FechaPago), AAAA-MM-DD. Por omisión el último día del periodo."""


class InvoicePayrollReferences(TypedDict):
    employee_id: str | None
    """El id del empleado en su sistema de nómina."""
    payroll_run_id: str | None
    """El id de la corrida de nómina en su sistema."""


class InvoicePayrollEmployerSncf(TypedDict):
    """Entidad del SNCF (EntidadSNCF)."""
    resource_origin: str
    """Origen del recurso (OrigenRecurso): IP, IF o IM."""
    own_resource_amount: float | None
    """Monto de recursos propios (MontoRecursoPropio), con IM."""


class InvoicePayrollEmployer(TypedDict):
    """El patrón (Emisor del complemento): registro patronal y CURP si es persona física."""
    employer_registration: str | None
    """Registro patronal ante el IMSS (RegistroPatronal), 11 caracteres. Necesario para timbrar nómina."""
    curp: str | None
    """CURP, 18 caracteres."""
    origin_tax_id: NotRequired[str]
    """RFC del patrón de origen (RfcPatronOrigen)."""
    sncf: NotRequired[InvoicePayrollEmployerSncf]
    """Entidad del SNCF (EntidadSNCF)."""


class InvoicePayrollEmployeeSubcontractingItem(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    percentage: float
    """Porcentaje de tiempo (PorcentajeTiempo)."""


class InvoicePayrollEmployee(TypedDict):
    """El empleado (Nomina/Receptor), como se timbró."""
    id: str | None
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    number: str
    """Número de empleado (NumEmpleado)."""
    curp: str
    """CURP, 18 caracteres."""
    social_security_number: str | None
    """Número de seguridad social (NumSeguridadSocial), 11 dígitos."""
    start_date: str | None
    """Fecha de inicio de la relación laboral (FechaInicioRelLaboral), AAAA-MM-DD."""
    seniority: str | None
    """Antigüedad (P52W, P1Y2M3D)."""
    contract_type: str
    """Tipo de contrato (TipoContrato), c_TipoContrato. Por omisión 01, por tiempo indeterminado."""
    unionized: bool | None
    """true si es sindicalizado (Sindicalizado)."""
    workday_type: str | None
    """Tipo de jornada (TipoJornada), c_TipoJornada. Por omisión 01, diurna."""
    regime_type: str
    """Tipo de régimen (TipoRegimen): 02 sueldos y salarios."""
    department: str | None
    """Departamento (Departamento)."""
    position: str | None
    """Puesto (Puesto)."""
    risk_class: str | None
    """Clase de riesgo del puesto ante el IMSS (RiesgoPuesto), 1 a 5. Por omisión 1."""
    contribution_base_salary: float | None
    """Salario base de cotización (SalarioBaseCotApor)."""
    integrated_daily_salary: float | None
    """Salario diario integrado (SalarioDiarioIntegrado): no menor al salario diario."""
    state: str
    """Entidad federativa donde trabaja (ClaveEntFed): JAL, CMX, NLE…"""
    bank: NotRequired[str]
    """Banco (Banco), c_Banco."""
    bank_account: NotRequired[str]
    """Cuenta bancaria o CLABE (CuentaBancaria)."""
    subcontracting: NotRequired[list[InvoicePayrollEmployeeSubcontractingItem]]
    """Subcontratación (SubContratacion)."""


class InvoicePayrollPerceptionsItemOvertimeItem(TypedDict):
    days: int
    """Días con horas extra (Dias)."""
    hours_type: str
    """c_TipoHoras: 01 dobles, 02 triples, 03 simples."""
    hours: int
    """Horas extra (HorasExtra)."""
    amount_paid: float
    """Importe pagado (ImportePagado)."""


class InvoicePayrollPerceptionsItemStockOptions(TypedDict):
    """Acciones o títulos (AccionesOTitulos), con la percepción 045."""
    market_value: float
    """Valor de mercado (ValorMercado)."""
    grant_price: float
    """Precio al otorgarse (PrecioAlOtorgarse)."""


class InvoicePayrollPerceptionsItem(TypedDict):
    type: str
    """Tipo de percepción (TipoPercepcion), c_TipoPercepcion: 001 sueldos…"""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    taxed: float
    """Importe gravado (ImporteGravado)."""
    exempt: float
    """Importe exento (ImporteExento)."""
    overtime: NotRequired[list[InvoicePayrollPerceptionsItemOvertimeItem]]
    """Horas extra (HorasExtra), con la percepción 019."""
    stock_options: NotRequired[InvoicePayrollPerceptionsItemStockOptions]
    """Acciones o títulos (AccionesOTitulos), con la percepción 045."""


class InvoicePayrollDeductionsItem(TypedDict):
    type: str
    """Tipo de deducción (TipoDeduccion), c_TipoDeduccion: 001 IMSS, 002 ISR…"""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    amount: float
    """Importe (Importe)."""


class InvoicePayrollOtherPaymentsItemBalanceCompensation(TypedDict):
    """Compensación del saldo a favor (CompensacionSaldosAFavor), con el 004."""
    balance: float
    """Saldo a favor (SaldoAFavor)."""
    year: int
    """Año del saldo a favor (Año)."""
    remaining: float
    """Remanente del saldo a favor (RemanenteSalFav)."""


class InvoicePayrollOtherPaymentsItem(TypedDict):
    type: str
    """Tipo de otro pago (TipoOtroPago), c_TipoOtroPago: 002 subsidio para el empleo."""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    amount: float
    """Importe pagado (Importe)."""
    subsidy_caused: NotRequired[float]
    """Subsidio causado (SubsidioCausado)."""
    subsidy_applied: NotRequired[float]
    """Del subsidio causado, el ISR que evitó (no va en el XML)."""
    balance_compensation: NotRequired[InvoicePayrollOtherPaymentsItemBalanceCompensation]
    """Compensación del saldo a favor (CompensacionSaldosAFavor), con el 004."""


class InvoicePayrollSeparation(TypedDict):
    """SeparacionIndemnizacion (percepciones 022, 023, 025)."""
    total_paid: float
    """Total pagado (TotalPagado)."""
    years_of_service: int
    """Años de servicio (NumAñosServicio)."""
    last_monthly_salary: float
    """Último sueldo mensual ordinario (UltimoSueldoMensOrd)."""
    accumulable_income: float
    """Ingreso acumulable (IngresoAcumulable)."""
    non_accumulable_income: float
    """Ingreso no acumulable (IngresoNoAcumulable)."""


class InvoicePayrollRetirement(TypedDict):
    """JubilacionPensionRetiro (percepciones 039, 044)."""
    total_one_payment: NotRequired[float]
    """Total en una exhibición (TotalUnaExhibicion)."""
    total_installment: NotRequired[float]
    """Total en parcialidades (TotalParcialidad)."""
    daily_amount: NotRequired[float]
    """Monto diario (MontoDiario)."""
    accumulable_income: float
    """Ingreso acumulable (IngresoAcumulable)."""
    non_accumulable_income: float
    """Ingreso no acumulable (IngresoNoAcumulable)."""


class InvoicePayrollDisabilitiesItem(TypedDict):
    days: int
    """Días pagados (NumDiasPagados). Por omisión, todos los del periodo que le tocan."""
    type: str
    """Tipo de comprobante (TipoDeComprobante): I ingreso, E egreso, P pago, T traslado, N nómina."""
    amount: float | None
    """Importe."""


class InvoicePayrollTotals(TypedDict):
    """Totales: percepciones, deducciones, otros pagos y el neto a pagar."""
    salaries: float
    """Total de sueldos, salarios y asimilados (TotalSueldos)."""
    taxed: float
    """Total gravado (TotalGravado)."""
    exempt: float
    """Total exento (TotalExento)."""
    separation: float
    """Total de separación e indemnización (TotalSeparacionIndemnizacion)."""
    retirement: float
    """Total de jubilación, pensión o retiro (TotalJubilacionPensionRetiro)."""
    perceptions: float
    """Total de percepciones (TotalPercepciones)."""
    other_deductions: float
    """Otras deducciones (TotalOtrasDeducciones)."""
    taxes_withheld: float
    """Impuestos retenidos (TotalImpuestosRetenidos)."""
    deductions: float
    """Total de deducciones (TotalDeducciones)."""
    other_payments: float
    """Total de otros pagos (TotalOtrosPagos)."""
    subtotal: float
    """Subtotal del comprobante: percepciones más otros pagos."""
    net: float
    """Neto a pagar al empleado."""


class InvoicePayroll(TypedDict):
    """El complemento de nómina 1.2 como se timbró: tipo, periodo, patrón, empleado, percepciones, deducciones, otros pagos, sus nodos y los totales."""
    type: Literal["O", "E"]
    """TipoNomina: O ordinaria, E extraordinaria."""
    calculation: Literal["fiscalisto", "external"]
    """fiscalisto: lo calculó Fiscalisto (POST /v1/payroll_receipts); external: lo calculó su sistema de nómina y se timbró tal cual (POST /v1/payroll_receipts/external)."""
    periodicity: str
    """Periodicidad del pago (PeriodicidadPago): 02 semanal, 03 catorcenal, 04 quincenal (por omisión), 05 mensual."""
    period: InvoicePayrollPeriod
    """Periodo pagado: FechaInicialPago, FechaFinalPago y FechaPago."""
    days: float
    """Días pagados (NumDiasPagados). Por omisión, todos los del periodo que le tocan."""
    references: InvoicePayrollReferences | None
    """Los ids de su sistema de nómina (solo en recibos external)."""
    employer: InvoicePayrollEmployer
    """El patrón (Emisor del complemento): registro patronal y CURP si es persona física."""
    employee: InvoicePayrollEmployee
    """El empleado (Nomina/Receptor), como se timbró."""
    perceptions: list[InvoicePayrollPerceptionsItem]
    """Percepciones (Percepcion): sueldo y demás, gravado y exento."""
    deductions: list[InvoicePayrollDeductionsItem]
    """Deducciones (Deduccion): ISR, cuotas IMSS y demás."""
    other_payments: list[InvoicePayrollOtherPaymentsItem]
    """Otros pagos (OtroPago): subsidio para el empleo."""
    separation: NotRequired[InvoicePayrollSeparation]
    """SeparacionIndemnizacion (percepciones 022, 023, 025)."""
    retirement: NotRequired[InvoicePayrollRetirement]
    """JubilacionPensionRetiro (percepciones 039, 044)."""
    disabilities: NotRequired[list[InvoicePayrollDisabilitiesItem]]
    """Incapacidades (percepción 014 o deducción 006)."""
    totals: InvoicePayrollTotals
    """Totales: percepciones, deducciones, otros pagos y el neto a pagar."""


class InvoiceCustomer(TypedDict):
    """El cliente (Receptor) como quedó en el CFDI: RFC, nombre, régimen fiscal y código postal (y foreign si es extranjero)."""
    tax_id: str | None
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: NotRequired[str]
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal del cliente (DomicilioFiscalReceptor), 5 dígitos."""
    foreign: NotRequired[dict[str, Any]]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""


class InvoiceTaxes(TypedDict):
    iva: float | None
    """IVA trasladado."""
    ieps: float | None
    """IEPS trasladado."""
    iva_withheld: float | None
    """IVA retenido."""
    isr_withheld: float | None
    """ISR retenido."""
    local_transferred: float | None
    """Impuestos locales trasladados."""
    local_withheld: float | None
    """Impuestos locales retenidos."""


class InvoicePaymentDocumentsItem(TypedDict):
    uuid: str
    """Folio fiscal que asigna el SAT (UUID del Timbre Fiscal Digital), en mayúsculas."""
    series: str | None
    """Serie de la factura pagada."""
    folio: str | None
    """Folio de la factura pagada."""
    currency: str
    """Moneda de la factura pagada (MonedaDR)."""
    partiality: int
    """Número de parcialidad (NumParcialidad)."""
    previous_balance: float
    """Saldo anterior de la factura (ImpSaldoAnt)."""
    amount: float
    """Lo que se paga de esa factura (ImpPagado), en la moneda de la factura."""
    remaining: float
    """Saldo insoluto después de este pago (ImpSaldoInsoluto)."""


class InvoicePayment(TypedDict):
    date: str | None
    """Fecha del pago (FechaPago)."""
    payment_form: str | None
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    currency: str
    """Moneda del pago (MonedaP)."""
    exchange_rate: float | None
    """Tipo de cambio a pesos (TipoCambio). Obligatorio si la moneda no es MXN; use el del DOF del día anterior."""
    amount: float
    """Monto del pago (Monto)."""
    operation_number: str | None
    """Número de operación del pago (NumOperacion), como el rastreo SPEI."""
    documents: list[InvoicePaymentDocumentsItem]
    """Las facturas que paga (DoctoRelacionado)."""


class InvoiceCancellation(TypedDict):
    status: str | None
    """pending (espera la respuesta del cliente), accepted (cancelada), rejected (el cliente la rechazó) o lapsed (venció; puede pedirla otra vez)."""
    motive: str | None
    """Motivo de cancelación (c_MotivoCancelacion): 01 con errores con relación (lleva substitution), 02 con errores sin relación (por omisión), 03 no se llevó a cabo, 04 solo en una factura global, cuando una venta incluida se facturó a nombre del cliente."""
    substitution: str | None
    """El comprobante que sustituye a este (su id o su UUID), con el motivo 01."""
    canceled_at: str | None
    """Cuándo se canceló."""


class InvoiceEmailRecipientsItem(TypedDict):
    address: str
    """La dirección de correo del destinatario."""
    status: Literal["sent", "delayed", "delivered", "opened", "bounced", "complained"]
    """Estado del objeto."""
    delivered_at: str | None
    """Cuando el servidor del destinatario lo aceptó."""
    opened_at: str | None
    """La primera vez que se abrió (aproximado: algunos correos cargan las imágenes solos o no las cargan)."""
    bounced_at: str | None
    """Cuando rebotó."""
    bounce_reason: str | None
    """Por qué rebotó, en español: «buzón no existe», «buzón lleno»…"""
    complained_at: str | None
    """Cuando el destinatario lo marcó como spam."""


class InvoiceEmail(TypedDict):
    to: str | None
    """A quién (correos separados por comas)."""
    cc: str | None
    """Con copia (correos separados por comas)."""
    sent_at: str | None
    """Cuándo se envió."""
    status: Literal["sent", "delayed", "delivered", "opened", "bounced", "complained"]
    """Lo que pasó con el último envío: el peor de sus destinatarios (bounced o complained pesan más que opened o delivered). sent hasta que el servidor del cliente conteste."""
    recipients: list[InvoiceEmailRecipientsItem]
    """Cada dirección del envío (para y copia), con su entrega."""


class InvoiceError(TypedDict):
    message: str
    """Qué pasó y cómo corregirlo, para una persona."""
    sat_code: str | None
    """Código del SAT o del PAC (CFDI40xxx)."""
    raw: str
    """El texto original del PAC."""


class InvoiceSubstitutes(TypedDict):
    """La factura que esta sustituyó y si quedó cancelada."""
    invoice: str
    """La factura sustituida (inv_…)."""
    canceled: bool
    """true si la sustituida ya quedó cancelada."""
    cancel_error: NotRequired[str]
    """Por qué no se pudo cancelar la sustituida (cancélela con POST /v1/invoices/{id}/cancel)."""


class InvoiceAdvanceApplication(TypedDict):
    """La aplicación del anticipo: método, nota de aplicación y su estado."""
    advance: str | None
    """El anticipo, como factura (inv_…)."""
    advance_uuid: str
    """El folio fiscal del anticipo."""
    method: Literal["egreso", "remanente"]
    """egreso (la factura completa y después una nota de crédito por el anticipo, opción A) o remanente (la factura solo por lo que falta, opción B)."""
    status: Literal["done", "credit_note_pending"]
    """done (listo) o credit_note_pending (falta timbrar la nota de aplicación: repita la solicitud con la misma Idempotency-Key)."""
    credit_note: str | None
    """La nota de aplicación del anticipo (inv_…), con method egreso."""
    credit_note_error: NotRequired[str]
    """Por qué no se timbró la nota de aplicación (repita con la misma Idempotency-Key)."""


# Un CFDI 4.0 emitido: factura de ingreso o global, traslado, nota de crédito (E), complemento de pago (P) o recibo de nómina (N).
Invoice = TypedDict(
    "Invoice",
    {
        "id": "str",
        "livemode": "bool",
        "object": "Literal[\"invoice\"]",
        "issuer": "str",
        "branch": "str | None",
        "cost_center": "str | None",
        "type": "Literal[\"I\", \"E\", \"P\", \"T\", \"N\"]",
        "status": "Literal[\"processing\", \"pending\", \"valid\", \"rejected\", \"canceled\"]",
        "uuid": "str | None",
        "series": "str | None",
        "folio": "str | None",
        "date": "str | None",
        "customer": "InvoiceCustomer",
        "use": "str | None",
        "payment_form": "str | None",
        "payment_method": "str | None",
        "currency": "str",
        "exchange_rate": "float | None",
        "items": "list[InvoiceItem]",
        "subtotal": "float | None",
        "discount": "float | None",
        "taxes": "InvoiceTaxes | None",
        "total": "float | None",
        "payment_status": "Literal[\"paid\", \"partial\", \"unpaid\"] | None",
        "amount_due": "float | None",
        "amount_paid": "float | None",
        "paid_on": "str | None",
        "related": "dict[str, Any] | None",
        "payment": "NotRequired[InvoicePayment | None]",
        "payroll": "NotRequired[InvoicePayroll]",
        "global": "NotRequired[dict[str, Any]]",
        "cancellation": "InvoiceCancellation | None",
        "email": "InvoiceEmail | None",
        "error": "InvoiceError | None",
        "recurring_invoice": "str | None",
        "created_at": "str | None",
        "metadata": "dict[str, str]",
        "warnings": "NotRequired[list[str]]",
        "email_error": "NotRequired[str]",
        "substitutes": "NotRequired[InvoiceSubstitutes]",
        "advance_application": "NotRequired[InvoiceAdvanceApplication]",
    },
)


class RetentionRecipient(TypedDict):
    """Receptor de la constancia (Receptor): nacional con RFC y código postal, o extranjero."""
    foreign: bool
    """true si el receptor es extranjero (sin RFC)."""
    tax_id: str | None
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    curp: NotRequired[str | None]
    """CURP, 18 caracteres."""


class RetentionPeriod(TypedDict):
    """Periodo (Periodo): mes inicial, mes final y año."""
    year: int
    """Año (Ejercicio)."""
    from_month: int
    """Mes inicial (MesIni), 1 a 12."""
    to_month: int
    """Mes final (MesFin), 1 a 12, del mismo año."""


class RetentionTotals(TypedDict):
    """Totales (Totales)."""
    operation: float | None
    """Monto total de la operación (MontoTotOperacion)."""
    taxed: float | None
    """Monto gravado (MontoTotGrav). Por omisión, operation menos exempt."""
    exempt: float | None
    """Monto exento (MontoTotExent). Por omisión 0."""
    withheld: float | None
    """Total retenido (MontoTotRet)."""


class RetentionTaxesItem(TypedDict):
    tax: str
    """Impuesto: isr, iva o ieps (ImpuestoRet 001, 002, 003)."""
    base: float
    """Base del impuesto retenido (BaseRet)."""
    amount: float
    """Monto retenido (MontoRet)."""
    payment_type: str
    """Tipo de pago de la retención (TipoPagoRet): 01 definitivo IVA, 02 definitivo IEPS, 03 definitivo ISR, 04 provisional ISR. Por omisión el usual de cada impuesto."""


class RetentionCancellation(TypedDict):
    status: str
    """pending (espera la respuesta del cliente), accepted (cancelada), rejected (el cliente la rechazó) o lapsed (venció; puede pedirla otra vez)."""
    motive: str | None
    """Motivo de cancelación (c_MotivoCancelacion): 01 con errores con relación (lleva substitution), 02 con errores sin relación (por omisión), 03 no se llevó a cabo, 04 solo en una factura global, cuando una venta incluida se facturó a nombre del cliente."""
    canceled_at: str | None
    """Cuándo se canceló."""


class RetentionEmail(TypedDict):
    to: str | None
    """A quién (correos separados por comas)."""
    sent_at: str | None
    """Cuándo se envió."""


class RetentionError(TypedDict):
    message: str
    """Qué pasó y cómo corregirlo, para una persona."""
    sat_code: str | None
    """Código del SAT o del PAC (CFDI40xxx)."""
    raw: str
    """El texto original del PAC."""


class Retention(TypedDict):
    """Una constancia de retenciones e información de pagos (CFDI de retenciones 2.0)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["retention"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    status: Literal["processing", "valid", "rejected", "canceled"]
    """processing: el PAC no ha contestado. valid: timbrada. rejected: el SAT o el PAC no la aceptaron (ver error). canceled: cancelada."""
    uuid: str | None
    """Folio fiscal que asigna el SAT (UUID del Timbre Fiscal Digital), en mayúsculas."""
    folio: int | None
    """El número de la constancia en la serie del emisor (internal_folio es el que se imprime, RET1…)."""
    internal_folio: str | None
    """Folio interno (FolioInt): RET1, RET2…"""
    date: str | None
    """Fecha de emisión (Fecha), hora de la Ciudad de México."""
    code: str
    """Clave de la retención (CveRetenc), c_CveRetenc: 01 servicios profesionales, 05 arrendamiento, 14 dividendos, 16 intereses, 18 pagos al extranjero… Las claves 14, 16, 17 y 18 a 24 llevan su complemento (dividends, interest, trust_lease, foreign_payment, share_sale, prize, trust, retirement_plan, mortgage_interest, financial_derivatives); la 26 (plataformas tecnológicas) lleva platform, y sus totals y taxes se calculan de las operaciones."""
    description: str | None
    """Descripción de la retención (DescRetenc)."""
    recipient: RetentionRecipient
    """Receptor de la constancia (Receptor): nacional con RFC y código postal, o extranjero."""
    period: RetentionPeriod
    """Periodo (Periodo): mes inicial, mes final y año."""
    totals: RetentionTotals
    """Totales (Totales)."""
    taxes: list[RetentionTaxesItem]
    """Impuestos del comprobante, por tipo."""
    dividends: NotRequired[dict[str, Any]]
    """Complemento de dividendos."""
    interest: NotRequired[dict[str, Any]]
    """Complemento de intereses."""
    foreign_payment: NotRequired[dict[str, Any]]
    """Complemento de pagos a extranjeros."""
    trust_lease: NotRequired[dict[str, Any]]
    """Complemento de arrendamiento en fideicomiso (Arrendamientoenfideicomiso 1.0), obligatorio con code 17."""
    share_sale: NotRequired[dict[str, Any]]
    """Complemento de enajenación de acciones u operaciones de valores (EnajenaciondeAcciones 1.0), obligatorio con code 19."""
    prize: NotRequired[dict[str, Any]]
    """Complemento de premios (Premios 1.0), obligatorio con code 20. Sus montos son los de totals."""
    trust: NotRequired[dict[str, Any]]
    """Complemento de fideicomisos que no realizan actividades empresariales (Fideicomisonoempresarial 1.0), obligatorio con code 21."""
    retirement_plan: NotRequired[dict[str, Any]]
    """Complemento de planes personales de retiro (Planesderetiro 1.1), obligatorio con code 22: lo del año anterior."""
    mortgage_interest: NotRequired[dict[str, Any]]
    """Complemento de intereses reales deducibles por créditos hipotecarios (Intereseshipotecarios 1.0), obligatorio con code 23."""
    financial_derivatives: NotRequired[dict[str, Any]]
    """Complemento de operaciones financieras derivadas de capital (Operacionesconderivados 1.0), obligatorio con code 24."""
    platform: NotRequired[dict[str, Any]]
    """Complemento de servicios de plataformas tecnológicas (ServiciosPlataformasTecnologicas 1.0), obligatorio con code 26: una constancia por mes, receptor y tipo de servicio. totals y taxes se calculan de services con las tasas del SAT (ISR de LISR 113-A y LIF 2026 art. 25; IVA 50% o 100%; IEPS en apuestas); si los manda, deben coincidir."""
    cancellation: RetentionCancellation | None
    """La cancelación, si se pidió: estado, motivo, sustituto y cuándo."""
    email: RetentionEmail | None
    """El envío por correo: a quién, con copia a quién y cuándo (null si no se ha enviado)."""
    error: RetentionError | None
    """Por qué el SAT o el PAC no lo aceptaron: mensaje, código del SAT y texto original."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    metadata: dict[str, str]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""
    warnings: NotRequired[list[str]]
    """Avisos que no impidieron timbrar (por ejemplo, el XML se guardará después)."""
    email_error: NotRequired[str]
    """Por qué no se pudo mandar el correo; el comprobante sí se timbró."""


class CustomerForeign(TypedDict):
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str | None
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class Customer(TypedDict):
    """Un cliente del catálogo de un emisor."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["customer"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: str | None
    """Correo del cliente (varios separados por comas), a donde van sus facturas."""
    use: str | None
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    foreign: CustomerForeign | None
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: bool
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""
    group: str | None
    """Su grupo de clientes (cgr_…), o null si no está en ninguno."""
    price_list: str | None
    """Lista de precios (prl_…). En un cliente, la suya propia, que gana a la de su grupo; null para usar la de su grupo o la de todos."""
    discount_percent: float | None
    """Porcentaje de descuento sobre el precio, de 0 a 100; en el CFDI va como Descuento de cada concepto."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    updated_at: str | None
    """Cuándo cambió por última vez, ISO 8601 (-06:00)."""


class ProductLocalTaxesItem(TypedDict):
    retention: bool
    """true si es una retención local; false si es un traslado."""
    name: str
    """Nombre del impuesto local (ImpLocTrasladado o ImpLocRetenido), como ISH."""
    rate: float
    """Tasa en por ciento (TasadeTraslado o TasadeRetencion)."""


class Product(TypedDict):
    """Un producto o servicio del catálogo de un emisor."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["product"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    name: str | None
    """Nombre corto para encontrarlo, solo para usted."""
    description: str
    """Descripción que va en el CFDI (Descripcion)."""
    product_key: str
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: str
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: str | None
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: str | None
    """Número de identificación o SKU (NoIdentificacion)."""
    category: str | None
    """Su categoría, con las de arriba separadas por › («Ferretería › Tornillos»), o null si no tiene."""
    unit_price: float
    """Precio unitario antes de impuestos (ValorUnitario)."""
    open_price: bool
    """Precio abierto: el producto no tiene precio fijo y cada concepto con él manda su unit_price."""
    taxability: str
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: str
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: float | None
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: str | None
    """Tasa o Cuota (TipoFactor del IEPS)."""
    iva_retention: float
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: float
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""
    local_taxes: list[ProductLocalTaxesItem]
    """Impuestos locales (complemento implocal): traslados y retenciones estatales."""
    track_stock: bool
    """true si lleva existencias (Inventario)."""
    cost: float | None
    """Su costo por unidad en pesos sin IVA, o null."""
    barcode: str | None
    """Su código de barras, o null."""
    min_stock: float | None
    """Su existencia mínima, o null."""
    portal_visible: bool
    """true si se ofrece en el Portal del cliente para hacer pedidos."""
    min_order_qty: float | None
    """Lo mínimo que se pide de él en el Portal del cliente, o null sin mínimo."""
    order_step: float | None
    """De cuántos en cuántos se pide en el Portal del cliente (6 para pedir 6, 12, 18…), o null de uno en uno."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    updated_at: str | None
    """Cuándo cambió por última vez, ISO 8601 (-06:00)."""


class Employee(TypedDict):
    """Un empleado de un emisor, para sus recibos de nómina."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["employee"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    number: str
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre completo del empleado."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    curp: str
    """CURP, 18 caracteres."""
    social_security_number: str
    """Número de seguridad social (NumSeguridadSocial), 11 dígitos."""
    zip: str
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: str | None
    """Correo del empleado, a donde van sus recibos."""
    start_date: str
    """Fecha de inicio de la relación laboral (FechaInicioRelLaboral), AAAA-MM-DD."""
    end_date: str | None
    """Último día trabajado si ya no trabaja ahí, AAAA-MM-DD."""
    daily_salary: float
    """Salario diario."""
    integrated_daily_salary: float
    """Salario diario integrado (SalarioDiarioIntegrado): no menor al salario diario."""
    contract_type: str
    """Tipo de contrato (TipoContrato), c_TipoContrato. Por omisión 01, por tiempo indeterminado."""
    workday_type: str
    """Tipo de jornada (TipoJornada), c_TipoJornada. Por omisión 01, diurna."""
    regime_type: str
    """Tipo de régimen (TipoRegimen): 02 sueldos y salarios."""
    periodicity: str
    """Periodicidad del pago (PeriodicidadPago): 02 semanal, 03 catorcenal, 04 quincenal (por omisión), 05 mensual."""
    risk_class: str
    """Clase de riesgo del puesto ante el IMSS (RiesgoPuesto), 1 a 5. Por omisión 1."""
    state: str
    """Entidad federativa donde trabaja (ClaveEntFed): JAL, CMX, NLE…"""
    border_zone: bool
    """true si trabaja en la zona libre de la frontera norte (salario mínimo de frontera)."""
    unionized: bool
    """true si es sindicalizado (Sindicalizado)."""
    department: str | None
    """Departamento (Departamento)."""
    position: str | None
    """Puesto (Puesto)."""
    clabe: str | None
    """CLABE de su cuenta, a donde le paga el archivo para el banco, o null."""
    given_names: str | None
    """Nombre(s) como en su CURP, o null (los archivos del IMSS lo separan con la CURP)."""
    first_surname: str | None
    """Primer apellido como en su CURP, o null."""
    second_surname: str | None
    """Segundo apellido, o null."""
    imss_worker_type: str
    """Tipo de trabajador del IMSS: 1 permanente, 2 eventual de la ciudad, 3 eventual de la construcción, 4 eventual del campo."""
    imss_salary_type: str
    """Tipo de salario del IMSS: 0 fijo, 1 variable, 2 mixto."""
    imss_reduced_week: str
    """Semana o jornada reducida: 0 normal, 1 a 5 días a la semana, 6 jornada de menos de 8 horas."""
    family_medicine_unit: str | None
    """Unidad de medicina familiar del IMSS, o null."""
    exit_reason: str | None
    """Causa de la baja ante el IMSS cuando tiene end_date (2 separación voluntaria por omisión), o null."""
    warnings: list[str]
    """Lo que el SAT podría observar de sus datos, antes de timbrar."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""


class PayrollReceiptPreviewWarningsItem(TypedDict):
    code: str
    """finiquito_not_included: el empleado se fue en el periodo y el recibo no trae su finiquito; payroll_rates_pending: aún no se cargan los valores (ISR, subsidio, salario mínimo, UMA) de una fecha próxima."""
    message: str
    """Qué pasó y cómo corregirlo, para una persona."""


class PayrollReceiptPreviewPeriod(TypedDict):
    """El periodo de pago: primer y último día y el día de pago (FechaInicialPago, FechaFinalPago y FechaPago)."""
    start: str
    """Primer día del periodo (FechaInicialPago), AAAA-MM-DD."""
    end: str
    """Último día del periodo (FechaFinalPago), AAAA-MM-DD."""
    payment_date: str
    """Fecha de pago (FechaPago), AAAA-MM-DD. Por omisión el último día del periodo."""


class PayrollReceiptPreviewPerceptionsItemOvertimeItem(TypedDict):
    days: int
    """Días con horas extra (Dias)."""
    hours_type: str
    """c_TipoHoras: 01 dobles, 02 triples, 03 simples."""
    hours: int
    """Horas extra (HorasExtra)."""
    amount_paid: float
    """Importe pagado (ImportePagado)."""


class PayrollReceiptPreviewPerceptionsItemStockOptions(TypedDict):
    """Acciones o títulos (AccionesOTitulos), con la percepción 045."""
    market_value: float
    """Valor de mercado (ValorMercado)."""
    grant_price: float
    """Precio al otorgarse (PrecioAlOtorgarse)."""


class PayrollReceiptPreviewPerceptionsItem(TypedDict):
    type: str
    """Tipo de percepción (TipoPercepcion), c_TipoPercepcion: 001 sueldos…"""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    taxed: float
    """Importe gravado (ImporteGravado)."""
    exempt: float
    """Importe exento (ImporteExento)."""
    overtime: NotRequired[list[PayrollReceiptPreviewPerceptionsItemOvertimeItem]]
    """Horas extra (HorasExtra), con la percepción 019."""
    stock_options: NotRequired[PayrollReceiptPreviewPerceptionsItemStockOptions]
    """Acciones o títulos (AccionesOTitulos), con la percepción 045."""


class PayrollReceiptPreviewDeductionsItem(TypedDict):
    type: str
    """Tipo de deducción (TipoDeduccion), c_TipoDeduccion: 001 IMSS, 002 ISR…"""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    amount: float
    """Importe (Importe)."""


class PayrollReceiptPreviewOtherPaymentsItemBalanceCompensation(TypedDict):
    """Compensación del saldo a favor (CompensacionSaldosAFavor), con el 004."""
    balance: float
    """Saldo a favor (SaldoAFavor)."""
    year: int
    """Año del saldo a favor (Año)."""
    remaining: float
    """Remanente del saldo a favor (RemanenteSalFav)."""


class PayrollReceiptPreviewOtherPaymentsItem(TypedDict):
    type: str
    """Tipo de otro pago (TipoOtroPago), c_TipoOtroPago: 002 subsidio para el empleo."""
    key: str
    """Clave del patrón (Clave)."""
    concept: str
    """Concepto (Concepto)."""
    amount: float
    """Importe pagado (Importe)."""
    subsidy_caused: NotRequired[float]
    """Subsidio causado (SubsidioCausado)."""
    subsidy_applied: NotRequired[float]
    """Del subsidio causado, el ISR que evitó (no va en el XML)."""
    balance_compensation: NotRequired[PayrollReceiptPreviewOtherPaymentsItemBalanceCompensation]
    """Compensación del saldo a favor (CompensacionSaldosAFavor), con el 004."""


class PayrollReceiptPreviewIsrAdjustment(TypedDict):
    """El ajuste de fin de mes: subsidio revertido y el ISR que retiene."""
    reversed: float
    """El subsidio para el empleo que se revierte en el ajuste."""
    isr: float
    """El ISR que se retiene después del ajuste."""


class PayrollReceiptPreviewIsr(TypedDict):
    """El cálculo del ISR del periodo: base, tarifa, subsidio y resultado."""
    tariff: float
    """ISR según la tarifa del periodo."""
    subsidy: float
    """Subsidio para el empleo causado."""
    withheld: float
    """ISR retenido (tarifa menos subsidio, no menos de 0)."""
    exempt_minimum: bool
    """true si gana el salario mínimo: no se le retiene ISR."""
    adjustment: NotRequired[PayrollReceiptPreviewIsrAdjustment]
    """El ajuste de fin de mes: subsidio revertido y el ISR que retiene."""


class PayrollReceiptPreviewTotals(TypedDict):
    """Totales: percepciones, deducciones, otros pagos y el neto a pagar."""
    salaries: float
    """Total de sueldos, salarios y asimilados (TotalSueldos)."""
    taxed: float
    """Total gravado (TotalGravado)."""
    exempt: float
    """Total exento (TotalExento)."""
    separation: float
    """Total de separación e indemnización (TotalSeparacionIndemnizacion)."""
    retirement: float
    """Total de jubilación, pensión o retiro (TotalJubilacionPensionRetiro)."""
    perceptions: float
    """Total de percepciones (TotalPercepciones)."""
    other_deductions: float
    """Otras deducciones (TotalOtrasDeducciones)."""
    taxes_withheld: float
    """Impuestos retenidos (TotalImpuestosRetenidos)."""
    deductions: float
    """Total de deducciones (TotalDeducciones)."""
    other_payments: float
    """Total de otros pagos (TotalOtrosPagos)."""
    subtotal: float
    """Subtotal del comprobante: percepciones más otros pagos."""
    net: float
    """Neto a pagar al empleado."""


class PayrollReceiptPreview(TypedDict):
    """El recibo como se timbraría: percepciones, deducciones (ISR, IMSS), otros pagos (subsidio) y el neto."""
    object: Literal["payroll_receipt_preview"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    confirmation_token: str
    """Mándelo en POST /v1/payroll_receipts para timbrar exactamente este recibo: si al timbrar se calcula otro, contesta 409 payroll_calculation_changed sin timbrar."""
    warnings: list[PayrollReceiptPreviewWarningsItem]
    """Lo que el recibo no incluye o pronto no se podrá calcular; no impide timbrar."""
    employee: str
    """El empleado (emp_…)."""
    periodicity: str
    """Periodicidad del pago (PeriodicidadPago): 02 semanal, 03 catorcenal, 04 quincenal (por omisión), 05 mensual."""
    period: PayrollReceiptPreviewPeriod
    """El periodo de pago: primer y último día y el día de pago (FechaInicialPago, FechaFinalPago y FechaPago)."""
    days: float
    """Días pagados (NumDiasPagados). Por omisión, todos los del periodo que le tocan."""
    contribution_base_salary: float
    """Salario base de cotización (SalarioBaseCotApor)."""
    perceptions: list[PayrollReceiptPreviewPerceptionsItem]
    """Percepciones (Percepcion): sueldo y demás, gravado y exento."""
    deductions: list[PayrollReceiptPreviewDeductionsItem]
    """Deducciones (Deduccion): ISR, cuotas IMSS y demás."""
    other_payments: list[PayrollReceiptPreviewOtherPaymentsItem]
    """Otros pagos (OtroPago): subsidio para el empleo."""
    isr: PayrollReceiptPreviewIsr
    """El cálculo del ISR del periodo: base, tarifa, subsidio y resultado."""
    totals: PayrollReceiptPreviewTotals
    """Totales: percepciones, deducciones, otros pagos y el neto a pagar."""


class ExternalPayrollReceiptPreviewCustomer(TypedDict):
    """El empleado como receptor del CFDI (Receptor)."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    zip: str
    """Código postal del domicilio fiscal del cliente (DomicilioFiscalReceptor), 5 dígitos."""


class ExternalPayrollReceiptPreviewWarningsItem(TypedDict):
    param: str
    """El campo de la solicitud."""
    code: str
    """Clave de la retención (CveRetenc), c_CveRetenc: 01 servicios profesionales, 05 arrendamiento, 14 dividendos, 16 intereses, 18 pagos al extranjero… Las claves 14, 16, 17 y 18 a 24 llevan su complemento (dividends, interest, trust_lease, foreign_payment, share_sale, prize, trust, retirement_plan, mortgage_interest, financial_derivatives); la 26 (plataformas tecnológicas) lleva platform, y sus totals y taxes se calculan de las operaciones."""
    message: str
    """Qué pasó y cómo corregirlo, para una persona."""


class ExternalPayrollReceiptPreview(TypedDict):
    """Un recibo calculado por su sistema, revisado y sin timbrar: lo que se timbraría, tal cual."""
    object: Literal["payroll_receipt_preview"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    calculation: Literal["external"]
    """external: los importes son los que calculó su sistema."""
    issuer: str
    """El emisor (iss_…)."""
    customer: ExternalPayrollReceiptPreviewCustomer
    """El empleado como receptor del CFDI (Receptor)."""
    payroll: InvoicePayroll
    """El recibo de nómina 1.2: empleado, periodo, percepciones, deducciones y otros pagos."""
    subtotal: float
    """SubTotal: percepciones más otros pagos."""
    discount: float
    """Descuento: las deducciones."""
    total: float
    """Total: el neto a pagar."""
    warnings: list[ExternalPayrollReceiptPreviewWarningsItem]
    """Lo que el SAT podría observar; no impide timbrar."""
    unsigned_xml: str
    """El XML que se mandaría al PAC, sin sello ni timbre: sus importes son exactamente los que mandó."""


class AdvanceCustomer(TypedDict):
    """El cliente del anticipo: RFC y nombre."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class Advance(TypedDict):
    """Un anticipo timbrado que aún no se aplica."""
    object: Literal["advance"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    uuid: str
    """Folio fiscal que asigna el SAT (UUID del Timbre Fiscal Digital), en mayúsculas."""
    date: str
    """Fecha de emisión (Fecha), hora de la Ciudad de México."""
    series: str | None
    """La serie (Serie) del anticipo, o null."""
    folio: str | None
    """El folio (Folio) del anticipo, o null."""
    customer: AdvanceCustomer
    """El cliente del anticipo: RFC y nombre."""
    amount: float
    """El anticipo antes de impuestos."""
    total: float
    """Total en la moneda del comprobante (Total)."""
    iva: str
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    currency: str
    """Moneda, clave ISO 4217 de c_Moneda (MXN, USD, EUR…). Por omisión MXN."""


class InvoiceBatchInvoicesItem(TypedDict):
    index: int
    """Su posición en invoices, desde 0."""
    reference: str | None
    """Su identificador de esta factura (su número de pedido), hasta 100 caracteres."""
    status: Literal["processing", "valid", "failed"]
    """processing, valid (timbrada) o failed (no se timbró; ver error)."""
    invoice: str | None
    """La factura timbrada (inv_…)."""
    uuid: str | None
    """Folio fiscal que asigna el SAT (UUID del Timbre Fiscal Digital), en mayúsculas."""
    total: float
    """Total en la moneda del comprobante (Total)."""
    error: str | None
    """Por qué no se timbró."""


class InvoiceBatch(TypedDict):
    """Un lote de hasta 1,000 facturas timbradas en segundo plano."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["invoice_batch"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    name: str
    """Nombre del lote, para usted."""
    status: Literal["processing", "completed"]
    """processing: timbrando. completed: ya no queda ninguna por timbrar."""
    total: int
    """Cuántas facturas tiene el lote."""
    stamped: int
    """Cuántas se timbraron."""
    failed: int
    """Cuántas no se timbraron (quedan con su motivo)."""
    processing: NotRequired[int]
    """Cuántas siguen en proceso."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    completed_at: str | None
    """Cuándo terminó."""
    invoices: NotRequired[list[InvoiceBatchInvoicesItem]]
    """Cada factura del lote (no viene en listas ni en eventos)."""


class PayrollBatchReceiptsItemError(TypedDict):
    code: str
    """payroll_invalid, payroll_period_overlap, payroll_receipt_exists, invoice_rejected, invoice_invalid, insufficient_balance…"""
    message: str
    """Qué pasó y cómo corregirlo, para una persona."""


class PayrollBatchReceiptsItem(TypedDict):
    index: int
    """Su posición en receipts (o external_receipts), desde 0."""
    reference: str | None
    """Su identificador de esta factura (su número de pedido), hasta 100 caracteres."""
    employee: str | None
    """El empleado (emp_…), cuando Fiscalisto calculó el recibo."""
    tax_id: str
    """El RFC del empleado."""
    name: str | None
    """Nombre."""
    status: Literal["processing", "valid", "failed"]
    """Estado del objeto."""
    invoice: str | None
    """El recibo (inv_…, una factura tipo N); también el que el SAT rechazó."""
    uuid: str | None
    """Folio fiscal que asigna el SAT (UUID del Timbre Fiscal Digital), en mayúsculas."""
    total: float | None
    """El neto del recibo timbrado."""
    error: PayrollBatchReceiptsItemError | None
    """Por qué no se timbró este recibo: su código y su mensaje."""


class PayrollBatch(TypedDict):
    """Una nómina completa (hasta 1,000 recibos) timbrada en segundo plano."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["payroll_batch"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    name: str
    """Nombre del lote, para usted."""
    calculation: Literal["fiscalisto", "external"]
    """fiscalisto: Fiscalisto calculó cada recibo (receipts); external: se timbraron los importes de su sistema (external_receipts)."""
    status: Literal["processing", "completed"]
    """processing: timbrando. completed: ya no queda ningún recibo por timbrar."""
    total: int
    """Cuántos recibos tiene el lote."""
    stamped: int
    """Cuántos recibos se timbraron."""
    failed: int
    """Cuántos no se timbraron (cada uno con su error)."""
    processing: int
    """Cuántos faltan por timbrar."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    completed_at: str | None
    """Cuándo terminó."""
    receipts: NotRequired[list[PayrollBatchReceiptsItem]]
    """El recibo de cada empleado, en el orden en que los mandó (no viene en listas)."""


class PayrollBankFilePaymentsItem(TypedDict):
    employee: str | None
    """El empleado (emp_…); null si el recibo lo timbró otro sistema y no hay empleado con ese RFC."""
    number: str | None
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    amount: float
    """El neto a pagar: la suma de sus recibos con esa fecha de pago."""
    clabe: str
    """La CLABE a donde se paga."""
    spei: bool
    """true: a otro banco por SPEI; false: a una cuenta del mismo banco."""
    receipts: list[str]
    """Serie y folio de los recibos que paga."""


class PayrollBankFileExcludedItem(TypedDict):
    employee: str | None
    """El empleado (emp_…); null si el recibo lo timbró otro sistema y no hay empleado con ese RFC."""
    number: str | None
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    amount: float
    """El neto a pagar: la suma de sus recibos con esa fecha de pago."""
    reason: str
    """Por qué no va en el archivo."""


class PayrollBankFile(TypedDict):
    """El archivo para pagar la nómina desde el portal del banco (no cobra nada)."""
    object: Literal["payroll_bank_file"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor (iss_…)."""
    layout: Literal["bbva", "banamex", "banorte", "santander", "spei"]
    """El formato del banco: bbva, banamex, banorte, santander o spei (CSV)."""
    payment_date: str
    """Fecha de pago (FechaPago), AAAA-MM-DD. Por omisión el último día del periodo."""
    account: str | None
    """La CLABE de la cuenta de cargo."""
    file_name: str
    """El nombre con que el portal del banco lo espera."""
    content_type: Literal["text/plain", "text/csv"]
    """text/plain para los portales de los bancos, text/csv para spei."""
    content: str
    """El archivo como texto, con renglones terminados en CR LF."""
    content_base64: str
    """El mismo archivo en Windows-1252 (ANSI), en base64: guárdelo tal cual para subirlo."""
    total: float
    """Total en la moneda del comprobante (Total)."""
    count: int
    """Cuántos pagos lleva."""
    payments: list[PayrollBankFilePaymentsItem]
    """Cada pago del archivo, en el orden en que va."""
    excluded: list[PayrollBankFileExcludedItem]
    """Quién no va en el archivo y por qué (sin CLABE, otro banco…)."""


class ImssMovement(TypedDict):
    """Un movimiento afiliatorio del IMSS de un empleado: alta, modificación de salario, baja o reingreso."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["imss_movement"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    employee: str
    """El empleado (emp_…)."""
    employee_number: str
    """Su número de empleado."""
    employee_name: str
    """Su nombre completo."""
    social_security_number: str
    """Número de seguridad social (NumSeguridadSocial), 11 dígitos."""
    kind: Literal["alta", "reingreso", "modificacion", "baja"]
    """alta, reingreso, modificacion (de salario) o baja."""
    movement_type: Literal["08", "07", "02"]
    """El tipo de movimiento del IMSS: 08 alta o reingreso, 07 modificación, 02 baja."""
    date: str
    """Fecha de emisión (Fecha), hora de la Ciudad de México."""
    integrated_daily_salary: float | None
    """Salario diario integrado (SalarioDiarioIntegrado): no menor al salario diario."""
    exit_reason: str | None
    """En bajas, la causa (1 a 9 o A); null en los demás."""
    source: Literal["automatic", "manual"]
    """automatic: lo registró el alta o el cambio del empleado; manual: se agregó a mano."""
    status: Literal["pending", "reported"]
    """pending: falta presentarlo al IMSS; reported: ya se presentó (ya no cambia)."""
    reported_at: str | None
    """Cuándo se marcó como presentado, o null."""
    problems: list[str]
    """Lo que el IMSS rechazaría en su renglón (vacío: listo para el archivo)."""


class ImssFilesFilesItem(TypedDict):
    file_name: str
    """El nombre del archivo."""
    description: str
    """Qué lleva, en palabras."""
    count: int
    """Cuántos movimientos lleva."""
    content: str
    """El archivo como texto, renglones terminados en CR LF."""
    content_base64: str
    """El archivo en Windows-1252 (ANSI, como lo leen IDSE y SUA), en base64."""


class ImssFilesRefusedItem(TypedDict):
    movement: str
    """El movimiento (imv_…)."""
    employee_name: str
    """El nombre del empleado."""
    problems: list[str]
    """Lo que el IMSS rechazaría en su renglón."""


class ImssFiles(TypedDict):
    """Los archivos para presentar movimientos en IDSE o importarlos en SUA."""
    object: Literal["imss_files"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor (iss_…)."""
    format: Literal["idse", "sua"]
    """idse o sua."""
    files: list[ImssFilesFilesItem]
    """Los archivos: en IDSE uno por tipo de movimiento; en SUA ASEG.TXT y MOVT.TXT."""
    movements: list[str]
    """Los movimientos que van en los archivos."""
    refused: list[ImssFilesRefusedItem]
    """Los que se quedaron fuera y por qué (un NSS inválido…)."""


class SatCatalogEntry(TypedDict):
    """Una clave de un catálogo del SAT."""
    code: str
    """La clave en el catálogo del SAT."""
    description: str
    """Su descripción en el catálogo."""


class SatListCheckListsItem(TypedDict):
    list: Literal["69", "69b", "69b_bis"]
    """69b: art. 69-B (operaciones simuladas). 69b_bis: art. 69-B Bis (pérdidas fiscales). 69: art. 69 (no localizados, adeudos, cancelados)."""
    source: str
    """El archivo del SAT de donde viene (clave)."""
    source_name: str
    """El nombre del archivo del SAT, para mostrarlo."""
    situation: str | None
    """Su situación según el SAT: Presunto, Definitivo, Desvirtuado, Sentencia favorable; en el art. 69, el supuesto (null si el archivo no la trae)."""
    published_on: str | None
    """Fecha de publicación en el SAT o en el DOF (null si no la trae)."""
    details: dict[str, str] | None
    """Lo demás que publica el SAT para ese RFC (oficios, fechas, montos), tal cual; null si nada."""


class SatListCheck(TypedDict):
    """Si un RFC aparece en las listas del SAT (69-B, 69-B Bis y art. 69)."""
    object: Literal["sat_list_check"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    tax_id: str
    """El RFC revisado."""
    name: str | None
    """El nombre con que aparece en las listas del SAT (null si no aparece)."""
    listed: bool
    """true si el RFC aparece en alguna lista, aunque haya desvirtuado."""
    risk: Literal["high", "medium", "none", "unknown"]
    """high: 69-B o 69-B Bis como presunto o definitivo (el SAT dice que simula operaciones; sus facturas no se pueden deducir). medium: una lista del art. 69 (no localizado, créditos firmes o exigibles, cancelados, sentencias, CSD sin efectos). none: no aparece en ninguna, con todas las listas al día, o ya desvirtuó o tiene sentencia favorable. unknown: no aparece, pero alguna lista no se pudo actualizar (vea lists_unavailable): no lo dé por limpio."""
    verified: bool
    """true si todas las listas se leyeron con éxito en los últimos dos días. Con false, que no aparezca no significa que esté limpio."""
    lists: list[SatListCheckListsItem]
    """Cada lista en que aparece; vacía si no aparece en ninguna."""
    lists_updated_at: str | None
    """Cuándo se actualizaron las listas por última vez (cada día a las 00:00 de la Ciudad de México)."""
    lists_unavailable: list[str]
    """Las listas que no se pudieron confirmar (su última actualización falló, falta o tiene más de dos días). Vacía si todas están al día."""


class TaxIdValidationErrorsItem(TypedDict):
    param: str
    """El campo: tax_id, legal_name, tax_system, zip, use o cif_id."""
    code: str
    """Qué falló, para su código: tax_id_format, tax_id_date, legal_name_capital_regime, legal_name_mismatch, tax_system_person, tax_system_mismatch, zip_unknown, zip_mismatch, use_tax_system, cif_id_not_found…"""
    message: str
    """La explicación, para mostrarla a su usuario."""
    suggestion: str | None
    """El valor correcto cuando se sabe (el del SAT con cif_id, o el nombre sin régimen de capital); null si no."""


class TaxIdValidationWarningsItem(TypedDict):
    param: str
    """El campo."""
    code: str
    """tax_id_check_digit, legal_name_format, tax_id_listed_69b o tax_id_listed_69."""
    message: str
    """La explicación."""
    suggestion: str | None
    """El valor sugerido, o null."""


class TaxIdValidationSatRecord(TypedDict):
    legal_name: str | None
    """El nombre o razón social, como lo tiene el SAT."""
    zip: str | None
    """El código postal de su domicilio fiscal."""
    tax_systems: list[str]
    """Sus regímenes vigentes (c_RegimenFiscal)."""


class TaxIdValidation(TypedDict):
    """Si los datos fiscales de un cliente van a pasar el SAT."""
    object: Literal["tax_id_validation"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    tax_id: str
    """El RFC revisado."""
    kind: Literal["company", "person", "generic"]
    """company (persona moral, 12 caracteres), person (persona física, 13) o generic (XAXX010101000, XEXX010101000)."""
    valid: bool
    """true si no hay errores: con lo que mandó, el SAT no debería rechazar la factura por los datos del cliente."""
    checked_with_sat: bool
    """true si se comparó con el registro del SAT (mandó cif_id y el SAT contestó)."""
    errors: list[TaxIdValidationErrorsItem]
    """Lo que haría que el SAT rechace la factura. Cada uno con el campo (param), un código, la explicación y, si se puede, el valor correcto (suggestion)."""
    warnings: list[TaxIdValidationWarningsItem]
    """Lo que no impide timbrar pero conviene revisar: el dígito verificador, mayúsculas, si el RFC está en las listas del SAT."""
    sat_record: TaxIdValidationSatRecord | None
    """Lo que tiene el SAT en la constancia (con cif_id): nombre, código postal y regímenes vigentes. null sin cif_id."""
    sat_error: str | None
    """Si el SAT no contestó a tiempo (con cif_id): reintente en unos minutos. null si contestó o no se consultó."""
    sat_lists: SatListCheck | None
    """Si el RFC aparece en las listas del SAT. null con un RFC genérico o mal escrito."""


class CustomerDataRequestSubmission(TypedDict):
    tax_id: str
    """Su RFC."""
    legal_name: str
    """Su nombre o razón social, como en su constancia."""
    tax_system: str
    """Su régimen fiscal (c_RegimenFiscal)."""
    zip: str
    """El código postal de su domicilio fiscal."""
    use: str
    """El uso del CFDI que eligió (c_UsoCFDI)."""
    email: str | None
    """Su correo para recibir facturas, si lo dio."""
    source: Literal["constancia", "manual"]
    """constancia (leído de su constancia o del SAT con su idCIF) o manual (escrito)."""
    customer: str | None
    """El cliente (cus_…) en el catálogo del emisor: el nuevo, o el que ya existía con ese RFC."""
    applied: bool
    """true si quedó en el catálogo. false si el cliente ya existía con otros datos: aplíquelos con POST /v1/customers/{id} si son correctos."""
    submitted_at: str | None
    """Cuándo los mandó."""


class CustomerDataRequest(TypedDict):
    """Una liga para que un cliente dé sus datos fiscales."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["customer_data_request"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor que le va a facturar."""
    status: Literal["open", "completed", "expired", "canceled"]
    """open (la liga espera), completed (el cliente mandó sus datos), expired (venció) o canceled."""
    url: str | None
    """La liga para su cliente, en fiscalisto.com. null cuando ya no está abierta."""
    reference: str | None
    """Su id para este cliente o pedido."""
    description: str | None
    """Lo que el cliente ve arriba del formulario."""
    expires_at: str | None
    """Cuándo deja de servir la liga."""
    created_at: str | None
    """Cuándo se creó."""
    submission: CustomerDataRequestSubmission | None
    """Lo que mandó el cliente (el último envío: puede corregirlo en las 24 horas siguientes). null mientras no conteste."""


class TestDataReset(TypedDict):
    """Lo que se borró (y se creó) al reiniciar los datos de prueba."""
    object: Literal["test_data_reset"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: Literal[False]
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuers: int
    """Cuántos emisores de pruebas se vaciaron (archivados incluidos)."""
    deleted_rows: int
    """Cuántos registros se borraron: facturas, clientes, productos, lotes, ligas, descargas…"""
    deleted_events: int
    """Cuántos eventos de pruebas se borraron (con sus entregas)."""
    customers_created: int
    """Clientes de ejemplo creados (con seed)."""
    products_created: int
    """Productos de ejemplo creados (con seed)."""


class SandboxKey(TypedDict):
    """Solo al crearlo."""
    id: str
    """Id de la llave."""
    secret: str
    """La llave fk_test_… del entorno. Solo se ve esta vez: guárdela."""


class Sandbox(TypedDict):
    """Un entorno de prueba: el modo de pruebas propio de una persona, con su emisor, llaves, webhooks y eventos aparte."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["sandbox"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: Literal[False]
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    name: str
    """Nombre."""
    issuers: int
    """Emisores activos en el entorno."""
    issuer: NotRequired[Issuer | None]
    """El emisor de pruebas del SAT con que nace (solo al crearlo)."""
    key: NotRequired[SandboxKey]
    """Solo al crearlo."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    deleted: NotRequired[bool]
    """Siempre true."""


class TestClockAdvanced(TypedDict):
    """Al adelantarlo: lo que se hizo en el camino."""
    recurring_invoices: int
    """Facturas recurrentes timbradas en el camino."""
    quotes_expired: int
    """Cotizaciones que vencieron en el camino."""
    global_invoices: int
    """Facturas globales de tickets timbradas en el camino."""


class TestClock(TypedDict):
    """El reloj de prueba de un emisor de pruebas: su «hoy», que solo avanza cuando usted lo adelanta, haciendo día por día lo que toca."""
    id: str
    """clk_ y la clave del emisor."""
    object: Literal["test_clock"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: Literal[False]
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor de pruebas que vive en esta hora."""
    frozen_time: str
    """La hora del reloj: el «hoy» del emisor para sus facturas recurrentes, cotizaciones, cuentas por cobrar y tickets."""
    status: Literal["ready", "advancing"]
    """advancing mientras una solicitud lo adelanta; ready en cualquier otro momento."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    advanced: NotRequired[TestClockAdvanced]
    """Al adelantarlo: lo que se hizo en el camino."""
    stopped_early: NotRequired[bool]
    """true si se detuvo antes de requested_time porque ya timbró 25 comprobantes en esta solicitud: adelántelo otra vez para seguir."""
    requested_time: NotRequired[str]
    """A dónde se pidió adelantarlo (con stopped_early)."""
    deleted: NotRequired[bool]
    """Siempre true."""


# Una solicitud al SAT de las facturas emitidas o recibidas de un emisor en un periodo.
SatDownload = TypedDict(
    "SatDownload",
    {
        "id": "str",
        "livemode": "bool",
        "object": "Literal[\"sat_download\"]",
        "issuer": "str",
        "direction": "Literal[\"received\", \"issued\"]",
        "from": "str | None",
        "to": "str | None",
        "type": "Literal[\"I\", \"E\", \"P\", \"T\", \"N\"] | None",
        "counterparty_tax_id": "str | None",
        "uuid": "str | None",
        "status": "Literal[\"processing\", \"completed\", \"failed\"]",
        "new_invoices": "int | None",
        "error": "str | None",
        "created_at": "str | None",
        "completed_at": "str | None",
    },
)


class SatInvoiceIssuedBy(TypedDict):
    """Quien la emitió (Emisor)."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class SatInvoiceIssuedTo(TypedDict):
    """A quien se la emitieron (Receptor)."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class SatInvoiceTaxes(TypedDict):
    """Impuestos del comprobante: trasladados (iva, ieps), retenidos (iva_withheld, isr_withheld, ieps_withheld) y locales."""
    iva: float
    """IVA trasladado."""
    ieps: float
    """IEPS trasladado."""
    iva_withheld: float
    """IVA retenido."""
    isr_withheld: float
    """ISR retenido."""
    ieps_withheld: float
    """IEPS retenido."""
    local_transferred: float
    """Impuestos locales trasladados (ISH y similares)."""
    local_withheld: float
    """Impuestos locales retenidos."""


class SatInvoice(TypedDict):
    """Una factura que el SAT tiene del emisor, emitida o recibida, traída con una descarga."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["sat_invoice"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor de su cuenta (iss_…) a quien pertenece esta factura."""
    uuid: str
    """El folio fiscal (UUID del timbre)."""
    direction: Literal["received", "issued"]
    """received (se la hicieron al emisor) o issued (la emitió)."""
    type: Literal["I", "E", "P", "T", "N"] | None
    """Tipo de comprobante (TipoDeComprobante): I ingreso, E egreso, P pago, T traslado, N nómina."""
    date: str
    """La fecha del comprobante (Fecha), en la hora local con que se emitió."""
    series: str | None
    """Serie (Serie), o null."""
    folio: str | None
    """Folio (Folio), o null."""
    issued_by: SatInvoiceIssuedBy
    """Quien la emitió (Emisor)."""
    issued_to: SatInvoiceIssuedTo
    """A quien se la emitieron (Receptor)."""
    currency: str | None
    """Moneda (Moneda): MXN, USD…"""
    exchange_rate: float | None
    """Tipo de cambio (TipoCambio), o null en pesos."""
    payment_method: str | None
    """Método de pago (MetodoPago): PUE o PPD."""
    payment_form: str | None
    """Forma de pago (FormaPago), clave de c_FormaPago."""
    use: str | None
    """Uso del CFDI (UsoCFDI)."""
    subtotal: float | None
    """Subtotal (SubTotal)."""
    total: float | None
    """Total (Total)."""
    taxes: SatInvoiceTaxes
    """Impuestos del comprobante: trasladados (iva, ieps), retenidos (iva_withheld, isr_withheld, ieps_withheld) y locales."""
    sat_status: Literal["active", "canceled"] | None
    """Su estado en el SAT cuando se revisó: active (vigente) o canceled. null si aún no se revisa."""
    cost_center: str | None
    """Su centro de costo (ccn_…), o null. Póngalo o cámbielo con POST /v1/sat_invoices/{id}."""
    sat_download: str | None
    """La descarga (sdl_…) que la trajo, o null."""
    downloaded_at: str | None
    """Cuándo llegó."""


class SatRetentionIssuedBy(TypedDict):
    """Quien retuvo (Emisor)."""
    tax_id: str | None
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class SatRetentionIssuedTo(TypedDict):
    """A quien le retuvieron (Receptor)."""
    tax_id: str | None
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class SatRetentionPeriod(TypedDict):
    year: int
    """Ejercicio (Ejercicio)."""
    month_start: int
    """Mes inicial (MesIni), 1 a 12."""
    month_end: int
    """Mes final (MesFin), 1 a 12."""


class SatRetentionTotals(TypedDict):
    """Los montos de Totales."""
    operation: float | None
    """Monto total de la operación (MontoTotOperacion)."""
    taxed: float | None
    """Monto gravado (MontoTotGrav). Por omisión, operation menos exempt."""
    exempt: float | None
    """Monto exento (MontoTotExent). Por omisión 0."""
    withheld: float | None
    """Total retenido (MontoTotRet)."""


class SatRetentionWithheldTaxesItem(TypedDict):
    base: float | None
    """Base del impuesto retenido (BaseRet)."""
    tax: str | None
    """Impuesto: isr, iva o ieps (ImpuestoRet 001, 002, 003)."""
    amount: float | None
    """Importe."""
    payment_type: str | None
    """Tipo de pago de la retención (TipoPagoRet): 01 definitivo IVA, 02 definitivo IEPS, 03 definitivo ISR, 04 provisional ISR. Por omisión el usual de cada impuesto."""


class SatRetention(TypedDict):
    """Un CFDI de retenciones e información de pagos del emisor, recibido (la constancia que le dio un banco, una plataforma o quien le pagó) o emitido, como lo muestra Facturas › Retenciones."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["sat_retention"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor de su cuenta (iss_…) a quien pertenece esta constancia."""
    uuid: str
    """El folio fiscal (UUID del timbre)."""
    direction: Literal["received", "issued"]
    """received (se la dieron al emisor: un banco, una plataforma, quien le pagó) o issued (la emitió)."""
    date: str
    """La fecha de expedición (FechaExp)."""
    internal_folio: str | None
    """Folio interno (FolioInt), o null."""
    code: str | None
    """Clave de la retención (CveRetenc), como 14 dividendos, 16 intereses o 26 plataformas."""
    description: str | None
    """Descripción de la retención (DescRetenc), o null."""
    issued_by: SatRetentionIssuedBy
    """Quien retuvo (Emisor)."""
    issued_to: SatRetentionIssuedTo
    """A quien le retuvieron (Receptor)."""
    period: SatRetentionPeriod | None
    """Los meses y el ejercicio que cubre (Periodo), o null si no se pudo leer."""
    totals: SatRetentionTotals
    """Los montos de Totales."""
    withheld_taxes: list[SatRetentionWithheldTaxesItem]
    """Cada impuesto retenido (ImpRetenidos)."""
    status: Literal["active", "canceled"]
    """active o canceled: la canceló el emisor en Fiscalisto, o el SAT la reporta cancelada (se revisa cada mes). Una cancelada ya no es impuesto retenido."""
    read_error: str | None
    """Si su XML no se pudo leer, por qué; sus campos quedan en null. Si no, null."""
    downloaded_at: str | None
    """Cuándo llegó a Fiscalisto."""


class SatDeclarationSectionsItemFieldsItem(TypedDict):
    label: str
    """El renglón como lo imprime el SAT."""
    value: float | str
    """El valor del renglón como lo trae la declaración (número o texto)."""


class SatDeclarationSectionsItem(TypedDict):
    tax: str
    """Impuesto: isr, iva o ieps (ImpuestoRet 001, 002, 003)."""
    fields: list[SatDeclarationSectionsItemFieldsItem]
    """Los renglones del impuesto, en el orden del PDF."""


class SatDeclarationReceiptConceptsItem(TypedDict):
    concept: str
    """El concepto de la línea de captura (ISR, IVA…) como lo da el SAT."""
    due: float | None
    """Lo que resultó a cargo."""
    amount_due: float | None
    """La cantidad a cargo."""
    amount_to_pay: float | None
    """La cantidad a pagar."""


class SatDeclarationReceipt(TypedDict):
    concepts: list[SatDeclarationReceiptConceptsItem]
    """Cada impuesto del acuse."""
    total: float | None
    """Total en la moneda del comprobante (Total)."""
    payment_line: str | None
    """La línea de captura del acuse."""
    valid_until: str | None
    """Hasta cuándo sirve la línea de captura (AAAA-MM-DD)."""


class SatDeclarationSummaryObligationsItem(TypedDict):
    obligation: Literal["isr", "vat", "ieps", "isr_salaries", "isr_assimilated_salaries", "isr_professional_services", "isr_rent", "vat_withholdings", "other"]
    """Qué obligación es."""
    name: str
    """Su nombre como lo imprime el SAT."""
    read: bool
    """true si sus cifras se leyeron de la declaración; false si solo vienen del acuse."""
    amount_due: float | None
    """La cantidad a cargo."""
    amount_to_pay: float | None
    """La cantidad a pagar."""
    figures: dict[str, float | None]
    """Sus cifras con nombres fijos. ISR: income, invoiced_income, income_ytd, deductions, profit_coefficient, taxable_profit, losses_applied, tax_base, tax_caused, prior_payments, withheld. IVA: taxable_16, taxable_0, exempt, charged, paid_16, creditable, withheld, balance_applied. Salarios: workers, payments, exempt, withheld. Todas: surcharges, inflation, paid_before, due, in_favor, to_pay. null si no viene o no se pudo leer."""


class SatDeclarationSummary(TypedDict):
    """Las mismas cifras con nombres fijos, por obligación (ISR, IVA, cada retención), para leerlas igual cada mes sin conocer el formato del SAT. Una cifra que no viene en la declaración o no se pudo leer es null, nunca 0. En Declaraciones y pagos solo trae lo del acuse."""
    obligations: list[SatDeclarationSummaryObligationsItem]
    """Cada obligación de la declaración: isr, vat, ieps, isr_salaries, isr_assimilated_salaries, isr_professional_services, isr_rent, vat_withholdings u other."""
    total_to_pay: float | None
    """El total a pagar del acuse; si no hay acuse, la suma de las obligaciones cuando todas se conocen."""


class SatDeclarationFiles(TypedDict):
    """Qué archivos ya tiene: pdf (GET …/pdf), receipt (GET …/receipt) y financial_statements (GET …/financial_statements, solo en la anual de persona moral)."""
    pdf: bool
    """Si ya tiene la declaración en PDF (GET …/pdf)."""
    receipt: bool
    """Si ya tiene el acuse (GET …/receipt)."""
    financial_statements: bool
    """Si ya tiene el Excel de estados financieros (GET …/financial_statements), solo en la anual de persona moral."""


class SatDeclaration(TypedDict):
    """Una declaración que el emisor presentó ante el SAT (provisional o definitiva, anual o del servicio anterior Declaraciones y pagos), con sus cifras y sus archivos."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["sat_declaration"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor que la presentó."""
    source: Literal["monthly", "annual", "dyp"]
    """monthly (provisional o definitiva, desde 2022), annual (la anual de persona moral) o dyp (el servicio anterior Declaraciones y pagos, 2021 y antes)."""
    year: int
    """El ejercicio."""
    month: int | None
    """El mes (1 a 12), o null en la anual y otros periodos."""
    period: str
    """El periodo como lo nombra el SAT: «Enero», «Del Ejercicio»…"""
    type: Literal["normal", "complementary"]
    """normal o complementary (complementaria)."""
    complementary_type: str | None
    """El tipo de complementaria como lo dice el SAT («Modificación de obligaciones»…), o null."""
    operation_number: str
    """El número de operación que le dio el SAT."""
    payment_line: str | None
    """La línea de captura, si hubo algo a pagar."""
    filed_on: str | None
    """Cuándo se presentó (AAAA-MM-DD)."""
    profit_coefficient: float | None
    """El coeficiente de utilidad que aplicó (ISR de personas morales), o null."""
    isr_due: float | None
    """El ISR a cargo, según el acuse."""
    vat_due: float | None
    """El IVA a cargo, según el acuse."""
    total_due: float | None
    """El total a pagar, según el acuse."""
    sections: list[SatDeclarationSectionsItem]
    """Las cifras de la declaración por impuesto (tax), cada una con su texto como lo imprime el SAT (label) y su valor. Vacío en las de Declaraciones y pagos (su PDF trae dos columnas que no se leen con certeza) o si el PDF aún no llega."""
    receipt: SatDeclarationReceipt | None
    """Lo que dice el acuse: cada concepto con su cantidad a cargo y a pagar, el total, la línea de captura y su vigencia. null si el acuse aún no llega."""
    summary: SatDeclarationSummary
    """Las mismas cifras con nombres fijos, por obligación (ISR, IVA, cada retención), para leerlas igual cada mes sin conocer el formato del SAT. Una cifra que no viene en la declaración o no se pudo leer es null, nunca 0. En Declaraciones y pagos solo trae lo del acuse."""
    files: SatDeclarationFiles
    """Qué archivos ya tiene: pdf (GET …/pdf), receipt (GET …/receipt) y financial_statements (GET …/financial_statements, solo en la anual de persona moral)."""
    files_error: str | None
    """Por qué falta un archivo, como lo dijo el SAT (por ejemplo «No se puede generar el archivo»). Se vuelve a pedir en la siguiente consulta."""
    created_at: str | None
    """Cuándo se trajo por primera vez."""
    updated_at: str | None
    """Cuándo cambió por última vez."""


class SatDeclarationsRefresh(TypedDict):
    """Lo que trajo una consulta de las declaraciones del emisor en el SAT."""
    object: Literal["sat_declarations_refresh"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor consultado."""
    status: Literal["completed", "processing"]
    """completed (ya bajó todo) o processing (queda algo por bajar: sigue solo en la siguiente hora, sin otro timbre)."""
    found: int
    """Cuántas declaraciones listó el SAT en los años consultados."""
    downloaded: int
    """Cuántos archivos bajó en esta consulta."""
    pending: int
    """Cuántas declaraciones quedan con archivos por bajar."""
    warning: str | None
    """Si una parte del SAT falló (por ejemplo, la anual), lo que dijo; lo demás sí se trajo. null si todo salió."""
    refreshed_at: str
    """Cuándo se consultó."""
    next_refresh_at: str
    """Desde cuándo se puede volver a consultar este emisor (10 minutos después)."""


class SatDeclarationCalendarMonthsItemObligationsItem(TypedDict):
    obligation: Literal["isr", "vat", "ieps", "isr_salaries", "isr_assimilated_salaries", "isr_professional_services", "isr_rent", "vat_withholdings", "other"] | Literal["annual_return"]
    """Qué obligación es (las de summary.obligations), o annual_return para la anual."""
    status: Literal["filed", "missing", "due"]
    """filed (presentada), missing (venció y no la encontramos) o due (aún no vence)."""
    declarations: list[str]
    """Las declaraciones (dcl_…) que la presentaron, la normal y sus complementarias."""


class SatDeclarationCalendarMonthsItem(TypedDict):
    month: int | None
    """El mes (1 a 12), o null para la anual."""
    due_on: str
    """El último día para presentarla (AAAA-MM-DD)."""
    obligations: list[SatDeclarationCalendarMonthsItemObligationsItem]
    """Las obligaciones del mes."""


class SatDeclarationCalendar(TypedDict):
    """El ejercicio del emisor mes por mes: qué obligaciones presentó, cuáles parecen faltar y cuáles aún no vencen."""
    object: Literal["sat_declaration_calendar"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    year: int
    """El ejercicio."""
    missing: int
    """Cuántas obligaciones ya vencidas no encontramos presentadas en el SAT."""
    months: list[SatDeclarationCalendarMonthsItem]
    """Los 12 meses y, en persona moral, la anual (month null). Las obligaciones se deducen de lo que el emisor presenta: ISR e IVA cada mes desde el primero que presentó; una retención si la presentó en 2 de los 3 meses anteriores o antes y después. La opinión de cumplimiento del SAT es la que manda."""


class BranchAddress(TypedDict):
    """Su dirección, en el PDF de sus facturas."""
    street: str | None
    """Calle (Calle)."""
    exterior: str | None
    """Número exterior (NumeroExterior)."""
    interior: str | None
    """Número interior (NumeroInterior)."""
    neighborhood: str | None
    """Colonia."""
    city: str | None
    """Municipio o alcaldía."""
    state: str | None
    """Estado (Estado): en el extranjero c_Estado para USA y CAN, o texto."""


class BranchSeries(TypedDict):
    """La serie de cada tipo de CFDI que se timbra desde ella; null usa la del emisor."""
    invoice: str | None
    """Serie de sus facturas (tipo I); null, la del emisor."""
    credit_note: str | None
    """Serie de sus notas de crédito (tipo E); null, la del emisor."""
    payment: str | None
    """Serie de sus complementos de pago (tipo P); null, la del emisor."""
    transfer: str | None
    """Serie de sus traslados (tipo T); null, la del emisor."""


class Branch(TypedDict):
    """Una sucursal del emisor: otro lugar desde donde factura, con su código postal (LugarExpedicion), su dirección en el PDF, sus series y, si quiere, su propia marca (nombre comercial, logo, color y estilo del PDF)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["branch"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor de la sucursal."""
    name: str
    """Cómo la llama su equipo; va en el PDF."""
    zip: str
    """Su código postal: el LugarExpedicion de sus CFDI."""
    address: BranchAddress
    """Su dirección, en el PDF de sus facturas."""
    phone: str | None
    """Teléfono, en el PDF, o null."""
    email: str | None
    """Correo, en el PDF, o null."""
    series: BranchSeries
    """La serie de cada tipo de CFDI que se timbra desde ella; null usa la del emisor."""
    trade_name: str | None
    """Su nombre comercial propio (PDF, correo y página de la factura); null: el del emisor."""
    logo_url: str | None
    """Su logo propio, para el PDF (se sube en Ajustes › Sucursales); null: el del emisor."""
    pdf_color: str | None
    """Color de su PDF, como #2563EB; null: el del emisor."""
    pdf_style: Literal["clasico", "moderno", "compacto", "minimalista"] | None
    """Estilo de su PDF; null: el del emisor."""
    archived: bool
    """true si está archivada: ya no se factura desde ella."""
    created_at: str | None
    """Cuándo se creó."""
    updated_at: str | None
    """Cuándo cambió por última vez."""


class CostCenter(TypedDict):
    """Un centro de costo del emisor: una obra, proyecto, sucursal o área por la que separa sus ingresos y gastos."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["cost_center"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor del centro de costo."""
    name: str
    """Cómo lo llama su equipo, por ejemplo «Obra Norte»."""
    code: str | None
    """Su clave (por ejemplo «CC-01»), o null."""
    archived: bool
    """true si está archivado: ya no se ponen facturas en él, pero las suyas lo conservan."""
    invoices: int
    """Cuántas facturas tiene, emitidas y recibidas."""
    created_at: str | None
    """Cuándo se creó."""
    updated_at: str | None
    """Cuándo cambió por última vez."""


class PriceListItemsItem(TypedDict):
    product: str
    """Un producto de su catálogo (prd_…): toma su clave, unidad, precio e impuestos."""
    unit: str | None
    """Unidad aduana (UnidadAduana), c_UnidadAduana."""
    min_quantity: float
    """Desde cuántas unidades (de su presentación) vale este precio: un escalón de mayoreo. 1 por omisión."""
    unit_price: float | None
    """Precio unitario antes de impuestos (ValorUnitario)."""
    discount_percent: float | None
    """Porcentaje que baja el precio de la lista para este producto, en vez de un precio fijo."""


class PriceList(TypedDict):
    """Una lista de precios: parte del precio del catálogo (o de otra lista), lo mueve un porcentaje y lo redondea, con precios propios por producto, presentación y desde cierta cantidad (escalones de mayoreo). items solo viene al ver una lista."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["price_list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    name: str
    """Nombre."""
    description: str | None
    """Descripción."""
    base_list: str | None
    """La lista (prl_…) de la que parte; null parte del precio del catálogo de cada producto."""
    adjust_percent: float
    """Cuánto sube (positivo) o baja (negativo) el precio del que parte, en porcentaje."""
    round_to: float | None
    """A cuánto redondea los precios que calcula (0.5, 1, 10…), o null sin redondear."""
    starts_on: str | None
    """Desde qué día vale (YYYY-MM-DD, Ciudad de México), o null desde siempre."""
    ends_on: str | None
    """Hasta qué día vale, ese día incluido (YYYY-MM-DD), o null sin fin."""
    is_default: bool
    """true si es la lista de todos los clientes que no tienen otra (solo puede haber una)."""
    active: bool
    """false la pausa; true la reanuda desde hoy."""
    groups: int
    """Cuántos grupos de clientes la usan."""
    customers: int
    """Cuántos clientes la tienen como suya."""
    items: list[PriceListItemsItem] | None
    """Conceptos (Conceptos), al menos uno."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    updated_at: str | None
    """Cuándo cambió por última vez, ISO 8601 (-06:00)."""


class CustomerGroup(TypedDict):
    """Un grupo de clientes: su lista de precios, descuento, días de crédito, pedido mínimo y si piden desde su Portal del cliente."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["customer_group"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    name: str
    """Nombre."""
    color: str
    """Color de su etiqueta en la app: info, warning, positive, critical o muted."""
    price_list: str | None
    """Lista de precios (prl_…). En un cliente, la suya propia, que gana a la de su grupo; null para usar la de su grupo o la de todos."""
    discount_percent: float
    """Porcentaje de descuento sobre el precio, de 0 a 100; en el CFDI va como Descuento de cada concepto."""
    credit_days: int | None
    """Días de crédito que se le dan, de 0 a 365, o null para no cambiar los del cliente."""
    min_order: float | None
    """Pedido mínimo, sin IVA, para pedir desde el Portal del cliente, o null sin mínimo."""
    portal_ordering: bool
    """true si sus clientes pueden hacer pedidos desde su Portal del cliente."""
    customers: int
    """Cuántos clientes hay en el grupo."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""


class PriceQuoteItemsItemNextStep(TypedDict):
    min_quantity: float
    """Desde cuántas unidades (de su presentación) vale este precio: un escalón de mayoreo. 1 por omisión."""
    unit_price: float
    """Precio unitario antes de impuestos (ValorUnitario)."""


class PriceQuoteItemsItem(TypedDict):
    product: str
    """Un producto de su catálogo (prd_…): toma su clave, unidad, precio e impuestos."""
    quantity: float
    """Cantidad (Cantidad). Por omisión 1."""
    unit: str | None
    """Unidad aduana (UnidadAduana), c_UnidadAduana."""
    unit_price: float
    """Precio unitario antes de impuestos (ValorUnitario)."""
    catalog_price: float
    """Su precio del catálogo, por unidad y sin IVA, antes de su lista."""
    discount_percent: float
    """El descuento del cliente (el suyo, o el de su grupo) sobre ese precio; va como Descuento en el CFDI."""
    price_list: str | None
    """La lista (prl_…) de donde sale el precio, o null si es el del catálogo."""
    next_step: PriceQuoteItemsItemNextStep | None
    """El siguiente escalón de mayoreo: desde qué cantidad y a qué precio. null si no hay."""


class PriceQuote(TypedDict):
    """Lo que un cliente paga por unos productos a una cantidad: su precio por unidad sin IVA (de su lista), su descuento y el siguiente escalón de mayoreo."""
    object: Literal["price_quote"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    customer: str
    """El cliente (cus_…) cuyos precios se calcularon."""
    items: list[PriceQuoteItemsItem]
    """Conceptos (Conceptos), al menos uno."""


class ExpensePerson(TypedDict):
    """Alguien que viaja o gasta por el emisor: un empleado (de Nómina) o alguien por honorarios. Tiene un enlace propio para subir sus facturas sin cuenta."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["expense_person"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor por el que gasta."""
    kind: Literal["empleado", "honorarios"]
    """empleado (sueldos y salarios: viáticos exentos en su recibo de nómina) o honorarios."""
    employee: str | None
    """Su empleado de Nómina (emp_…), o null si es por honorarios."""
    name: str
    """Su nombre."""
    tax_id: str | None
    """Su RFC, o null."""
    email: str | None
    """Su correo, a donde se le manda su enlace y los avisos, o null."""
    base_city: str | None
    """Dónde trabaja: un viaje a más de 50 km de ahí es de viáticos."""
    department: str | None
    """Su área, o null."""
    link_active: bool
    """true si tiene un enlace que funciona para subir sus facturas."""
    archived: bool
    """true si está archivada."""
    created_at: str | None
    """Cuándo se agregó."""


class ExpensePersonLink(TypedDict):
    """El enlace de una persona: ahí ve solo sus comprobaciones y sube sus facturas desde el teléfono, sin cuenta."""
    object: Literal["expense_person_link"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    person: str
    """La persona (exp_…)."""
    url: str | None
    """Su enlace, o null si está apagado."""


class ExpenseItemIssuesItem(TypedDict):
    level: Literal["error", "warning", "policy", "info"]
    """error (impide enviarla), warning, policy (pasa la política) o info."""
    code: str
    """Qué es, como código estable."""
    message: str
    """Qué es, en palabras."""


class ExpenseItem(TypedDict):
    """Un gasto de una comprobación."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["expense_item"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    date: str
    """Cuándo se gastó (AAAA-MM-DD)."""
    category: Literal["hospedaje", "alimentos", "avion", "transporte", "auto", "combustible", "comidas", "papeleria", "mensajeria", "software", "otros"]
    """De qué es: hospedaje, alimentos, avion, transporte, auto, combustible, comidas, papeleria, mensajeria, software u otros."""
    description: str | None
    """Qué fue (el proveedor), o null."""
    amount: float
    """En pesos."""
    foreign_amount: float | None
    """En su moneda, o null."""
    foreign_currency: str | None
    """Su moneda (USD, EUR…), o null."""
    people: int
    """Cuántas personas comieron (en alimentos el tope es por persona)."""
    payment: Literal["tarjeta_empresa", "tarjeta_propia", "efectivo", "transferencia", "otro"] | None
    """Cómo se pagó: tarjeta_empresa, tarjeta_propia, efectivo, transferencia u otro, o null."""
    receipt: Literal["cfdi", "extranjero", "ticket", "ninguno"]
    """Su comprobante: cfdi, extranjero, ticket o ninguno."""
    uuid: str | None
    """El UUID de su factura, o null."""
    note: str | None
    """La nota de la persona, o null."""
    rejected: bool
    """true si quien aprueba lo rechazó."""
    reject_reason: str | None
    """Por qué se rechazó, o null."""
    deductible: float
    """Lo que se deduce de este gasto."""
    non_deductible: float
    """Lo que no se deduce."""
    over_policy: bool
    """true si pasa un tope de la política."""
    issues: list[ExpenseItemIssuesItem]
    """Sus avisos contra la ley y la política."""
    created_at: str | None
    """Cuándo se agregó."""


class ExpenseMovement(TypedDict):
    """Dinero que se le dio a la persona (anticipo, reembolso) o que devolvió."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["expense_movement"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    kind: Literal["anticipo", "reembolso", "devolucion"]
    """anticipo, reembolso o devolucion."""
    amount: float
    """En pesos."""
    date: str
    """Cuándo se pagó (AAAA-MM-DD)."""
    method: Literal["transferencia", "efectivo", "tarjeta", "nomina"]
    """transferencia, efectivo, tarjeta o nomina (en su recibo de nómina)."""
    reference: str | None
    """Su referencia, o null."""
    in_payroll: bool
    """true si ya se pagó en un recibo de nómina."""
    created_at: str | None
    """Cuándo se registró."""


class ExpenseReportIssuesItem(TypedDict):
    level: Literal["error", "warning", "policy", "info"]
    """error (impide enviarla), warning, policy (pasa la política) o info."""
    code: str
    """Qué es, como código estable."""
    message: str
    """Qué es, en palabras."""


class ExpenseReportPayroll(TypedDict):
    exempt: float
    """Viáticos exentos comprobados (OtroPago/Percepción 050, ImporteExento)."""
    taxed: float
    """Lo que grava como sueldo (050, ImporteGravado): lo gastado sin comprobar."""
    adjustment: float
    """Lo que se descuenta (deducción 081) por lo que ya se le dio y sobró."""
    net: float
    """Lo que neto cobra o paga en el recibo por esta comprobación."""


class ExpenseReport(TypedDict):
    """Una comprobación de viáticos (un viaje) o de gastos de un periodo: sus gastos revisados contra la ley y la política, y el dinero dado o devuelto. Al aprobarla sus facturas se deducen y entra en las pólizas por 107.01."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["expense_report"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor."""
    number: int
    """Su número, consecutivo por emisor."""
    label: str
    """Cómo se muestra, por ejemplo «VIA-0012»."""
    person: str
    """Quién la comprueba (exp_…)."""
    person_name: str
    """El nombre de esa persona."""
    kind: Literal["viaje", "gastos"]
    """viaje o gastos (de oficina, de un periodo)."""
    title: str
    """Su nombre."""
    purpose: str | None
    """Para qué fue, o null."""
    destination: str | None
    """A dónde, o null."""
    abroad: bool
    """true si fue al extranjero."""
    far: bool
    """true si fue a más de 50 km de donde trabaja la persona."""
    start_date: str | None
    """La salida o el inicio del periodo (AAAA-MM-DD), o null."""
    end_date: str | None
    """El regreso o el fin del periodo (AAAA-MM-DD), o null."""
    status: Literal["draft", "submitted", "rejected", "approved", "closed"]
    """draft (abierta), submitted (por aprobar), rejected (devuelta para corregir), approved (por liquidar) o closed (cerrada, con el saldo en cero)."""
    due_date: str | None
    """Hasta cuándo hay para comprobarla (la política), o null."""
    submitted_at: str | None
    """Cuándo se envió a aprobar, o null."""
    decided_at: str | None
    """Cuándo se aprobó o se devolvió, o null."""
    decision_note: str | None
    """La nota de quien la aprobó o la devolvió, o null."""
    closed_at: str | None
    """Cuándo se cerró, o null."""
    in_payroll: bool
    """true si ya se reportó en un recibo de nómina (viáticos 050 y 081)."""
    spent: float
    """Lo gastado, sin los gastos rechazados."""
    rejected: float
    """Lo de los gastos rechazados."""
    proven: float
    """Lo comprobado con factura o comprobante del extranjero."""
    deductible: float
    """Lo que se deduce, con los topes de la ley."""
    non_deductible: float
    """Lo que no se deduce (pasa los topes o no tiene comprobante)."""
    advances: float
    """Lo que se le dio en anticipos."""
    reimbursed: float
    """Lo que se le reembolsó."""
    returned: float
    """Lo que devolvió."""
    balance: float
    """Positivo, lo que la persona debe devolver; negativo, lo que la empresa le debe reembolsar; 0, liquidada. Lo pagado con la tarjeta de la empresa no cuenta."""
    ready: bool
    """true si se puede enviar o aprobar: ningún gasto tiene errores."""
    issues: list[ExpenseReportIssuesItem]
    """Avisos de la comprobación entera."""
    payroll: ExpenseReportPayroll | None
    """Para un empleado, cómo irá en su recibo de nómina (o null)."""
    items: list[ExpenseItem]
    """Sus gastos."""
    movements: list[ExpenseMovement]
    """El dinero que se le dio o devolvió."""
    created_at: str | None
    """Cuándo se abrió."""
    updated_at: str | None
    """Cuándo cambió por última vez."""


class ExpensePolicyLimitsValue(TypedDict):
    domestic: float | None
    abroad: float | None
    per: Literal["dia", "gasto"]


class ExpensePolicy(TypedDict):
    """La política de viáticos y gastos del emisor: topes por categoría, hasta cuánto sin factura y en cuántos días se comprueba."""
    object: Literal["expense_policy"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    limits: dict[str, ExpensePolicyLimitsValue]
    """Topes por categoría (hospedaje, alimentos…): las que no están no tienen tope."""
    ticket_limit: float
    """Hasta cuánto se acepta un gasto sin factura; 0: todos la piden."""
    due_days: int
    """Días después del regreso para comprobar."""
    note_over_limit: bool
    """true si pide una nota en cada gasto que pase un tope."""
    notify_approvers: bool
    """true si avisa por correo a quien aprueba."""
    notify_people: bool
    """true si avisa a la persona cuando se aprueba, se devuelve o se le paga."""


class Warehouse(TypedDict):
    """Un almacén del emisor: el de la Matriz y uno por sucursal se crean solos; cada factura saca existencias del de su sucursal."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["warehouse"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor del almacén."""
    name: str
    """Su nombre («Matriz», el de su sucursal, o el que le dieron en la app)."""
    code: str | None
    """Su clave corta, o null."""
    type: Literal["warehouse", "consignment"]
    """warehouse (almacén propio) o consignment (mercancía en consignación con un cliente, todavía suya)."""
    branch: str | None
    """Su sucursal (brn_…), o null si es de la Matriz."""
    default: bool
    """true si es el almacén del que vende y recibe su sucursal."""
    archived: bool
    """true si está archivado."""
    created_at: str | None
    """Cuándo se creó."""


class StockLevel(TypedDict):
    """Lo que hay de un producto en un almacén, y lo que vale."""
    id: str
    """Su id (stl_…): el producto en ese almacén. Sirve como starting_after."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["stock_level"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    product: str
    """El producto (prd_…)."""
    warehouse: str
    """El almacén (whs_…)."""
    on_hand: float
    """Lo que hay, en la unidad del producto (todos sus lotes)."""
    reserved: float
    """Lo apartado por cotizaciones aceptadas que no se han facturado."""
    available: float
    """on_hand menos reserved: lo que se puede vender."""
    value: float
    """Lo que valen esas existencias a su costo, en pesos sin IVA."""
    average_cost: float | None
    """value / on_hand: el costo por unidad, o null sin existencias."""


class StockMovementSource(TypedDict):
    """Lo que lo causó: type invoice (id es el UUID del CFDI), adjustment (adj_…), receipt, transfer, count o ticket."""
    type: str
    """Qué lo movió: invoice (una factura; id es su UUID), adjustment (un ajuste, adj_…), count (un conteo) u otro origen."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""


class StockMovement(TypedDict):
    """Una entrada o salida de existencias (el kárdex): una venta, una compra, un ajuste, un traspaso…"""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["stock_movement"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor."""
    product: str
    """El producto (prd_…)."""
    warehouse: str
    """El almacén (whs_…)."""
    type: Literal["sale", "purchase", "customer_return", "supplier_return", "adjustment", "count", "transfer_out", "transfer_in", "initial", "cost", "reversal"]
    """sale (una factura), purchase (una compra), customer_return, supplier_return, adjustment, count (conteo físico), transfer_out, transfer_in, initial, cost (un ajuste de costo) o reversal (deshace otro, como una factura cancelada)."""
    quantity: float
    """Cuánto entró (positivo) o salió (negativo)."""
    unit_cost: float
    """El costo por unidad con que entró o salió, en pesos sin IVA."""
    value: float
    """quantity × unit_cost: lo que cambió el valor del inventario."""
    lot: str | None
    """El lote o número de serie, o null."""
    source: StockMovementSource
    """Lo que lo causó: type invoice (id es el UUID del CFDI), adjustment (adj_…), receipt, transfer, count o ticket."""
    reason: str | None
    """El motivo de un ajuste, o null."""
    date: str | None
    """Cuándo pasó, hora de la Ciudad de México (la Fecha del CFDI en una venta)."""
    reversed: bool
    """true si un movimiento posterior lo deshizo."""
    created_at: str | None
    """Cuándo se registró."""


class StockAdjustmentLinesItem(TypedDict):
    product: str
    """Un producto de su catálogo (prd_…): toma su clave, unidad, precio e impuestos."""
    quantity: float
    """Cantidad (Cantidad). Por omisión 1."""
    unit_cost: float | None
    """El costo por unidad que se dio al ajuste, en pesos sin IVA, o null (el costo promedio)."""
    lot: str | None
    """Lote del medicamento (LoteMedicamento)."""


class StockAdjustment(TypedDict):
    """Un ajuste de existencias: lo que entró o salió de un almacén por inventario inicial, merma, robo, conteo…"""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["stock_adjustment"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor."""
    warehouse: str
    """El almacén (whs_…)."""
    reason: Literal["shrinkage", "theft", "damage", "expiration", "internal_use", "gift", "initial", "surplus", "count", "other"]
    """El motivo (ver POST /v1/stock_adjustments)."""
    note: str | None
    """Su nota, o null."""
    status: Literal["applied", "pending", "rejected", "reversed"]
    """applied (ya movió existencias), pending (espera aprobación en la app), rejected o reversed (se deshizo)."""
    value: float
    """Lo que vale lo que movió, en pesos sin IVA."""
    lines: list[StockAdjustmentLinesItem]
    """Lo que entró o salió de cada producto."""
    created_at: str | None
    """Cuándo se hizo."""


class ComplianceOpinion(TypedDict):
    """La opinión de cumplimiento de obligaciones fiscales (32-D) más reciente del emisor, como la dio el SAT."""
    object: Literal["compliance_opinion"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    result: Literal["positive", "negative", "no_obligations", "suspended"] | None
    """positive, negative, no_obligations (inscrito sin obligaciones) o suspended (en suspensión de actividades); null si no se ha consultado."""
    date: str | None
    """El día que la emitió el SAT (AAAA-MM-DD), o null."""
    folio: str | None
    """Su folio, o null."""
    reasons: list[str]
    """Si es negativa, lo que el SAT marca como pendiente."""
    pdf: bool
    """true si su PDF está en GET /v1/issuers/{id}/compliance_opinion/pdf."""
    checked_at: str | None
    """Cuándo se consultó por última vez, o null."""
    last_error: str | None
    """Por qué falló la última consulta, o null."""


class TaxStatusCertificateTaxSystemsItem(TypedDict):
    code: str
    """Clave del régimen fiscal (c_RegimenFiscal): 601, 612, 626…"""
    name: str
    """Nombre del régimen fiscal, como lo escribe el SAT."""


class TaxStatusCertificate(TypedDict):
    """La constancia de situación fiscal más reciente del emisor, generada en el SAT con su e.firma."""
    object: Literal["tax_status_certificate"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    issued_on: str | None
    """El día que la emitió el SAT (AAAA-MM-DD), o null."""
    id_cif: str | None
    """Su idCIF, o null."""
    tax_id: str
    """El RFC."""
    legal_name: str | None
    """Nombre o razón social como la tiene el SAT, o null."""
    tax_systems: list[TaxStatusCertificateTaxSystemsItem]
    """Sus regímenes fiscales (clave de c_RegimenFiscal y nombre)."""
    zip: str | None
    """El código postal de su domicilio fiscal, o null."""
    status: str | None
    """Estatus en el padrón (ACTIVO, SUSPENDIDO…), o null."""
    pdf: bool
    """true si su PDF está en GET /v1/issuers/{id}/tax_status_certificate/pdf."""
    created_at: str | None
    """Cuándo se generó."""


class SatMailboxMessage(TypedDict):
    """Un aviso del buzón tributario del SAT del emisor."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["sat_mailbox_message"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor."""
    subject: str
    """Su asunto."""
    summary: str | None
    """Su texto, resumido, o null."""
    source: Literal["mailbox", "email"]
    """mailbox (el buzón del portal) o email (un aviso que el SAT mandó por correo)."""
    unread: bool
    """true si no se ha leído en el SAT."""
    urgency: Literal["urgent", "attention", "informational"]
    """urgent (un requerimiento, un plazo), attention o informational."""
    kind: str
    """Qué es: requerimiento, carta invitación, informativo…"""
    action_required: bool
    """true si pide hacer algo."""
    received_at: str | None
    """Cuándo llegó, como lo dice el SAT."""
    created_at: str | None
    """Cuándo lo trajo Fiscalisto."""


class SatRefresh(TypedDict):
    """Una consulta al SAT de un documento del emisor: si ya terminó y dónde leerlo."""
    object: Literal["sat_refresh"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    document: Literal["compliance_opinion", "tax_status_certificate", "sat_mailbox"]
    """Qué se consultó."""
    status: Literal["completed", "processing"]
    """completed (ya está en url) o processing (el SAT tarda; llega a url en unos minutos)."""
    refreshed_at: str | None
    """Cuándo se pidió."""
    next_refresh_at: str | None
    """Desde cuándo se puede pedir otra vez."""
    url: str
    """Dónde leer lo que trajo."""


class SatFinding(TypedDict):
    """Un tipo de hallazgo en los CFDI del emisor (un proveedor en la lista 69-B, un CFDI cancelado, un pago en efectivo de más de $2,000…), con cuántos CFDI lo tienen."""
    id: str
    """El código del hallazgo (el mismo que code)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["sat_finding"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor."""
    code: str
    """El código del hallazgo, estable (por ejemplo efos_definitivo)."""
    severity: Literal["critical", "warning", "info"]
    """critical (grave), warning (revisar) o info."""
    title: str
    """Qué es, en palabras."""
    explanation: str | None
    """Por qué importa y qué hacer, o null."""
    invoices: int
    """Cuántos CFDI lo tienen, sin revisar."""
    counterparties: int
    """De cuántos proveedores o clientes son esos CFDI."""
    amount: float
    """La suma de sus totales, en pesos (los de otra moneda, a su tipo de cambio)."""
    last_date: str | None
    """La fecha del CFDI más reciente que lo tiene (AAAA-MM-DD)."""


class SatFindingCounterpartyFindingsItem(TypedDict):
    code: str
    """El código del hallazgo (el code de GET /v1/sat_findings)."""
    severity: Literal["critical", "warning", "info"]
    """critical (grave), warning (revisar) o info."""
    title: str
    """Qué es, en palabras."""
    invoices: int
    """En cuántos de sus CFDI está, sin revisar."""


class SatFindingCounterparty(TypedDict):
    """Un proveedor o cliente con hallazgos sin revisar en los CFDI del emisor: cuántos CFDI, cuánto suman y qué tipos de hallazgo tiene."""
    id: str
    """Su RFC (el mismo que rfc). Sirve como starting_after."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["sat_finding_counterparty"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor."""
    rfc: str
    """El RFC del proveedor (en recibidos) o del cliente (en emitidos)."""
    name: str | None
    """Su nombre como viene en el CFDI, o null."""
    severity: Literal["critical", "warning", "info"]
    """Su hallazgo más grave: critical, warning o info."""
    invoices: int
    """Cuántos de sus CFDI tienen algún hallazgo sin revisar."""
    amount: float
    """La suma de los totales de esos CFDI, en pesos, cada uno una vez aunque tenga varios hallazgos."""
    last_date: str | None
    """La fecha del más reciente de esos CFDI (AAAA-MM-DD)."""
    findings: list[SatFindingCounterpartyFindingsItem]
    """Sus tipos de hallazgo, del más grave al más leve."""


class TicketLinesItem(TypedDict):
    product: str | None
    """Un producto de su catálogo (prd_…): toma su clave, unidad, precio e impuestos."""
    description: str
    """Descripción."""
    product_key: str
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: str
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    iva: str | None
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    quantity: float
    """Cantidad (Cantidad). Por omisión 1."""
    total: float
    """Total en la moneda del comprobante (Total)."""


class TicketCustomer(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class TicketBuyer(TypedDict):
    name: str | None
    """Nombre."""
    email: str | None
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""


class Ticket(TypedDict):
    """Una venta que su comprador puede facturar él mismo en el portal del emisor (autofactura)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["ticket"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor que vendió."""
    folio: str
    """El folio de la venta en su sistema."""
    code: str
    """Lo que su comprador escribe en el portal junto con el total: el folio y 4 caracteres al azar (A123-K7QX). Imprímalo en el ticket o mándelo con la compra."""
    status: Literal["pending", "invoiced", "global", "cancelled"]
    """pending (se puede facturar), invoiced (su comprador lo facturó: la factura en invoice), global (entró en la factura global del periodo) o cancelled."""
    url: str | None
    """La página del portal con el código (c) y el total (t) del ticket: el portal lo encuentra solo y el comprador solo da sus datos. Quien tenga la liga puede facturar el ticket: désela solo al comprador (como el ticket impreso). Puede incrustarla con fiscalisto.js. null si ya no está pendiente."""
    total: float
    """Lo que se cobró, impuestos incluidos y sin propina."""
    tip: float
    """La propina (no va en la factura)."""
    payment_form: str
    """c_FormaPago de la venta."""
    description: str
    """El concepto de la factura (el primero, si lleva varios)."""
    product_key: str
    """c_ClaveProdServ del concepto (el primero, si lleva varios)."""
    lines: list[TicketLinesItem]
    """Sus conceptos, en orden: uno solo si se registró sin lines. Cada uno con su producto (prd_… o null), descripción, claves del SAT, IVA (null si no es objeto de impuesto), unidades y lo que se cobró por él, impuestos incluidos."""
    sold_at: str
    """Cuándo se vendió."""
    invoiceable_until: str
    """El último día (AAAA-MM-DD) en que el comprador puede facturarlo; después entra en la factura global."""
    invoice: str | None
    """La factura (inv_…) que hizo su comprador, o null."""
    global_invoice: str | None
    """La factura global (inv_…) en que entró, o null."""
    customer: TicketCustomer | None
    """A quién se facturó, o null."""
    buyer: TicketBuyer | None
    """Quién pagó, como lo conoce el origen de la venta (el `buyer` que mandó, o el cliente de un pago de Stripe). No es el receptor de la factura (`customer`)."""
    created_at: str | None
    """Cuándo se registró."""


class SelfInvoicing(TypedDict):
    """El portal de autofactura de un emisor y sus reglas."""
    object: Literal["self_invoicing"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    portal_url: str
    """El portal permanente del emisor: ahí cualquier comprador factura con su código y su total."""
    window: Literal["month", "days"]
    """month: se factura hasta el fin del mes de la venta. days: hasta window_days días después."""
    window_days: int
    """Días para facturar con window: days."""
    global_periodicity: Literal["01", "02", "03", "04"]
    """Cada cuánto se timbra sola la factura global con lo que nadie facturó: 01 diaria, 02 semanal, 03 quincenal, 04 mensual."""
    global_invoice: Literal["auto", "off"]
    """auto: los tickets que nadie facturó van solos a la factura global de su periodo. off: Fiscalisto no hace factura global de estos tickets (la hace usted en otro lado)."""
    ask_total: bool
    """Si el portal pide el total para encontrar el ticket (true) o solo su código (false)."""
    portal_title: str | None
    """El título del portal, o null para «Facture su ticket»."""
    portal_message: str | None
    """El mensaje bajo el título, o null."""
    code_hint: str | None
    """Dónde encuentra el comprador su código, bajo el campo; null para el texto de Fiscalisto."""
    portal_theme: Literal["auto", "light", "dark"]
    """auto: el tema del dispositivo del comprador, que puede cambiarlo. light o dark: siempre ese, en la página del portal, sus QR y dentro de su sitio."""
    portal_accent: str | None
    """El color de los botones del portal («#rrggbb»), o null para el de Fiscalisto."""
    portal_radius: int | None
    """Las esquinas del portal en píxeles (0 a 24), o null para las de Fiscalisto."""


class RecurringInvoiceSchedule(TypedDict):
    """Cada cuánto: frequency (monthly, weekly o daily), interval, day_of_month (con monthly; "last" es el último del mes), y la hora (hour, en time_zone) en que se timbra."""
    frequency: Literal["monthly", "weekly", "daily"]
    """monthly: cada interval meses en day_of_month. weekly o daily: cada interval semanas o días."""
    interval: int
    """Cada cuántos meses, semanas o días."""
    day_of_month: int | Literal["last"] | None
    """Con monthly: el día del mes, del 1 al 28, o "last" (el último). null con weekly o daily."""
    hour: int
    """La hora (0 a 23) en que se timbra, en time_zone."""
    time_zone: str
    """La zona de esa hora (America/Mexico_City, America/Cancun…)."""


class RecurringInvoiceLastError(TypedDict):
    message: str | None
    """Qué pasó."""


class RecurringInvoiceCustomer(TypedDict):
    """A quién se factura."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class RecurringInvoiceItemsItem(TypedDict):
    description: str
    """Descripción del concepto (Descripcion), hasta 1,000 caracteres."""
    product_key: str
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    quantity: NotRequired[float]
    """Cantidad (Cantidad). Por omisión 1."""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_price: float
    """Precio unitario antes de impuestos (ValorUnitario)."""


class RecurringInvoice(TypedDict):
    """Una factura que el emisor timbra solo, cada mes, semana o día."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["recurring_invoice"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    name: str
    """Para reconocerla."""
    status: Literal["active", "paused"]
    """active (timbra en cada fecha) o paused."""
    schedule: RecurringInvoiceSchedule
    """Cada cuánto: frequency (monthly, weekly o daily), interval, day_of_month (con monthly; "last" es el último del mes), y la hora (hour, en time_zone) en que se timbra."""
    next_invoice_on: str
    """La fecha (AAAA-MM-DD) de la siguiente factura."""
    last_invoiced_on: str | None
    """La fecha del último periodo que timbró, o null si aún no timbra ninguna."""
    last_invoice: str | None
    """La última factura (inv_…) que timbró, o null."""
    last_error: RecurringInvoiceLastError | None
    """Por qué no se pudo timbrar la última vez (sin timbres, el cliente borrado, el SAT la rechazó…), o null. Se vuelve a intentar a la siguiente hora del día siguiente; también llega recurring_invoice.failed."""
    send_email: bool
    """Si cada factura se manda al correo del cliente."""
    catch_up: Literal["all", "latest"]
    """Si quedaron periodos sin timbrar: all los timbra todos, latest solo el más reciente."""
    customer: RecurringInvoiceCustomer
    """A quién se factura."""
    currency: str
    """La moneda de la factura."""
    items: list[RecurringInvoiceItemsItem]
    """Los conceptos, con description tal como se guardó ({mes}, {año}… se llenan en cada factura)."""
    total: float | None
    """El total de cada factura con los precios de hoy."""
    created_at: str | None
    """Cuándo se creó."""


class JournalEntryLinesItem(TypedDict):
    account: str
    """El número de cuenta."""
    account_name: str
    """El nombre de la cuenta."""
    grouping_code: str
    """Su código agrupador del SAT."""
    debit: float
    """El cargo, en pesos."""
    credit: float
    """El abono, en pesos."""


class JournalEntry(TypedDict):
    """Una póliza de diario (de un CFDI, un pago, un recibo de nómina o la depreciación del mes): sus cargos y abonos, que siempre cuadran."""
    id: str
    """El número de la póliza: D-AAAAMM-NNNNN, en orden de fecha dentro del mes."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["journal_entry"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor."""
    type: Literal["invoice", "payment_received", "payment_made", "payroll", "employee_expenses", "depreciation"]
    """De qué es: invoice (un CFDI de ingreso o egreso), payment_received o payment_made (un pago de un complemento), payroll (un recibo de nómina), employee_expenses (un anticipo, reembolso, devolución o comprobación de viáticos, contra 107.01 «Funcionarios y empleados») o depreciation (la depreciación del mes de los activos fijos)."""
    date: str
    """La fecha del CFDI o del pago; en la depreciación, el último día del mes."""
    description: str
    """El documento, su folio y la contraparte."""
    invoice: str | None
    """La factura (inv_…) si es la póliza de un CFDI que timbró este emisor; null en los demás casos."""
    uuid: str | None
    """El folio fiscal del CFDI (o del complemento de pago); null en la depreciación."""
    tax_id: str | None
    """El RFC de la contraparte (cliente, proveedor o empleado); null en la depreciación."""
    total: float
    """El total del documento, en su moneda."""
    currency: str
    """La moneda del documento."""
    exchange_rate: float | None
    """El tipo de cambio, si no es en pesos; null si es en pesos."""
    lines: list[JournalEntryLinesItem]
    """Los movimientos, en pesos: el cargo (debit) o abono (credit) a cada cuenta."""


class LedgerAccount(TypedDict):
    """Una cuenta del catálogo, con su código agrupador del SAT."""
    object: Literal["ledger_account"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    number: str
    """El número de cuenta (NumCta)."""
    name: str
    """Su nombre."""
    grouping_code: str
    """El código agrupador del SAT (Anexo 24)."""
    nature: Literal["debit", "credit"]
    """debit (deudora) o credit (acreedora)."""


class TrialBalanceAccountsItem(TypedDict):
    object: Literal["ledger_account"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    number: str
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre."""
    grouping_code: str
    """El código agrupador del SAT."""
    nature: Literal["debit", "credit"]
    """debit (deudora) o credit (acreedora)."""
    opening_balance: float
    """El saldo al empezar el mes."""
    debit: float
    """Los cargos del mes."""
    credit: float
    """Los abonos del mes."""
    closing_balance: float
    """El saldo al terminar el mes."""


class TrialBalanceTotals(TypedDict):
    """Cargos y abonos del mes: siempre iguales."""
    debit: float
    """Todos los cargos del mes."""
    credit: float
    """Todos los abonos del mes."""


class TrialBalance(TypedDict):
    """La balanza de comprobación de un mes."""
    object: Literal["trial_balance"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    month: str
    """El mes (AAAA-MM)."""
    journal_entries: int
    """Cuántas pólizas tuvo el mes."""
    accounts: list[TrialBalanceAccountsItem]
    """Cada cuenta con movimiento o saldo: saldo inicial, cargos, abonos y saldo final."""
    totals: TrialBalanceTotals
    """Cargos y abonos del mes: siempre iguales."""


class FinancialStatementsIncomeStatementMonthSectionsItemGroupsItemAccountsItem(TypedDict):
    number: str
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre."""
    amount: float
    """Importe."""


class FinancialStatementsIncomeStatementMonthSectionsItemGroupsItem(TypedDict):
    grouping_code: str
    """El primer nivel del código agrupador (401, 601…)."""
    name: str
    """Nombre."""
    amount: float
    """Importe."""
    accounts: list[FinancialStatementsIncomeStatementMonthSectionsItemGroupsItemAccountsItem]
    """Las cuentas del grupo con su monto."""


class FinancialStatementsIncomeStatementMonthSectionsItem(TypedDict):
    key: Literal["ingresos", "costos", "gastos", "financiamiento", "otros"]
    """La sección: ingresos, costos, gastos, financiamiento u otros."""
    name: str
    """Nombre."""
    total: float
    """Total en la moneda del comprobante (Total)."""
    groups: list[FinancialStatementsIncomeStatementMonthSectionsItemGroupsItem]
    """Su monto por el primer nivel del código agrupador."""


class FinancialStatementsIncomeStatementMonth(TypedDict):
    """El estado de resultados del mes."""
    sections: list[FinancialStatementsIncomeStatementMonthSectionsItem]
    """Ingresos, costos, gastos, financiamiento y otros, cada uno con su total."""
    net_income: float
    """La utilidad (o pérdida, negativa) antes de impuestos del mes."""


class FinancialStatementsIncomeStatementYearToDateSectionsItemGroupsItemAccountsItem(TypedDict):
    number: str
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre."""
    amount: float
    """Importe."""


class FinancialStatementsIncomeStatementYearToDateSectionsItemGroupsItem(TypedDict):
    grouping_code: str
    """El primer nivel del código agrupador (401, 601…)."""
    name: str
    """Nombre."""
    amount: float
    """Importe."""
    accounts: list[FinancialStatementsIncomeStatementYearToDateSectionsItemGroupsItemAccountsItem]
    """Las cuentas del grupo con su monto."""


class FinancialStatementsIncomeStatementYearToDateSectionsItem(TypedDict):
    key: Literal["ingresos", "costos", "gastos", "financiamiento", "otros"]
    """La sección: ingresos, costos, gastos, financiamiento u otros."""
    name: str
    """Nombre."""
    total: float
    """Total en la moneda del comprobante (Total)."""
    groups: list[FinancialStatementsIncomeStatementYearToDateSectionsItemGroupsItem]
    """Su monto por el primer nivel del código agrupador."""


class FinancialStatementsIncomeStatementYearToDate(TypedDict):
    """El estado de resultados de enero al mes."""
    sections: list[FinancialStatementsIncomeStatementYearToDateSectionsItem]
    """Ingresos, costos, gastos, financiamiento y otros, cada uno con su total."""
    net_income: float
    """La utilidad (o pérdida, negativa) antes de impuestos de enero al mes."""


class FinancialStatementsIncomeStatement(TypedDict):
    """El estado de resultados del mes (month) y del año hasta ese mes (year_to_date). Cada sección suma en positivo lo que aumenta la utilidad (ingresos) y en negativo lo que la reduce (costos y gastos)."""
    month: FinancialStatementsIncomeStatementMonth
    """El estado de resultados del mes."""
    year_to_date: FinancialStatementsIncomeStatementYearToDate
    """El estado de resultados de enero al mes."""


class FinancialStatementsBalanceSheetAssetsGroupsItemAccountsItem(TypedDict):
    number: str
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre."""
    amount: float
    """Importe."""


class FinancialStatementsBalanceSheetAssetsGroupsItem(TypedDict):
    grouping_code: str
    """El primer nivel del código agrupador (401, 601…)."""
    name: str
    """Nombre."""
    amount: float
    """Importe."""
    accounts: list[FinancialStatementsBalanceSheetAssetsGroupsItemAccountsItem]
    """Las cuentas del grupo con su monto."""


class FinancialStatementsBalanceSheetAssets(TypedDict):
    """El activo: su total y sus grupos."""
    total: float
    """Total en la moneda del comprobante (Total)."""
    groups: list[FinancialStatementsBalanceSheetAssetsGroupsItem]
    """Su monto por el primer nivel del código agrupador."""


class FinancialStatementsBalanceSheetLiabilitiesGroupsItemAccountsItem(TypedDict):
    number: str
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre."""
    amount: float
    """Importe."""


class FinancialStatementsBalanceSheetLiabilitiesGroupsItem(TypedDict):
    grouping_code: str
    """El primer nivel del código agrupador (401, 601…)."""
    name: str
    """Nombre."""
    amount: float
    """Importe."""
    accounts: list[FinancialStatementsBalanceSheetLiabilitiesGroupsItemAccountsItem]
    """Las cuentas del grupo con su monto."""


class FinancialStatementsBalanceSheetLiabilities(TypedDict):
    """El pasivo: su total y sus grupos."""
    total: float
    """Total en la moneda del comprobante (Total)."""
    groups: list[FinancialStatementsBalanceSheetLiabilitiesGroupsItem]
    """Su monto por el primer nivel del código agrupador."""


class FinancialStatementsBalanceSheetEquityGroupsItemAccountsItem(TypedDict):
    number: str
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre."""
    amount: float
    """Importe."""


class FinancialStatementsBalanceSheetEquityGroupsItem(TypedDict):
    grouping_code: str
    """El primer nivel del código agrupador (401, 601…)."""
    name: str
    """Nombre."""
    amount: float
    """Importe."""
    accounts: list[FinancialStatementsBalanceSheetEquityGroupsItemAccountsItem]
    """Las cuentas del grupo con su monto."""


class FinancialStatementsBalanceSheetEquity(TypedDict):
    """El capital contable sin el resultado del ejercicio: su total y sus grupos."""
    total: float
    """Total en la moneda del comprobante (Total)."""
    groups: list[FinancialStatementsBalanceSheetEquityGroupsItem]
    """Su monto por el primer nivel del código agrupador."""


class FinancialStatementsBalanceSheet(TypedDict):
    """El balance general al cierre del mes, agrupado por el primer nivel del código agrupador. difference es activo menos pasivo y capital: 0 cuando los libros cuadran."""
    assets: FinancialStatementsBalanceSheetAssets
    """El activo: su total y sus grupos."""
    liabilities: FinancialStatementsBalanceSheetLiabilities
    """El pasivo: su total y sus grupos."""
    equity: FinancialStatementsBalanceSheetEquity
    """El capital contable sin el resultado del ejercicio: su total y sus grupos."""
    net_income_year_to_date: float
    """El resultado del ejercicio hasta el mes, parte del capital."""
    liabilities_and_equity: float
    """Pasivo más capital más el resultado del ejercicio."""
    difference: float
    """Activo menos pasivo y capital: 0 cuando los libros cuadran."""


class FinancialStatements(TypedDict):
    """El estado de resultados y el balance general de un mes, leídos de su balanza."""
    object: Literal["financial_statements"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    month: str
    """El mes (AAAA-MM)."""
    income_statement: FinancialStatementsIncomeStatement
    """El estado de resultados del mes (month) y del año hasta ese mes (year_to_date). Cada sección suma en positivo lo que aumenta la utilidad (ingresos) y en negativo lo que la reduce (costos y gastos)."""
    balance_sheet: FinancialStatementsBalanceSheet
    """El balance general al cierre del mes, agrupado por el primer nivel del código agrupador. difference es activo menos pasivo y capital: 0 cuando los libros cuadran."""
    journal_entries: int
    """Cuántas pólizas tuvo el mes."""
    opening_balances_date: str | None
    """Desde qué fecha cuentan los saldos iniciales capturados en la app; null si no hay."""
    missing_invoices: int
    """Pagos que se refieren a facturas que no están en Fiscalisto y no se registraron."""


class CrossChecksMonthsItemChecksItem(TypedDict):
    key: Literal["vat_charged", "vat_creditable", "vat_withheld", "isr_income", "isr_withheld_salaries", "isr_withheld_suppliers", "vat_withheld_suppliers"]
    """Qué cifra: vat_charged (IVA trasladado), vat_creditable (IVA acreditable), vat_withheld (IVA que le retuvieron), isr_income (ingresos para ISR: nominales en persona moral, cobrados en los demás) y, solo en los meses en que retuvo, isr_withheld_salaries (ISR retenido por salarios y asimilados, contra sus recibos de nómina), isr_withheld_suppliers (ISR retenido por honorarios y arrendamiento, contra las facturas recibidas que pagó) o vat_withheld_suppliers (IVA retenido a proveedores)."""
    status: Literal["matches", "differs", "not_filed", "unreadable"]
    """matches (hasta $2 de diferencia), differs, not_filed (no hay declaración del mes, o en una retención ninguna declaración del mes la trae) o unreadable (la declaración no trae la cifra en un renglón reconocible)."""
    declared: float | None
    """Lo declarado, en pesos; null si no hay declaración o no se pudo leer."""
    declared_without_cfdi: float
    """De declared, lo que la propia declaración dice que no salió de facturas: en isr_income los ingresos nominales adicionales (cobrado sin factura, intereses) y en vat_charged el IVA al 16% por encima de la precarga del SAT. Se compara aparte; 0 si no hay."""
    invoiced: float
    """Lo que dicen los CFDI del mes, con los mismos cálculos de Impuestos."""
    difference: float | None
    """declared menos declared_without_cfdi menos invoiced; null si declared es null."""
    operation_number: str | None
    """El número de operación de la declaración de donde salió la cifra."""


class CrossChecksMonthsItem(TypedDict):
    month: str
    """El mes (AAAA-MM)."""
    status: Literal["matches", "differs", "not_filed", "unreadable"]
    """El peor de sus cruces: differs (no coincide), unreadable (una cifra no se pudo leer), not_filed (sin declaración mensual) o matches."""
    checks: list[CrossChecksMonthsItemChecksItem]
    """Un cruce por cifra."""


class CrossChecksVatBalanceInFavorPeriodsItem(TypedDict):
    month: str
    """El mes cuya declaración muestra el IVA a favor."""
    amount: float
    """El IVA a favor de ese mes."""
    operation_number: str
    """El número de operación de esa declaración."""


class CrossChecksVatBalanceInFavor(TypedDict):
    """El IVA a favor que muestran las declaraciones del año y lo que meses posteriores acreditaron. Una estimación con las declaraciones leídas, no la cuenta del SAT."""
    periods: list[CrossChecksVatBalanceInFavorPeriodsItem]
    """Cada mes con IVA a favor."""
    total: float
    """La suma del IVA a favor del año."""
    credited: float
    """Lo que las declaraciones del año acreditaron de saldos a favor de periodos anteriores."""
    remaining: float
    """total menos credited, nunca menos de 0: lo que quedaría por acreditar o pedir en devolución."""


class CrossChecksTaxRegimesInvoicedItem(TypedDict):
    tax_regime: str
    """El régimen (c_RegimenFiscal)."""
    invoices: int
    """Cuántos CFDI lo llevan (ingreso, egreso y pago, sin cancelados)."""
    first_date: str
    """La fecha del primero (AAAA-MM-DD)."""
    last_date: str
    """La fecha del último (AAAA-MM-DD)."""
    registered: bool | None
    """Si el régimen está en su constancia; null si no se capturaron los regímenes de la constancia."""


class CrossChecksTaxRegimes(TypedDict):
    """Los regímenes del emisor (registered, de su constancia) y con cuáles facturó en el año."""
    registered: list[str]
    """Los regímenes de su constancia (c_RegimenFiscal), capturados en la app."""
    invoiced: list[CrossChecksTaxRegimesInvoicedItem]
    """Cada régimen con que facturó en el año (RegimenFiscal del emisor)."""


class CrossChecks(TypedDict):
    """Lo que el emisor declaró cada mes contra lo que dicen sus CFDI, el IVA a favor y el régimen con que factura."""
    object: Literal["cross_checks"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    year: int
    """El ejercicio."""
    months: list[CrossChecksMonthsItem]
    """Cada mes cuya declaración mensual ya venció (el día 17 del mes siguiente), con sus cruces. Un mes con complementaria toma, por impuesto, la más reciente que lo trae."""
    vat_balance_in_favor: CrossChecksVatBalanceInFavor
    """El IVA a favor que muestran las declaraciones del año y lo que meses posteriores acreditaron. Una estimación con las declaraciones leídas, no la cuenta del SAT."""
    tax_regimes: CrossChecksTaxRegimes
    """Los regímenes del emisor (registered, de su constancia) y con cuáles facturó en el año."""


class CrossCheckCfdiCfdiItem(TypedDict):
    uuid: str | None
    """El folio fiscal (UUID) del CFDI; el de la factura PPD en un pago."""
    type: Literal["invoice", "credit_note", "payment", "withholding_certificate"]
    """invoice (factura de ingreso, PUE), credit_note (nota de crédito: resta) o payment (lo pagado en el mes de una factura PPD)."""
    date: str | None
    """La fecha del CFDI, o la del pago (AAAA-MM-DD)."""
    tax_id: str | None
    """El RFC de la contraparte: el cliente en lo emitido, el proveedor en lo recibido."""
    name: str | None
    """El nombre de la contraparte, como viene en el CFDI."""
    amount: float
    """Lo que aporta a la cifra, en pesos; negativo en una nota de crédito."""


class CrossCheckCfdi(TypedDict):
    """Los CFDI que forman una cifra del cruce de un mes (invoiced): cada uno con lo que aporta, y el ajuste que Impuestos agrega encima."""
    object: Literal["cross_check_cfdi"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    month: str
    """El mes (AAAA-MM)."""
    key: Literal["vat_charged", "vat_creditable", "vat_withheld", "isr_income", "isr_withheld_salaries", "isr_withheld_suppliers", "vat_withheld_suppliers"]
    """La cifra: vat_charged (IVA trasladado), vat_creditable (IVA acreditable), vat_withheld (IVA que le retuvieron), isr_income (ingresos para ISR), isr_withheld_salaries (ISR retenido en sus recibos de nómina), isr_withheld_suppliers o vat_withheld_suppliers (ISR o IVA que retuvo a proveedores)."""
    status: Literal["matches", "differs", "not_filed", "unreadable"]
    """El cruce de esa cifra, como en GET /v1/accounting/cross_checks: matches, differs, not_filed o unreadable."""
    declared: float | None
    """Lo declarado, en pesos; null si no hay declaración o no se pudo leer."""
    declared_without_cfdi: float
    """De declared, lo que la propia declaración dice que no salió de facturas (ingresos nominales adicionales en isr_income, IVA al 16% sobre la precarga del SAT en vat_charged); 0 si no hay."""
    invoiced: float
    """Lo que dicen los CFDI del mes: la suma de cfdi más adjustment."""
    difference: float | None
    """declared menos declared_without_cfdi menos invoiced; null si declared es null."""
    operation_number: str | None
    """El número de operación de la declaración de donde salió la cifra."""
    cfdi: list[CrossCheckCfdiCfdiItem]
    """Cada CFDI que suma en el mes, de mayor a menor: los PUE y las notas de crédito en su mes, las facturas PPD por lo que se pagó en el mes."""
    adjustment: float
    """Lo que Impuestos agrega sobre los CFDI: en vat_creditable, la proporción de gastos comunes, el IVA retenido enterado del mes anterior y las importaciones; 0 en las demás."""


class DiotLinesItemPaid(TypedDict):
    """Lo pagado en el mes por tasa, en pesos, con su IVA."""
    base_16: float
    """Valor de los actos al 16 %."""
    base_8: float
    """Valor de los actos al 8 % (región fronteriza)."""
    base_0: float
    """Valor de los actos al 0 %."""
    exempt: float
    """Valor de los actos exentos."""
    not_taxable: float
    """Valor de los actos no objeto de IVA."""
    vat: float
    """El IVA de esos actos."""


class DiotLinesItemReturns(TypedDict):
    """Las devoluciones (notas de crédito) del mes, por tasa."""
    base_16: float
    """Valor de los actos al 16 %."""
    base_8: float
    """Valor de los actos al 8 % (región fronteriza)."""
    base_0: float
    """Valor de los actos al 0 %."""
    exempt: float
    """Valor de las devoluciones exentas."""
    not_taxable: float
    """Valor de los actos no objeto de IVA."""
    vat: float
    """El IVA de esos actos."""


class DiotLinesItem(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    name: str | None
    """Nombre."""
    third_party_type: Literal["15", "04", "05"]
    """Tipo de tercero: 04 nacional, 05 extranjero, 15 global."""
    operation_type: Literal["85", "87", "02", "03", "06", "07"]
    """Tipo de operación: 02 enajenación de bienes, 03 servicios profesionales, 06 uso o goce temporal, 07 importación, 85 otros, 87 operaciones globales."""
    paid: DiotLinesItemPaid
    """Lo pagado en el mes por tasa, en pesos, con su IVA."""
    returns: DiotLinesItemReturns
    """Las devoluciones (notas de crédito) del mes, por tasa."""
    blacklisted: bool
    """El proveedor está en la lista 69-B definitiva: revise si deduce sus CFDI."""


class Diot(TypedDict):
    """La DIOT de un mes: lo pagado a cada proveedor, por tipo de operación."""
    object: Literal["diot"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    month: str
    """El mes (AAAA-MM)."""
    proportion: float
    """La proporción de IVA acreditable del mes para gastos comunes (1 si no la aplica)."""
    lines: list[DiotLinesItem]
    """Una línea por proveedor y tipo de operación, con lo pagado en el mes."""
    warnings: list[str]
    """Lo que conviene revisar antes de presentarla."""


class VatRefundBalancesItemCreditedInItem(TypedDict):
    month: str
    """El mes en que se acreditó esa parte (AAAA-MM)."""
    amount: float
    """Lo acreditado ese mes."""


class VatRefundBalancesItem(TypedDict):
    month: str
    """El mes del saldo (AAAA-MM)."""
    source: Literal["declaration", "cfdi"]
    """declaration si sale de la declaración leída; cfdi si se calculó con sus CFDI."""
    amount: float
    """El saldo a favor del mes."""
    operation_number: str | None
    """El número de operación de la declaración, o null."""
    credited: float
    """Lo que de este saldo se acreditó en meses posteriores, del saldo más antiguo primero."""
    credited_in: list[VatRefundBalancesItemCreditedInItem]
    """En qué mes se acreditó cada parte y cuánto."""
    available: float
    """Lo que queda de este saldo para pedir de vuelta."""
    status: Literal["available", "credited", "in_refund", "refunded", "denied", "prescribed"]
    """available (se puede pedir), credited (ya se acreditó), in_refund (con solicitud), refunded (depositado), denied (negado) o prescribed (pasaron cinco años)."""
    prescribes_on: str
    """Cuándo prescribe el derecho a pedirlo: cinco años desde su declaración (AAAA-MM-DD)."""


class VatRefundReviewChecksItem(TypedDict):
    key: str
    """Qué se revisó, estable para su código."""
    result: Literal["ok", "warning", "blocking", "pending"]
    """ok, warning (conviene revisar), blocking (el SAT la rechazaría) o pending (falta un dato)."""
    title: str
    """La revisión, en una línea."""
    detail: str
    """Qué encontró y qué hacer."""
    amount: float | None
    """Los pesos que toca, como el IVA en riesgo, o null."""


class VatRefundReviewSuppliers(TypedDict):
    """Los proveedores del mes, para la relación que pide el SAT."""
    count: int
    """Cuántos proveedores tuvo en el mes."""
    cfdi: int
    """Cuántos CFDI recibidos suman al IVA acreditable."""
    main: int
    """Cuántos proveedores juntan el 80% del IVA acreditable."""
    vat_at_risk: float
    """El IVA de CFDI de proveedores que el SAT no reconocería: cancelados, de EFOS o con otros hallazgos."""


class VatRefundReviewCustomers(TypedDict):
    """Los clientes del mes."""
    count: int
    """Cuántos clientes tuvo en el mes."""
    cfdi: int
    """Cuántos CFDI emitidos suman al IVA cobrado."""


class VatRefundReview(TypedDict):
    month: str
    """El mes revisado (AAAA-MM)."""
    amount_to_request: float
    """Lo que conviene pedir, en pesos sin centavos como lo pide el SAT."""
    remainder: bool
    """true si ya acreditó parte del saldo y lo que pide es el remanente."""
    ready: bool
    """true si ninguna revisión bloquea la solicitud."""
    checks: list[VatRefundReviewChecksItem]
    """Cada revisión, de la más grave a la que está bien."""
    suppliers: VatRefundReviewSuppliers
    """Los proveedores del mes, para la relación que pide el SAT."""
    customers: VatRefundReviewCustomers
    """Los clientes del mes."""


class VatRefund(TypedDict):
    """El IVA a favor del emisor mes por mes, qué pasó con cada saldo y, con un mes, la revisión antes de pedir su devolución."""
    object: Literal["vat_refund"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    available: float
    """El IVA a favor que todavía puede pedir de vuelta: lo que queda de cada saldo sin acreditar, sin solicitud y sin prescribir."""
    in_refund: float
    """Lo pedido en solicitudes que siguen en trámite o ya se resolvieron sin depósito."""
    refunded: float
    """Lo que el SAT ya depositó."""
    estimated: bool
    """true si algún mes sale de sus CFDI porque su declaración no se ha leído (POST /v1/sat_declarations/refresh)."""
    balances: list[VatRefundBalancesItem]
    """Cada mes con IVA a favor en los últimos cinco años, del más reciente al más antiguo."""
    review: VatRefundReview | None
    """Con month, la revisión de ese mes antes de pedirlo; null sin month."""


class StoreConnectionSettings(TypedDict):
    """Cómo se vuelve ticket cada pedido."""
    product_key: str | None
    """c_ClaveProdServ de lo que vende, o null."""
    unit_key: str | None
    """c_ClaveUnidad, o null (la de la clave del producto)."""
    iva: Literal["0", "0.16", "0.08", "exento"]
    """Tasa de IVA incluida en los precios."""
    description: str | None
    """El concepto fijo de cada ticket, o null (el pedido y sus artículos)."""
    folio_prefix: str
    """Lo que va antes del número del pedido en el folio."""
    payment_form: str | None
    """c_FormaPago cuando la del pedido no está en payment_forms, o null."""
    payment_forms: dict[str, str]
    """c_FormaPago por pasarela o tipo de pago."""
    auto_invoice: bool | None
    """Mercado Libre: si se timbra al momento con los datos fiscales del comprador; null en las demás plataformas."""
    notify_buyer: bool | None
    """WooCommerce y Tiendanube: si el comprador recibe su enlace para facturar (nota del pedido o correo); null en las demás plataformas."""


class StoreConnectionLastError(TypedDict):
    message: str
    """Qué pasó."""
    at: str | None
    """Cuándo."""


class StoreConnection(TypedDict):
    """Una tienda de Shopify, WooCommerce, Tiendanube, Mercado Libre o Amazon cuyos pedidos pagados se vuelven tickets de autofactura del emisor."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["store_connection"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor dueño de la tienda."""
    platform: Literal["shopify", "mercadolibre", "amazon", "tiendanube", "woocommerce"]
    """shopify, woocommerce, tiendanube, mercadolibre o amazon."""
    shop: str | None
    """El dominio de la tienda (Shopify, WooCommerce), o el id de la tienda en Tiendanube o del vendedor en Mercado Libre y Amazon (al autorizar)."""
    name: str | None
    """El nombre de la tienda según su plataforma, o null."""
    status: Literal["pending", "active", "disconnected"]
    """pending (Mercado Libre, Tiendanube o Amazon esperan que se autorice en authorize_url), active o disconnected."""
    authorize_url: str | None
    """Si está pending: la página de la plataforma donde el vendedor autoriza (vale un día; cada consulta da una nueva). Si no, null."""
    settings: StoreConnectionSettings
    """Cómo se vuelve ticket cada pedido."""
    orders_count: int
    """Cuántos pedidos se han vuelto tickets."""
    last_order_at: str | None
    """Cuándo llegó el último, o null."""
    last_error: StoreConnectionLastError | None
    """El último problema (un pedido en dólares, un ticket que ya se facturó cuando se canceló el pedido…), o null."""
    created_at: str | None
    """Cuándo se conectó."""


class StoreImportSkippedItem(TypedDict):
    order: str
    """El pedido."""
    reason: str
    """Por qué no se volvió ticket."""


class StoreImport(TypedDict):
    """Los pedidos pagados que se trajeron."""
    object: Literal["store_import"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    store_connection: str
    """La conexión (stc_…)."""
    since: str
    """Desde qué día se buscaron pedidos."""
    tickets: int
    """Pedidos que son tickets (los que ya lo eran cuentan otra vez)."""
    invoiced: int
    """De ellos, los que se facturaron al momento con los datos del comprador."""
    skipped: list[StoreImportSkippedItem]
    """Los que no se volvieron ticket, con el motivo."""


class QuoteCustomer(TypedDict):
    """A quién va: tax_id null si aún no tiene sus datos fiscales; catalog_id es su cliente (cus_…) en su catálogo, o null."""
    tax_id: str | None
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    name: str | None
    """Nombre."""
    email: str | None
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    catalog_id: str | None
    """El cliente (cus_…) en su catálogo, o null si no está en él."""


class QuoteItemsItem(TypedDict):
    description: str
    """Descripción del concepto (Descripcion), hasta 1,000 caracteres."""
    product_key: str
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    quantity: NotRequired[float]
    """Cantidad (Cantidad). Por omisión 1."""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_price: float
    """Precio unitario antes de impuestos (ValorUnitario)."""


class Quote(TypedDict):
    """Una cotización: su cliente la ve en una liga, la acepta, pide cambios o la rechaza, y se factura."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["quote"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    number: str
    """Su serie y folio, como lo ve el cliente (COT-12)."""
    version: int
    """Cambiar una ya enviada hace una versión nueva con el mismo número; el id contesta siempre la última."""
    status: Literal["draft", "sent", "viewed", "accepted", "rejected", "withdrawn", "expired", "invoiced"]
    """draft, sent, viewed (el cliente abrió la liga), accepted, rejected, withdrawn (usted la retiró), expired (pasó valid_until) o invoiced."""
    url: str | None
    """La liga donde el cliente la ve, descarga su PDF, la acepta, pide cambios o la rechaza; null mientras sea borrador."""
    customer: QuoteCustomer
    """A quién va: tax_id null si aún no tiene sus datos fiscales; catalog_id es su cliente (cus_…) en su catálogo, o null."""
    currency: str
    """La moneda."""
    items: list[QuoteItemsItem]
    """Los conceptos, como los de una factura."""
    total: float | None
    """El total con impuestos."""
    valid_until: str
    """Su último día de validez (AAAA-MM-DD)."""
    terms: str | None
    """Las condiciones impresas: entrega, anticipo, garantía…"""
    notes: str | None
    """Las notas, como las de una factura."""
    auto_invoice: bool
    """Si al aceptarla se timbra la factura sola."""
    remind: bool
    """Si se le manda un recordatorio por correo 3 días antes de su último día mientras no responda (remind en POST /v1/quotes/{id}/send)."""
    reminded_at: str | None
    """Cuándo se mandó el recordatorio, o null."""
    customer_comment: str | None
    """Lo que escribió el cliente al pedir cambios o al rechazarla, la nota de usted al retirarla o marcarla rechazada, o null."""
    sent_at: str | None
    """Cuándo se envió."""
    viewed_at: str | None
    """Cuándo el cliente abrió la liga por primera vez."""
    decided_at: str | None
    """Cuándo se aceptó, se rechazó o se retiró."""
    decided_by: Literal["customer", "user"] | None
    """customer (en su liga) o user (usted: POST /v1/quotes/{id}/accept, /reject o /withdraw, o desde la app)."""
    invoice: str | None
    """La factura (inv_…) que se timbró de ella, o null."""
    created_at: str | None
    """Cuándo se creó."""


class SalesOrderCustomer(TypedDict):
    """El cliente: su RFC, nombre, correo y su id en su catálogo."""
    tax_id: str | None
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    name: str | None
    """Nombre."""
    email: str | None
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    catalog_id: str | None
    """El cliente (cus_…) en su catálogo, o null si no está en él."""


class SalesOrderItemsItem(TypedDict):
    id: int
    """El id del concepto en el pedido: con él entrega o factura una parte (line)."""
    description: str
    """Descripción del concepto (Descripcion), hasta 1,000 caracteres."""
    product_key: str | None
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    quantity: float
    """Cantidad (Cantidad). Por omisión 1."""
    unit: str | None
    """La unidad, como la ve el cliente."""
    unit_price: float
    """Precio unitario antes de impuestos (ValorUnitario)."""
    discount: float
    """El descuento del concepto, en dinero."""
    amount: float
    """El importe del concepto, sin impuestos."""
    goods: bool
    """true si sale del almacén con cada entrega; false si es un servicio (solo se factura)."""
    delivered: float
    """Cuánto ya se entregó."""
    invoiced: float
    """Cuánto ya se facturó."""
    canceled: float
    """Cuánto ya no se entregará (POST /v1/sales_orders/{id}/cancel_remaining)."""


class SalesOrderInvoicesItem(TypedDict):
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    status: Literal["stamped", "canceled"]
    """stamped, o canceled (lo que llevaba se puede volver a facturar)."""
    total: float
    """El total de la factura."""
    balance: float | None
    """Lo que falta por pagar de esa factura, o null si aún no se sabe."""


class SalesOrder(TypedDict):
    """Un pedido de venta: lo que su cliente pidió, cómo se entrega (remisiones) y cómo se factura y se cobra."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["sales_order"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (iss_…)."""
    number: str
    """Su serie y folio (PED-12)."""
    status: Literal["draft", "confirmed", "partially_delivered", "delivered", "invoiced", "paid", "closed", "canceled"]
    """draft (borrador), confirmed, partially_delivered, delivered (todo entregado), invoiced (todo facturado), paid (sus facturas pagadas), closed (se dio por terminado) o canceled. Cambia solo, con lo que pasa."""
    stage: str | None
    """La etapa del negocio en que va («Por empacar», «En ruta»…), o null. Se elige en la app."""
    url: str | None
    """La liga donde su cliente ve el pedido, lo confirma, firma cada entrega y abre sus facturas. null mientras sea borrador o no se haya mandado."""
    customer: SalesOrderCustomer
    """El cliente: su RFC, nombre, correo y su id en su catálogo."""
    customer_po: str | None
    """El número de orden de compra de su cliente, o null."""
    quote: str | None
    """La cotización (quo_…) de donde salió, o null."""
    currency: str
    """La moneda."""
    items: list[SalesOrderItemsItem]
    """Los conceptos: id (para entregar o facturar una parte), lo pedido, lo entregado, lo facturado y lo que ya no se entregará (canceled). goods es true cuando sale del almacén."""
    subtotal: float
    """El subtotal, sin impuestos."""
    total: float
    """El total con impuestos."""
    invoiced_total: float
    """La suma de sus facturas timbradas (sin las canceladas)."""
    paid_total: float
    """Lo que ya se pagó de esas facturas."""
    expected_on: str | None
    """La entrega estimada (AAAA-MM-DD), o null."""
    payment_days: int
    """Días de crédito: cada factura vence esos días después de su fecha."""
    invoice_policy: Literal["delivered", "ordered"]
    """delivered: cada factura lleva lo ya entregado; ordered: se factura lo pedido, entregado o no."""
    ship_to: str | None
    """Dónde se entrega, o null."""
    terms: str | None
    """Las condiciones impresas en el pedido, o null."""
    notes: str | None
    """Las notas, como las de una factura."""
    internal_note: str | None
    """La nota interna (su cliente no la ve), o null."""
    deliveries: list[SalesOrderDelivery]
    """Sus entregas, cada una con su remisión."""
    invoices: list[SalesOrderInvoicesItem]
    """Sus facturas timbradas (inv_…), con lo que falta por pagar de cada una (balance)."""
    customer_confirmed_at: str | None
    """Cuándo su cliente lo confirmó en su liga, o null."""
    sent_at: str | None
    """Cuándo se mandó, o null."""
    viewed_at: str | None
    """Cuándo su cliente abrió la liga por primera vez, o null."""
    confirmed_at: str | None
    """Cuándo se confirmó, o null."""
    delivered_at: str | None
    """Cuándo quedó todo entregado, o null."""
    invoiced_at: str | None
    """Cuándo quedó todo facturado, o null."""
    paid_at: str | None
    """Cuándo quedaron pagadas sus facturas, o null."""
    closed_at: str | None
    """Cuándo se cerró, o null."""
    canceled_at: str | None
    """Cuándo se canceló, o null."""
    cancel_reason: str | None
    """Por qué se canceló, o null."""
    created_at: str | None
    """Cuándo se creó."""


class PortalSupplierDocuments(TypedDict):
    """Su alta: complete cuando todo lo obligatorio está aprobado y vigente, y cuántos documentos faltan, esperan revisión, vencieron o están por vencer."""
    complete: bool
    """true cuando todo lo obligatorio de su alta está aprobado y vigente."""
    missing: int
    """Cuántos documentos obligatorios no ha subido."""
    pending: int
    """Cuántos esperan revisión."""
    expired: int
    """Cuántos vencieron."""
    expiring: int
    """Cuántos vencen en los próximos 7 días."""


class PortalSupplierBankAccount(TypedDict):
    clabe: str
    """La CLABE de 18 dígitos."""
    bank: str | None
    """El banco, o null."""
    holder: str | None
    """El titular de la cuenta, o null."""
    status: Literal["pending", "approved", "rejected"]
    """Estado del objeto."""
    previous_clabe: str | None
    """Mientras una CLABE nueva está pending, la anterior, a la que se le sigue pagando; si no, null."""


class PortalSupplierScorePartsItem(TypedDict):
    part: Literal["invoices", "deliveries", "prices", "documents", "complements"]
    """invoices (facturas a la primera), deliveries (entregas a tiempo), prices (precio y cantidad de la orden), documents (documentos al día) o complements (complementos de pago)."""
    value: int | None
    """Valor de la mercancía (ValorMercancia); obligatorio en transporte aéreo."""
    good: int
    """En cuántos de los total casos lo hizo bien."""
    total: int
    """Total en la moneda del comprobante (Total)."""


class PortalSupplierScore(TypedDict):
    """Su calificación de 0 a 100 de los últimos 12 meses (value, null sin datos; level excellent, good, fair o poor) y cada parte: invoices (facturas a la primera), deliveries (entregas a tiempo), prices (precio y cantidad de la orden), documents (documentos al día) y complements (complementos de pago), con good de total casos."""
    value: int | None
    """Valor de la mercancía (ValorMercancia); obligatorio en transporte aéreo."""
    level: Literal["excellent", "good", "fair", "poor"] | None
    """Nivel educativo (nivelEducativo)."""
    parts: list[PortalSupplierScorePartsItem]
    """Partes del transporte que posee o arrienda (ParteTransporte), c_ParteTransporte."""


class PortalSupplier(TypedDict):
    """Un proveedor del Portal de proveedores del emisor: su alta, sus documentos, la cuenta a la que se le paga y su calificación."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["portal_supplier"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor de su cuenta (iss_…) cuyo portal es."""
    tax_id: str
    """El RFC del proveedor."""
    name: str | None
    """Su nombre o razón social, o null si aún no lo da."""
    emails: list[str]
    """Los correos a los que le escribimos."""
    phone: str | None
    """Su teléfono, o null."""
    status: Literal["invited", "onboarding", "in_review", "approved", "rejected", "suspended"]
    """invited (invitado), onboarding (dando su alta), in_review (alta por revisar), approved (puede mandar facturas), rejected o suspended."""
    repse: bool
    """true si da servicios especializados (REPSE)."""
    documents: PortalSupplierDocuments
    """Su alta: complete cuando todo lo obligatorio está aprobado y vigente, y cuántos documentos faltan, esperan revisión, vencieron o están por vencer."""
    bank_account: PortalSupplierBankAccount | None
    """La cuenta a la que se le paga, o null. Una nueva queda pending hasta que se aprueba en la app; mientras, se le paga a previous_clabe."""
    score: PortalSupplierScore
    """Su calificación de 0 a 100 de los últimos 12 meses (value, null sin datos; level excellent, good, fair o poor) y cada parte: invoices (facturas a la primera), deliveries (entregas a tiempo), prices (precio y cantidad de la orden), documents (documentos al día) y complements (complementos de pago), con good de total casos."""
    last_seen_at: str | None
    """La última vez que entró a su portal, o null."""
    created_at: str | None
    """Cuándo se invitó o se registró."""
    updated_at: str | None
    """Cuándo cambió por última vez."""


class SupplierInvoiceWarningsItem(TypedDict):
    code: str
    """Clave de la retención (CveRetenc), c_CveRetenc: 01 servicios profesionales, 05 arrendamiento, 14 dividendos, 16 intereses, 18 pagos al extranjero… Las claves 14, 16, 17 y 18 a 24 llevan su complemento (dividends, interest, trust_lease, foreign_payment, share_sale, prize, trust, retirement_plan, mortgage_interest, financial_derivatives); la 26 (plataformas tecnológicas) lleva platform, y sus totals y taxes se calculan de las operaciones."""
    message: str
    """Qué pasó y cómo corregirlo, para una persona."""


class SupplierInvoice(TypedDict):
    """Una factura que un proveedor le mandó al emisor por su Portal de proveedores, con lo que se revisó, su orden de compra, su contrarecibo y sus fechas de pago."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["supplier_invoice"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor de su cuenta (iss_…) que la recibió."""
    supplier: str
    """El proveedor (sup_…) que la mandó."""
    supplier_tax_id: str
    """El RFC del proveedor."""
    uuid: str
    """El folio fiscal (UUID del timbre)."""
    sat_invoice: str | None
    """La misma factura en sus facturas recibidas (sat_…), para su XML y su PDF, o null."""
    series: str | None
    """Su serie, o null."""
    folio: str | None
    """Su folio, o null."""
    type: Literal["income", "credit_note"]
    """income (factura de ingreso) o credit_note (nota de crédito)."""
    date: str
    """La fecha de la factura."""
    currency: str
    """La moneda."""
    total: float
    """El total de la factura."""
    payable: float
    """Lo que se le paga: el total sin las diferencias con su orden ni el descuento de pronto pago aceptado."""
    payment_method: str | None
    """PUE o PPD."""
    status: Literal["received", "approved", "scheduled", "paid", "rejected"]
    """received (por revisar), approved, scheduled (con fecha de pago), paid o rejected."""
    purchase_order: str | None
    """La orden de compra que factura (OC-12), o null."""
    matches_purchase_order: bool | None
    """true si cuadró con su orden, false si tuvo diferencias, null sin orden."""
    contrarecibo: str | None
    """El folio de su contrarecibo, o null."""
    due_on: str | None
    """El día en que vence por sus fechas de pago, o null."""
    scheduled_on: str | None
    """El día programado para pagarla, o null."""
    paid_on: str | None
    """El día en que se pagó, o null."""
    paid_amount: float | None
    """Lo que se pagó, o null."""
    payment_reference: str | None
    """La referencia del pago, o null."""
    rejection_reason: str | None
    """Por qué se rechazó, o null."""
    warnings: list[SupplierInvoiceWarningsItem]
    """Lo que se revisó y quedó como aviso (code y message), para que su equipo lo vea."""
    received_at: str | None
    """Cuándo llegó."""
    approved_at: str | None
    """Cuándo se aprobó, o null."""


class SalesOrderDeliveryItemsItem(TypedDict):
    line: int
    """El concepto del pedido (su items[].id)."""
    quantity: float
    """Cuánto salió de él."""


class SalesOrderDelivery(TypedDict):
    """Una entrega del pedido, con su remisión (REM-1): lo que salió del almacén."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["sales_order_delivery"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    number: str
    """Su remisión (REM-1)."""
    status: Literal["delivered", "canceled"]
    """delivered, o canceled (la mercancía regresó al almacén)."""
    delivered_on: str
    """El día en que salió (AAAA-MM-DD)."""
    carrier: str | None
    """El transporte, o null."""
    tracking: str | None
    """El número de guía, o null."""
    note: str | None
    """Una nota, o null."""
    received_by: str | None
    """Quién recibió (lo firmó en la liga o lo anotó usted), o null."""
    received_at: str | None
    """Cuándo se recibió, o null."""
    items: list[SalesOrderDeliveryItemsItem]
    """Cuánto salió de cada concepto (line es items[].id del pedido)."""
    created_at: str | None
    """Cuándo se registró."""


class ReceivableCustomer(TypedDict):
    """El cliente que debe."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str | None
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""


class Receivable(TypedDict):
    """Lo que un cliente le debe a un emisor en una moneda, de sus facturas abiertas."""
    id: str
    """El RFC y la moneda (RFC:MXN): para starting_after."""
    object: Literal["receivable"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    customer: ReceivableCustomer
    """El cliente que debe."""
    currency: str
    """La moneda de esas facturas."""
    amount_due: float
    """Lo que debe en total, en esa moneda."""
    open_invoices: int
    """Cuántas facturas tiene abiertas."""
    oldest_invoice_date: str
    """La fecha (AAAA-MM-DD) de su factura abierta más antigua."""


class CustomerPaymentBehaviorTrend(TypedDict):
    direction: Literal["slower", "faster", "steady"]
    """slower: tarda 7 días o más que antes; faster: 7 o más menos."""
    recent_days: float
    """Días promedio para pagar de los últimos 3 meses."""
    earlier_days: float
    """Días promedio de los 9 meses anteriores."""


class CustomerPaymentBehaviorPaymentFormsItem(TypedDict):
    payment_form: str
    """Clave de forma de pago del SAT (c_FormaPago): 03 transferencia, 02 cheque…"""
    amount: float
    """Lo pagado así, en pesos."""
    share: float
    """Su parte de lo pagado (0 a 1)."""


class CustomerPaymentBehaviorMonthsItem(TypedDict):
    month: str
    """El mes de los pagos (AAAA-MM)."""
    average_days_to_pay: float | None
    """Días promedio (por monto) de los pagos de ese mes; null sin pagos."""
    amount: float
    """Lo pagado ese mes, en pesos."""
    paid_invoices: int
    """Facturas con un pago ese mes."""


class CustomerPaymentBehaviorLastPayment(TypedDict):
    date: str
    """El día (AAAA-MM-DD)."""
    amount: float
    """Lo pagado ese día, en pesos."""


class CustomerPaymentBehaviorOpenInvoicesItem(TypedDict):
    uuid: str
    """El UUID (folio fiscal) de la factura."""
    date: str
    """Su fecha (AAAA-MM-DD)."""
    payment_method: Literal["PPD", "PUE"]
    """PPD a crédito; PUE que le pagan este mes."""
    amount_due: float
    """Lo que falta, en pesos."""
    due_date: str
    """Cuándo vence: su fecha más los días de crédito (una PUE, al fin de su mes)."""
    expected_payment_date: str
    """Cuándo le llegaría: su fecha más lo que el cliente suele tardar (sin historial, el vencimiento)."""


class CustomerPaymentBehavior(TypedDict):
    """Cómo paga un cliente: de sus facturas a crédito (PPD) de los últimos 12 meses y sus complementos de pago, en pesos."""
    object: Literal["customer_payment_behavior"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    customer: str
    """El cliente (cus_…)."""
    tax_id: str
    """Su RFC."""
    credit_days: int
    """Sus días de crédito: los suyos (Clientes) o los de la empresa (Ajustes › Cobranza automática). Contra ellos se mide el atraso."""
    rating: Literal["on_time", "sometimes_late", "late", "very_late", "no_history"]
    """on_time (80 % o más llega a tiempo y atraso promedio de 5 días o menos), sometimes_late (hasta 15 días), late (hasta 45), very_late (más) o no_history (menos de 2 facturas pagadas y nada vencido)."""
    paid_invoices: int
    """Facturas PPD con un pago en los últimos 12 meses."""
    average_days_to_pay: float | None
    """Días de la factura a su pago, en promedio por monto; null sin pagos."""
    median_days_to_pay: int | None
    """La factura típica: la mitad se pagó en estos días o menos."""
    p75_days_to_pay: int | None
    """3 de cada 4 facturas se pagaron en estos días o menos."""
    on_time_share: float | None
    """La parte (0 a 1) de lo pagado que llegó antes de vencer; lo vencido sin pagar cuenta como tarde."""
    average_days_late: float | None
    """Días después del vencimiento, en promedio por monto; lo vencido sin pagar cuenta con sus días de atraso hasta hoy."""
    trend: CustomerPaymentBehaviorTrend | None
    """Los últimos 3 meses contra los 9 anteriores; null con menos de 2 facturas pagadas en cada lado."""
    overdue_amount: float
    """Lo que debe ya vencido, en pesos."""
    overdue_invoices: int
    """Cuántas facturas tiene vencidas."""
    payment_forms: list[CustomerPaymentBehaviorPaymentFormsItem]
    """Cómo le pagó, la mayor primero."""
    months: list[CustomerPaymentBehaviorMonthsItem]
    """Cada uno de los últimos 12 meses, el más antiguo primero."""
    last_payment: CustomerPaymentBehaviorLastPayment | None
    """Su último pago; null sin pagos en 12 meses."""
    cash_invoices: int
    """Facturas de contado (PUE) de los últimos 12 meses: se pagan al emitirse y no cuentan en lo demás."""
    open_invoices: list[CustomerPaymentBehaviorOpenInvoicesItem]
    """Lo que debe ahora, la factura más antigua primero."""


class BankTransactionSuggestedMatch(TypedDict):
    invoices: list[str]
    """Las facturas, como el cuerpo de POST /v1/invoices, con reference opcional."""
    amounts: dict[str, float]
    """Lo que el depósito pagaría de cada factura (por inv_…)."""
    method: Literal["PPD", "PUE"]
    """PUE: facturas por cobrar que quedan pagadas al conciliar; PPD: se pagan con su complemento de pago (POST /v1/payments)."""
    confidence: Literal["high", "medium"]
    """high (el monto y además el RFC, el nombre o el folio coinciden) o medium (revíselo antes)."""
    reasons: list[str]
    """Por qué se sugiere, en palabras."""


class BankTransaction(TypedDict):
    """Un depósito de la cuenta del emisor, y las facturas que pagó."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["bank_transaction"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor."""
    date: str
    """El día del depósito (AAAA-MM-DD)."""
    amount: float
    """Lo depositado, en pesos."""
    description: str
    """El concepto del banco."""
    reference: str | None
    """La referencia o clave de rastreo, o null."""
    account: str | None
    """Los últimos 4 dígitos de la cuenta, o null."""
    payer_tax_id: str | None
    """El RFC de quien depositó, si se sabe."""
    status: Literal["open", "matched", "classified"]
    """open (sin conciliar), matched (pagó facturas) o classified (no es de una factura)."""
    classification: Literal["venta", "prestamo", "traspaso", "devolucion"] | None
    """classified: venta (aún sin facturar), prestamo, traspaso o devolucion; si no, null."""
    note: str | None
    """Una nota al clasificarlo, o null."""
    invoices: list[str]
    """Las facturas (inv_…) que pagó, si está conciliado."""
    payment: str | None
    """El complemento de pago (inv_…) timbrado con él, o null."""
    suggested_match: BankTransactionSuggestedMatch | None
    """Si está abierto, las facturas que parece pagar (por monto, RFC, folio en el concepto y fecha): invoices, lo que toca a cada una (amounts), method, confidence (high o medium) y por qué (reasons). null si ninguna encaja."""
    created_at: str | None
    """Cuándo se mandó."""


class BankImport(TypedDict):
    """Los depósitos que se agregaron."""
    object: Literal["bank_import"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor."""
    added: int
    """Cuántos depósitos se agregaron."""
    duplicates: int
    """Cuántos ya estaban (se omitieron)."""
    data: list[BankTransaction]
    """Los depósitos agregados."""


class PurchaseReceiptStore(TypedDict):
    """La tienda: name, tax_id (su RFC), email, portal_url (su portal o la liga del QR) y on_fiscalisto (factura con Fiscalisto: method fiscalisto la timbra al momento)."""
    name: str | None
    """Nombre."""
    tax_id: str | None
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    email: str | None
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    portal_url: str | None
    """Su portal de facturación o la liga del QR, o null."""
    on_fiscalisto: bool
    """true si factura con Fiscalisto: method fiscalisto timbra la factura al momento."""


class PurchaseReceiptFieldsItem(TypedDict):
    label: str
    """Cómo lo llama el ticket (Web ID, Sucursal…)."""
    value: str
    """Lo que dice el ticket en ese dato."""


class PurchaseReceiptRequested(TypedDict):
    method: str | None
    """egreso (la factura completa y después una nota de crédito por el anticipo, opción A) o remanente (la factura solo por lo que falta, opción B)."""
    to: str | None
    """A quién (correos separados por comas)."""
    at: str | None
    """Cuándo se pidió."""


class PurchaseReceipt(TypedDict):
    """Un ticket de compra del emisor sin factura: lo que se leyó de su foto y si ya se pidió, llegó o no es deducible."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["purchase_receipt"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    issuer: str
    """El emisor (el que compró)."""
    status: Literal["pending", "requested", "invoiced", "non_deductible"]
    """pending (por pedir), requested (pedida a la tienda), invoiced (ya tiene factura) o non_deductible (no hubo factura)."""
    store: PurchaseReceiptStore
    """La tienda: name, tax_id (su RFC), email, portal_url (su portal o la liga del QR) y on_fiscalisto (factura con Fiscalisto: method fiscalisto la timbra al momento)."""
    date: str | None
    """El día de la compra (AAAA-MM-DD), o null."""
    total: float | None
    """El total pagado, en pesos, o null."""
    payment_method: Literal["efectivo", "tarjeta", "otro"] | None
    """efectivo, tarjeta u otro, o null."""
    folio: str | None
    """El folio o número de ticket, o null."""
    fields: list[PurchaseReceiptFieldsItem]
    """Otros datos que pide el portal de la tienda para facturar (Web ID, sucursal, caja…)."""
    use: str | None
    """El uso del CFDI que se pide, o null: G03 si el régimen del emisor lo permite, si no S01."""
    note: str | None
    """Una nota, o null."""
    file_type: str | None
    """El tipo del archivo guardado (image/jpeg, application/pdf…)."""
    cash_over_limit: bool
    """true si se pagó en efectivo más de $2,000: aunque tenga factura, no es deducible (LISR art. 27 fr. III)."""
    days_left_in_month: int | None
    """Por pedir: los días que le quedan al mes de la compra, en hora de México (muchas tiendas solo facturan dentro del mes); si no, null."""
    requested: PurchaseReceiptRequested | None
    """Cuándo y cómo se pidió (method: fiscalisto, email, portal o manual; to: la tienda o su correo), o null."""
    invoice_uuid: str | None
    """El folio fiscal de la factura que lo cubre, o null."""
    invoice: str | None
    """La factura recibida (sat_…) que lo cubre, si ya llegó con las descargas del SAT, o null."""
    invoiced_at: str | None
    """Cuándo quedó facturado, o null."""
    non_deductible_at: str | None
    """Cuándo se marcó no deducible, o null."""
    created_at: str | None
    """Cuándo se guardó."""


class IssuerOnboardingLink(TypedDict):
    """Una liga para que el dueño de un emisor suba su CSD y firme con su e.firma."""
    object: Literal["issuer_onboarding_link"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    issuer: str
    """El emisor que se da de alta."""
    url: str
    """La página para el dueño del emisor, en fiscalisto.com. Ábrala en el navegador de su cliente; no la incruste en un iframe."""
    return_url: str | None
    """A dónde regresa al terminar."""
    expires_at: str | None
    """Cuándo deja de servir la liga. Pida otra cuando quiera."""
    created_at: str | None
    """Cuándo se creó."""


class WebhookEndpoint(TypedDict):
    """Una dirección de su servidor que recibe eventos."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    object: Literal["webhook_endpoint"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    sandbox: str | None
    """El entorno de prueba (sbx_…) al que pertenece, o null si es de la cuenta. Vea /v1/sandboxes."""
    url: str
    """Dirección https de su servidor que recibe los avisos."""
    description: str | None
    """Para qué es, para usted."""
    events: list[str]
    """Eventos que quiere recibir, o ["*"] para todos (por omisión). La lista con cuándo llega cada uno: [Tipos de evento](https://fiscalisto.com/docs/api/webhooks#tipos-de-evento)."""
    status: Literal["enabled", "failing", "disabled"]
    """enabled: entregando. failing: sus entregas fallan (se apaga tras 5 días así). disabled: apagado."""
    disabled_reason: NotRequired[str | None]
    """Por qué se apagó (sus entregas fallaron 5 días seguidos, o usted lo apagó)."""
    failing_since: NotRequired[str | None]
    """Desde cuándo fallan las entregas, o null."""
    previous_secret_expires_at: str | None
    """Hasta cuándo el secreto anterior también firma (después de cambiarlo), o null."""
    api_version: str | None
    """La versión de la API de sus eventos; null: la de la cuenta."""
    created_at: str | None
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    secret: NotRequired[str]
    """Secreto de firma (whsec_…). Solo viene al crearlo o al cambiarlo: guárdelo para verificar las firmas."""


class WebhookTestDelivery(TypedDict):
    """Cómo le fue: ok si contestó 2xx, el código, el error y el inicio de su respuesta."""
    ok: bool
    """true si su servidor contestó 2xx."""
    status: int | None
    """El código HTTP que contestó; null si no se pudo conectar."""
    error: str | None
    """Qué falló (sin respuesta, no se pudo conectar, otro código), o null."""
    response_body: str | None
    """El inicio de lo que contestó su servidor (hasta 2,000 caracteres)."""
    duration_ms: int
    """Cuánto tardó su servidor, en milisegundos."""


class WebhookTest(TypedDict):
    """Un evento de prueba que se mandó a su webhook, y lo que respondió su servidor."""
    object: Literal["webhook_test"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    event: Event
    """El evento que se mandó, como lo recibió su servidor."""
    delivery: WebhookTestDelivery
    """Cómo le fue: ok si contestó 2xx, el código, el error y el inicio de su respuesta."""


EventType = Literal["invoice.stamped", "invoice.failed", "invoice.canceled", "invoice.cancellation_pending", "invoice.cancellation_rejected", "invoice.paid", "invoice.partially_paid", "invoice.email_bounced", "invoice.email_complained", "retention.stamped", "retention.failed", "retention.canceled", "invoice_batch.completed", "payroll_batch.completed", "customer_data_request.completed", "sat_download.completed", "sat_download.failed", "sat_declaration.created", "sat_declaration.updated", "ticket.invoiced", "ticket.included_in_global", "recurring_invoice.failed", "quote.viewed", "quote.accepted", "quote.changes_requested", "quote.rejected", "quote.withdrawn", "sales_order.confirmed", "sales_order.customer_confirmed", "sales_order.delivered", "sales_order.paid", "sales_order.canceled", "supplier_invoice.received", "supplier_invoice.approved", "supplier_invoice.rejected", "supplier_invoice.scheduled", "supplier_invoice.paid", "portal_supplier.approved", "issuer.ready", "balance.low", "usage.high", "test_clock.ready"]
"""Lo que puede pasar: el tipo de cada evento."""


class InvoiceEventData(TypedDict):
    object: Invoice
    """El objeto como quedó: el comprobante completo, como lo contesta su GET."""


class RetentionEventData(TypedDict):
    object: Retention
    """El objeto como quedó: la constancia completo, como lo contesta su GET."""


class InvoiceBatchEventData(TypedDict):
    object: InvoiceBatch
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class PayrollBatchEventData(TypedDict):
    object: PayrollBatch
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class CustomerDataRequestEventData(TypedDict):
    object: CustomerDataRequest
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class SatDownloadEventData(TypedDict):
    object: SatDownload
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class SatDeclarationEventData(TypedDict):
    object: SatDeclaration
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class TicketEventData(TypedDict):
    object: Ticket
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class RecurringInvoiceEventData(TypedDict):
    object: RecurringInvoice
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class QuoteEventData(TypedDict):
    object: Quote
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class SalesOrderEventData(TypedDict):
    object: SalesOrder
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class SupplierInvoiceEventData(TypedDict):
    object: SupplierInvoice
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class PortalSupplierEventData(TypedDict):
    object: PortalSupplier
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class IssuerEventData(TypedDict):
    object: Issuer
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class BalanceEventData(TypedDict):
    object: Balance
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class UsageEventData(TypedDict):
    object: Usage
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class TestClockEventData(TypedDict):
    object: TestClock
    """El objeto como quedó: el lote completo, como lo contesta su GET."""


class InvoiceStampedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.stamped"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoiceFailedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.failed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoiceCanceledEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.canceled"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoiceCancellationPendingEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.cancellation_pending"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoiceCancellationRejectedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.cancellation_rejected"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoicePaidEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.paid"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoicePartiallyPaidEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.partially_paid"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoiceEmailBouncedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.email_bounced"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class InvoiceEmailComplainedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice.email_complained"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceEventData


class RetentionStampedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["retention.stamped"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: RetentionEventData


class RetentionFailedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["retention.failed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: RetentionEventData


class RetentionCanceledEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["retention.canceled"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: RetentionEventData


class InvoiceBatchCompletedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["invoice_batch.completed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: InvoiceBatchEventData


class PayrollBatchCompletedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["payroll_batch.completed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: PayrollBatchEventData


class CustomerDataRequestCompletedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["customer_data_request.completed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: CustomerDataRequestEventData


class SatDownloadCompletedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["sat_download.completed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SatDownloadEventData


class SatDownloadFailedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["sat_download.failed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SatDownloadEventData


class SatDeclarationCreatedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["sat_declaration.created"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SatDeclarationEventData


class SatDeclarationUpdatedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["sat_declaration.updated"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SatDeclarationEventData


class TicketInvoicedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["ticket.invoiced"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: TicketEventData


class TicketIncludedInGlobalEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["ticket.included_in_global"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: TicketEventData


class RecurringInvoiceFailedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["recurring_invoice.failed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: RecurringInvoiceEventData


class QuoteViewedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["quote.viewed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: QuoteEventData


class QuoteAcceptedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["quote.accepted"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: QuoteEventData


class QuoteChangesRequestedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["quote.changes_requested"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: QuoteEventData


class QuoteRejectedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["quote.rejected"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: QuoteEventData


class QuoteWithdrawnEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["quote.withdrawn"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: QuoteEventData


class SalesOrderConfirmedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["sales_order.confirmed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SalesOrderEventData


class SalesOrderCustomerConfirmedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["sales_order.customer_confirmed"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SalesOrderEventData


class SalesOrderDeliveredEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["sales_order.delivered"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SalesOrderEventData


class SalesOrderPaidEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["sales_order.paid"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SalesOrderEventData


class SalesOrderCanceledEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["sales_order.canceled"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SalesOrderEventData


class SupplierInvoiceReceivedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["supplier_invoice.received"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SupplierInvoiceEventData


class SupplierInvoiceApprovedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["supplier_invoice.approved"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SupplierInvoiceEventData


class SupplierInvoiceRejectedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["supplier_invoice.rejected"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SupplierInvoiceEventData


class SupplierInvoiceScheduledEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["supplier_invoice.scheduled"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SupplierInvoiceEventData


class SupplierInvoicePaidEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["supplier_invoice.paid"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: SupplierInvoiceEventData


class PortalSupplierApprovedEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["portal_supplier.approved"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: PortalSupplierEventData


class IssuerReadyEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["issuer.ready"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: IssuerEventData


class BalanceLowEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["balance.low"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: BalanceEventData


class UsageHighEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["usage.high"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: UsageEventData


class TestClockReadyEvent(TypedDict):
    """Algo que pasó en su cuenta: el objeto completo como quedó. Se manda a sus webhooks firmado (Standard Webhooks)."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: Literal["event"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    type: Literal["test_clock.ready"]
    """Qué pasó: invoice.stamped, invoice.failed, invoice.canceled, invoice.cancellation_pending, invoice.cancellation_rejected, invoice.paid, invoice.partially_paid, retention.stamped, retention.failed, retention.canceled, invoice_batch.completed, payroll_batch.completed, customer_data_request.completed, sat_download.completed, sat_download.failed, sat_declaration.created, sat_declaration.updated, ticket.invoiced, ticket.included_in_global, recurring_invoice.failed, quote.viewed, quote.accepted, quote.changes_requested, quote.rejected, quote.withdrawn, sales_order.confirmed, sales_order.customer_confirmed, sales_order.delivered, sales_order.paid, sales_order.canceled, supplier_invoice.received, supplier_invoice.approved, supplier_invoice.rejected, supplier_invoice.scheduled, supplier_invoice.paid, portal_supplier.approved, issuer.ready, balance.low, usage.high o test_clock.ready."""
    api_version: str
    """Versión de la API con que se armó el objeto."""
    livemode: bool
    """true en producción (llaves fk_live_), false en pruebas (fk_test_). Lo de pruebas no vale ante el SAT."""
    created_at: str
    """Cuándo se creó, ISO 8601 con la hora de la Ciudad de México (-06:00)."""
    data: TestClockEventData


Event = Union[
    InvoiceStampedEvent,
    InvoiceFailedEvent,
    InvoiceCanceledEvent,
    InvoiceCancellationPendingEvent,
    InvoiceCancellationRejectedEvent,
    InvoicePaidEvent,
    InvoicePartiallyPaidEvent,
    InvoiceEmailBouncedEvent,
    InvoiceEmailComplainedEvent,
    RetentionStampedEvent,
    RetentionFailedEvent,
    RetentionCanceledEvent,
    InvoiceBatchCompletedEvent,
    PayrollBatchCompletedEvent,
    CustomerDataRequestCompletedEvent,
    SatDownloadCompletedEvent,
    SatDownloadFailedEvent,
    SatDeclarationCreatedEvent,
    SatDeclarationUpdatedEvent,
    TicketInvoicedEvent,
    TicketIncludedInGlobalEvent,
    RecurringInvoiceFailedEvent,
    QuoteViewedEvent,
    QuoteAcceptedEvent,
    QuoteChangesRequestedEvent,
    QuoteRejectedEvent,
    QuoteWithdrawnEvent,
    SalesOrderConfirmedEvent,
    SalesOrderCustomerConfirmedEvent,
    SalesOrderDeliveredEvent,
    SalesOrderPaidEvent,
    SalesOrderCanceledEvent,
    SupplierInvoiceReceivedEvent,
    SupplierInvoiceApprovedEvent,
    SupplierInvoiceRejectedEvent,
    SupplierInvoiceScheduledEvent,
    SupplierInvoicePaidEvent,
    PortalSupplierApprovedEvent,
    IssuerReadyEvent,
    BalanceLowEvent,
    UsageHighEvent,
    TestClockReadyEvent,
]
"""Un evento: según su type, data.object es la factura, la constancia o el lote."""


class Deleted(TypedDict):
    """Confirmación de que se borró."""
    id: str
    """Identificador del objeto, con su prefijo (iss_, inv_, ret_, cus_, prd_, emp_, bat_, brn_, whs_, stm_, adj_, evt_, whe_)."""
    object: str
    """Qué tipo de objeto es («invoice», «customer»…)."""
    deleted: Literal[True]
    """Siempre true."""


class ApiErrorError(TypedDict):
    """El error: type, code, message (en el idioma pedido), param (el campo a corregir), doc_url y request_id."""
    type: Literal["invalid_request_error", "authentication_error", "permission_error", "not_found_error", "idempotency_error", "rate_limit_error", "invoice_error", "balance_error", "api_error"]
    """La familia del error: invalid_request_error, authentication_error, permission_error, not_found_error, idempotency_error, rate_limit_error, invoice_error, balance_error o api_error."""
    code: str
    """La razón precisa, estable (ver Errores)."""
    message: str
    """Qué pasó y cómo corregirlo, para una persona."""
    param: NotRequired[str]
    """El campo con el problema (items.0.unit_price)."""
    sat_code: NotRequired[str]
    """Código del SAT o del PAC (CFDI40xxx)."""
    message_es: NotRequired[str]
    """Con Accept-Language: en, el mensaje original en español cuando message solo dice en inglés qué significa el código."""
    doc_url: str
    """La explicación de este código en la documentación."""
    request_id: str
    """El id de la solicitud (req_…). Inclúyalo si nos escribe."""


class ApiError(TypedDict):
    """Todos los errores tienen esta forma."""
    error: ApiErrorError
    """El error: type, code, message (en el idioma pedido), param (el campo a corregir), doc_url y request_id."""


class SandboxList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Sandbox]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class IssuerList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Issuer]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class InvoiceList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Invoice]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class ReceivableList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Receivable]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class BankTransactionList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[BankTransaction]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class PurchaseReceiptList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[PurchaseReceipt]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class AdvanceList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Advance]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class RetentionList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Retention]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class EmployeeList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Employee]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class PayrollBatchList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[PayrollBatch]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class ImssMovementList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[ImssMovement]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class InvoiceBatchList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[InvoiceBatch]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class BranchList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Branch]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class CostCenterList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[CostCenter]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class PriceListList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[PriceList]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class CustomerGroupList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[CustomerGroup]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class ExpensePersonList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[ExpensePerson]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class ExpenseReportList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[ExpenseReport]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class CustomerList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Customer]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class CustomerDataRequestList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[CustomerDataRequest]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class ProductList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Product]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatMailboxMessageList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatMailboxMessage]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatFindingList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatFinding]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatFindingCounterpartyList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatFindingCounterparty]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class WarehouseList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Warehouse]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class StockLevelList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[StockLevel]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class StockMovementList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[StockMovement]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class StockAdjustmentList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[StockAdjustment]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatCatalogEntryList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatCatalogEntry]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatListCheckList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatListCheck]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatDownloadList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatDownload]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatInvoiceList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatInvoice]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatRetentionList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatRetention]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class PortalSupplierList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[PortalSupplier]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SupplierInvoiceList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SupplierInvoice]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SatDeclarationList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SatDeclaration]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class TicketList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Ticket]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class JournalEntryList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[JournalEntry]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class LedgerAccountList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[LedgerAccount]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class StoreConnectionList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[StoreConnection]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class RecurringInvoiceList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[RecurringInvoice]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class QuoteList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Quote]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class SalesOrderList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[SalesOrder]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class WebhookEndpointList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[WebhookEndpoint]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class EventList(TypedDict):
    object: Literal["list"]
    """Qué tipo de objeto es («invoice», «customer»…)."""
    data: list[Event]
    """Los objetos de esta página."""
    has_more: bool
    """true si hay más: pida la siguiente con starting_after igual al id del último."""
    url: str
    """La ruta de esta lista."""


class InvoiceCreateCustomerForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class InvoiceCreateCustomer(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal del cliente (DomicilioFiscalReceptor), 5 dígitos."""
    email: NotRequired[str | None]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    foreign: NotRequired[InvoiceCreateCustomerForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class InvoiceCreateItemsItemThirdParty(TypedDict):
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    tax_id: str
    """RFC de a cuenta de quién (RfcACuentaTerceros)."""
    name: str
    """Nombre (NombreACuentaTerceros)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscalACuentaTerceros), c_RegimenFiscal."""
    zip: str
    """Código postal de su domicilio fiscal (DomicilioFiscalACuentaTerceros)."""


class InvoiceCreateItemsItemIedu(TypedDict):
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    student_name: str
    """Nombre del alumno (nombreAlumno)."""
    curp: str
    """CURP, 18 caracteres."""
    level: Literal["Preescolar", "Primaria", "Secundaria", "Profesional técnico", "Bachillerato o su equivalente"]
    """Nivel educativo (nivelEducativo)."""
    rvoe: str
    """Reconocimiento de validez oficial de estudios (autRVOE)."""
    payer_tax_id: NotRequired[str | None]
    """RFC de quien paga, si no es el receptor (rfcPago)."""


class InvoiceCreateItemsItemUsedVehicleCustomsItem(TypedDict):
    number: str
    """Número del documento de importación (numero)."""
    date: str
    """Fecha del documento (fecha), AAAA-MM-DD."""
    office: NotRequired[str]
    """Aduana (aduana)."""


class InvoiceCreateItemsItemUsedVehicle(TypedDict):
    """Complemento de vehículo usado."""
    purchase_amount: float
    """Monto de adquisición (montoAdquisicion)."""
    sale_amount: float
    """Monto de enajenación (montoEnajenacion)."""
    vehicle_key: str
    """Clave vehicular (claveVehicular)."""
    make: str
    """Marca (marca)."""
    type: str
    """Tipo o versión (tipo)."""
    model: str
    """Año del modelo (modelo), 4 dígitos."""
    engine_number: NotRequired[str]
    """Número de motor (numeroMotor)."""
    serial_number: NotRequired[str]
    """Número de serie (numeroSerie)."""
    niv: NotRequired[str]
    """Número de identificación vehicular (NIV)."""
    guide_value: float
    """Valor según la guía EBC o Libro Azul (valor)."""
    customs: NotRequired[list[InvoiceCreateItemsItemUsedVehicleCustomsItem]]
    """Información aduanera de la importación del vehículo (InformacionAduanera)."""


class InvoiceCreateItemsItem(TypedDict):
    """Un concepto. description, product_key y unit_price son obligatorios, salvo que mande product (prd_…): entonces vienen de su catálogo y lo que mande encima gana."""
    product: NotRequired[str]
    """Un producto de su catálogo (prd_…): toma su clave, unidad, precio e impuestos."""
    description: NotRequired[str]
    """Descripción del concepto (Descripcion), hasta 1,000 caracteres."""
    product_key: NotRequired[str]
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: NotRequired[str | None]
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: NotRequired[str | None]
    """Número de identificación o SKU (NoIdentificacion)."""
    quantity: NotRequired[float]
    """Cantidad (Cantidad). Por omisión 1."""
    unit_price: NotRequired[float]
    """Precio unitario antes de impuestos (ValorUnitario)."""
    discount: NotRequired[float]
    """Descuento (Descuento)."""
    taxability: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: NotRequired[float]
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: NotRequired[Literal["Tasa", "Cuota"]]
    """Tasa o Cuota (TipoFactor del IEPS)."""
    ieps_units: NotRequired[float]
    """Unidades de IEPS a cuota (litros, cigarros…), si no son la cantidad."""
    iva_retention: NotRequired[float]
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: NotRequired[float]
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""
    predial: NotRequired[list[str]]
    """Números de cuenta predial (CuentaPredial) en arrendamiento."""
    pedimentos: NotRequired[list[str]]
    """Números de pedimento (InformacionAduanera) de mercancía importada."""
    third_party: NotRequired[InvoiceCreateItemsItemThirdParty]
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    iedu: NotRequired[InvoiceCreateItemsItemIedu]
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    used_vehicle: NotRequired[InvoiceCreateItemsItemUsedVehicle]
    """Complemento de vehículo usado."""
    addenda: NotRequired[dict[str, str]]
    """Addenda del receptor (Walmart, Soriana…), con sus propios campos."""


class InvoiceCreateCartaPorteInternational(TypedDict):
    """Transporte internacional (TranspInternac Sí): entrada o salida, país, vía y regímenes aduaneros."""
    direction: Literal["Entrada", "Salida"]
    """EntradaSalidaMerc: Entrada o Salida."""
    country: str
    """País de origen o destino (PaisOrigenDestino), c_Pais."""
    via: str
    """Vía de entrada o salida (ViaEntradaSalida), c_CveTransporte (05 ducto incluido)."""
    regimes: list[str]
    """Regímenes aduaneros (RegimenAduanero), c_RegimenAduanero."""


class InvoiceCreateCartaPorteIstmo(TypedDict):
    """Corredor Interoceánico del Istmo de Tehuantepec: polos de origen y destino (c_RegistroISTMO)."""
    origin: str
    """Polo de origen (UbicacionPoloOrigen)."""
    destination: str
    """Polo de destino (UbicacionPoloDestino)."""


class InvoiceCreateCartaPorteOriginForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""


class InvoiceCreateCartaPorteOriginStation(TypedDict):
    """Estación, puerto o aeropuerto (TipoEstacion y NumEstacion de c_Estaciones). Solo sin autotransporte."""
    type: NotRequired[str]
    """Tipo de estación (TipoEstacion): 01 origen, 02 intermedia, 03 destino final."""
    number: NotRequired[str]
    """Clave de la estación, puerto o aeropuerto (NumEstacion), c_Estaciones."""
    name: NotRequired[str]
    """Nombre de la estación (NombreEstacion)."""
    foreign: NotRequired[bool]
    """true si la estación está en el extranjero (va sin TipoEstacion)."""


class InvoiceCreateCartaPorteOriginAddress(TypedDict):
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""
    street: NotRequired[str]
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    zip: str
    """Código postal (CodigoPostal). En México se deducen de él estado, municipio y localidad."""
    country: NotRequired[str]
    """País (Pais), c_Pais. Por omisión MEX."""
    state: NotRequired[str]
    """Estado (Estado): en el extranjero c_Estado para USA y CAN, o texto."""
    municipality: NotRequired[str]
    """Municipio (Municipio), en el extranjero como texto."""
    locality: NotRequired[str]
    """Localidad (Localidad), en el extranjero como texto."""
    colony: NotRequired[str]
    """Colonia (Colonia), en el extranjero como texto."""


class InvoiceCreateCartaPorteOrigin(TypedDict):
    """Ubicación de origen (Ubicacion TipoUbicacion Origen): remitente, fecha y hora de salida y domicilio."""
    tax_id: str
    """RFC del remitente (RFCRemitenteDestinatario); XEXX010101000 si es extranjero."""
    name: NotRequired[str]
    """Nombre del remitente (NombreRemitenteDestinatario)."""
    foreign: NotRequired[InvoiceCreateCartaPorteOriginForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    date_time: str
    """Fecha y hora de salida (origen) o llegada (destino), AAAA-MM-DDTHH:MM, hora local."""
    distance_km: NotRequired[float]
    """Distancia recorrida desde la ubicación anterior, en km (DistanciaRecorrida). Autotransporte y ferroviario."""
    station: NotRequired[InvoiceCreateCartaPorteOriginStation]
    """Estación, puerto o aeropuerto (TipoEstacion y NumEstacion de c_Estaciones). Solo sin autotransporte."""
    navigation: NotRequired[Literal["Altura", "Cabotaje"]]
    """Marítimo: tipo de tráfico (NavegacionTrafico), Altura o Cabotaje."""
    address: InvoiceCreateCartaPorteOriginAddress
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""


class InvoiceCreateCartaPorteDestinationsItemForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""


class InvoiceCreateCartaPorteDestinationsItemStation(TypedDict):
    """Estación, puerto o aeropuerto (TipoEstacion y NumEstacion de c_Estaciones). Solo sin autotransporte."""
    type: NotRequired[str]
    """Tipo de estación (TipoEstacion): 01 origen, 02 intermedia, 03 destino final."""
    number: NotRequired[str]
    """Clave de la estación, puerto o aeropuerto (NumEstacion), c_Estaciones."""
    name: NotRequired[str]
    """Nombre de la estación (NombreEstacion)."""
    foreign: NotRequired[bool]
    """true si la estación está en el extranjero (va sin TipoEstacion)."""


class InvoiceCreateCartaPorteDestinationsItemAddress(TypedDict):
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""
    street: NotRequired[str]
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    zip: str
    """Código postal (CodigoPostal). En México se deducen de él estado, municipio y localidad."""
    country: NotRequired[str]
    """País (Pais), c_Pais. Por omisión MEX."""
    state: NotRequired[str]
    """Estado (Estado): en el extranjero c_Estado para USA y CAN, o texto."""
    municipality: NotRequired[str]
    """Municipio (Municipio), en el extranjero como texto."""
    locality: NotRequired[str]
    """Localidad (Localidad), en el extranjero como texto."""
    colony: NotRequired[str]
    """Colonia (Colonia), en el extranjero como texto."""


class InvoiceCreateCartaPorteDestinationsItem(TypedDict):
    tax_id: str
    """RFC del destinatario (RFCRemitenteDestinatario); XEXX010101000 si es extranjero."""
    name: NotRequired[str]
    """Nombre del destinatario (NombreRemitenteDestinatario)."""
    foreign: NotRequired[InvoiceCreateCartaPorteDestinationsItemForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    date_time: str
    """Fecha y hora de salida (origen) o llegada (destino), AAAA-MM-DDTHH:MM, hora local."""
    distance_km: NotRequired[float]
    """Distancia recorrida desde la ubicación anterior, en km (DistanciaRecorrida). Autotransporte y ferroviario."""
    station: NotRequired[InvoiceCreateCartaPorteDestinationsItemStation]
    """Estación, puerto o aeropuerto (TipoEstacion y NumEstacion de c_Estaciones). Solo sin autotransporte."""
    navigation: NotRequired[Literal["Altura", "Cabotaje"]]
    """Marítimo: tipo de tráfico (NavegacionTrafico), Altura o Cabotaje."""
    address: InvoiceCreateCartaPorteDestinationsItemAddress
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""


class InvoiceCreateCartaPorteGoodsItemHazmat(TypedDict):
    """Material peligroso (MaterialPeligroso Sí): clave UN y embalaje."""
    key: str
    """Clave del material peligroso (CveMaterialPeligroso), c_MaterialPeligroso (número UN)."""
    packaging: str
    """Tipo de embalaje (Embalaje), c_TipoEmbalaje."""
    packaging_description: NotRequired[str]
    """Descripción del embalaje (DescripEmbalaje)."""


class InvoiceCreateCartaPorteGoodsItemCofepris(TypedDict):
    """Datos COFEPRIS de la mercancía: sector y lo que pide cada uno (medicamentos, precursores, psicotrópicos, sustancias tóxicas, plaguicidas)."""
    sector: str
    """Sector COFEPRIS (SectorCOFEPRIS): 01 medicamento, 02 precursores y químicos de uso dual, 03 psicotrópicos y estupefacientes, 04 sustancias tóxicas, 05 plaguicidas y fertilizantes."""
    active_ingredient: NotRequired[str]
    """Nombre del ingrediente activo (NombreIngredienteActivo)."""
    chemical_name: NotRequired[str]
    """Nombre químico (NomQuimico)."""
    generic_name: NotRequired[str]
    """Denominación genérica del producto (DenominacionGenericaProd)."""
    brand_name: NotRequired[str]
    """Denominación distintiva o marca (DenominacionDistintivaProd)."""
    manufacturer: NotRequired[str]
    """Fabricante (Fabricante)."""
    expiry: NotRequired[str]
    """Fecha de caducidad (FechaCaducidad), AAAA-MM-DD."""
    lot: NotRequired[str]
    """Lote del medicamento (LoteMedicamento)."""
    form: NotRequired[str]
    """Forma farmacéutica (FormaFarmaceutica), c_FormaFarmaceutica."""
    conditions: NotRequired[str]
    """Condiciones especiales de transporte (CondicionesEspTransp), c_CondicionesEspeciales."""
    sanitary_registry: NotRequired[str]
    """Registro sanitario o folio de autorización (RegistroSanitarioFolioAutorizacion)."""
    import_permit: NotRequired[str]
    """Permiso de importación (PermisoImportacion)."""
    vucem_folio: NotRequired[str]
    """Folio de importación VUCEM (FolioImpoVUCEM)."""
    cas: NotRequired[str]
    """Número CAS de la sustancia (NumCAS)."""
    importer: NotRequired[str]
    """Razón social de la empresa importadora (RazonSocialEmpImp)."""
    pesticide_registry: NotRequired[str]
    """Registro sanitario de plaguicidas COFEPRIS (NumRegSanPlagCOFEPRIS)."""
    manufacturer_data: NotRequired[str]
    """Datos del fabricante (DatosFabricante)."""
    formulator_data: NotRequired[str]
    """Datos del formulador (DatosFormulador)."""
    maquilador_data: NotRequired[str]
    """Datos del maquilador (DatosMaquilador)."""
    authorized_use: NotRequired[str]
    """Uso autorizado (UsoAutorizado)."""


class InvoiceCreateCartaPorteGoodsItemMaterial(TypedDict):
    """Tipo de materia (TipoMateria, c_TipoMateria) y su descripción si es «otra»."""
    type: str
    """Tipo de materia (TipoMateria), c_TipoMateria."""
    description: NotRequired[str]
    """Descripción de la materia (DescripcionMateria), con el tipo 05 otra."""


class InvoiceCreateCartaPorteGoodsItemCustomsDocsItem(TypedDict):
    type: str
    """Tipo de documento (TipoDocumento), c_DocumentoAduanero: 01 pedimento…"""
    pedimento: NotRequired[str]
    """Número de pedimento (NumPedimento), con el formato «NN  NN  NNNN  NNNNNNN». Solo con el tipo 01."""
    doc_id: NotRequired[str]
    """Identificador del documento aduanero (IdentDocAduanero), con un tipo distinto de 01."""
    importer_tax_id: NotRequired[str]
    """RFC del importador (RFCImpo), con un pedimento."""


class InvoiceCreateCartaPorteGoodsItemGuidesItem(TypedDict):
    number: str
    """Número de guía (NumeroGuiaIdentificacion)."""
    description: str
    """Descripción del contenido (DescripGuiaIdentificacion)."""
    weight_kg: float
    """Peso en kilogramos (PesoEnKg)."""


class InvoiceCreateCartaPorteGoodsItemQuantitiesItem(TypedDict):
    quantity: float
    """Cantidad que va a ese destino."""
    destination: int
    """El destino, por su posición en destinations (desde 0)."""
    mode: NotRequired[Literal["01", "02", "03", "04"]]
    """Medio en que va esa cantidad (CvesTransporte), c_CveTransporte."""


class InvoiceCreateCartaPorteGoodsItemDetail(TypedDict):
    """Marítimo: detalle de la mercancía (DetalleMercancia): kilos netos, tara y piezas."""
    net_kg: float
    """Peso neto en kg (PesoNeto)."""
    tare_kg: float
    """Tara en kg (PesoTara)."""
    pieces: NotRequired[int]
    """Número de piezas (NumPiezas)."""


class InvoiceCreateCartaPorteGoodsItem(TypedDict):
    product_key: str
    """Clave del bien transportado (BienesTransp), c_ClaveProdServCP."""
    description: str
    """Descripción de la mercancía (Descripcion)."""
    quantity: float
    """Cantidad (Cantidad)."""
    unit_key: str
    """Clave de unidad (ClaveUnidad), c_ClaveUnidad."""
    weight_kg: float
    """Peso en kilogramos (PesoEnKg)."""
    dimensions: NotRequired[str]
    """Dimensiones (Dimensiones), como 30/40/30cm o en plg."""
    hazmat: NotRequired[InvoiceCreateCartaPorteGoodsItemHazmat]
    """Material peligroso (MaterialPeligroso Sí): clave UN y embalaje."""
    cofepris: NotRequired[InvoiceCreateCartaPorteGoodsItemCofepris]
    """Datos COFEPRIS de la mercancía: sector y lo que pide cada uno (medicamentos, precursores, psicotrópicos, sustancias tóxicas, plaguicidas)."""
    value: NotRequired[float]
    """Valor de la mercancía (ValorMercancia); obligatorio en transporte aéreo."""
    currency: NotRequired[str]
    """Moneda del valor de la mercancía (Moneda), c_Moneda."""
    tariff: NotRequired[str]
    """Fracción arancelaria (FraccionArancelaria), 10 dígitos. Transporte internacional."""
    cce_uuid: NotRequired[str]
    """UUID del CFDI con complemento de comercio exterior (UUIDComercioExt)."""
    material: NotRequired[InvoiceCreateCartaPorteGoodsItemMaterial]
    """Tipo de materia (TipoMateria, c_TipoMateria) y su descripción si es «otra»."""
    customs_docs: NotRequired[list[InvoiceCreateCartaPorteGoodsItemCustomsDocsItem]]
    """Documentación aduanera (DocumentacionAduanera) de la mercancía en transporte internacional."""
    guides: NotRequired[list[InvoiceCreateCartaPorteGoodsItemGuidesItem]]
    """Paquetería: guías de los paquetes o tarimas (GuiasIdentificacion)."""
    quantities: NotRequired[list[InvoiceCreateCartaPorteGoodsItemQuantitiesItem]]
    """Cuánto va a cada destino (CantidadTransporta), por destino."""
    detail: NotRequired[InvoiceCreateCartaPorteGoodsItemDetail]
    """Marítimo: detalle de la mercancía (DetalleMercancia): kilos netos, tara y piezas."""
    stcc: NotRequired[str]
    """Ferroviario: clave STCC (ClaveSTCC)."""


class InvoiceCreateCartaPorteVehicleTrailersItem(TypedDict):
    type: str
    """Subtipo de remolque (SubTipoRem), c_SubTipoRem."""
    plate: str
    """Placa del remolque (Placa)."""


class InvoiceCreateCartaPorteVehicle(TypedDict):
    """Autotransporte (Autotransporte): vehículo, permiso SCT, seguros y remolques."""
    config: str
    """Configuración vehicular (ConfigVehicular), c_ConfigAutotransporte: C2, T3S2…"""
    plate: str
    """Placa (PlacaVM), sin guiones ni espacios."""
    year: int
    """Año del modelo (AnioModeloVM)."""
    gross_weight: float
    """Peso bruto vehicular en toneladas (PesoBrutoVehicular)."""
    permit_type: str
    """Tipo de permiso SCT (PermSCT), c_TipoPermiso."""
    permit_number: str
    """Número de permiso SCT (NumPermisoSCT)."""
    insurer: str
    """Aseguradora de responsabilidad civil (AseguraRespCivil)."""
    policy: str
    """Póliza de responsabilidad civil (PolizaRespCivil)."""
    env_insurer: NotRequired[str]
    """Aseguradora de daños al medio ambiente (AseguraMedAmbiente); obligatoria con material peligroso."""
    env_policy: NotRequired[str]
    """Póliza de daños al medio ambiente (PolizaMedAmbiente)."""
    cargo_insurer: NotRequired[str]
    """Aseguradora de la carga (AseguraCarga)."""
    cargo_policy: NotRequired[str]
    """Póliza de la carga (PolizaCarga)."""
    premium: NotRequired[float]
    """Prima del seguro (PrimaSeguro)."""
    trailers: NotRequired[list[InvoiceCreateCartaPorteVehicleTrailersItem]]
    """Remolques o semirremolques (Remolque): tipo (c_SubTipoRem) y placa."""


class InvoiceCreateCartaPorteSeaContainersItemTrailersItem(TypedDict):
    type: str
    """Subtipo de remolque (SubTipoRem), c_SubTipoRem."""
    plate: str
    """Placa del remolque (Placa)."""


class InvoiceCreateCartaPorteSeaContainersItem(TypedDict):
    type: str
    """Tipo de contenedor (TipoContenedor), c_ContenedorMaritimo o c_Contenedor en ferroviario."""
    registration: NotRequired[str]
    """Matrícula (Matricula)."""
    seal: NotRequired[str]
    """Número de precinto (NumPrecinto)."""
    related_id_ccp: NotRequired[str]
    """Ferri: el IdCCP de la Carta Porte del autotransporte a bordo (IdCCPRelacionado)."""
    truck_plate: NotRequired[str]
    """Ferri: placa del vehículo a bordo (PlacaVMCCP)."""
    certified_at: NotRequired[str]
    """Ferri: fecha de certificación de la Carta Porte del vehículo (FechaCertificacionCCP)."""
    trailers: NotRequired[list[InvoiceCreateCartaPorteSeaContainersItemTrailersItem]]
    """Remolques o semirremolques (Remolque): tipo (c_SubTipoRem) y placa."""


class InvoiceCreateCartaPorteSea(TypedDict):
    """Transporte marítimo (TransporteMaritimo): embarcación, naviero y contenedores."""
    permit_type: NotRequired[str]
    """Tipo de permiso SCT (PermSCT), c_TipoPermiso."""
    permit_number: NotRequired[str]
    """Número de permiso SCT (NumPermisoSCT)."""
    insurer: NotRequired[str]
    """Aseguradora de responsabilidad civil (AseguraRespCivil)."""
    policy: NotRequired[str]
    """Póliza de responsabilidad civil (PolizaRespCivil)."""
    vessel_type: str
    """Tipo de embarcación (TipoEmbarcacion), c_ConfigMaritima."""
    registration: str
    """Matrícula (Matricula)."""
    imo: str
    """Número IMO (NumeroOMI): IMO y 7 dígitos."""
    year: NotRequired[int]
    """Año de la embarcación (AnioEmbarcacion)."""
    vessel_name: NotRequired[str]
    """Nombre de la embarcación (NombreEmbarc)."""
    flag: str
    """Nacionalidad de la embarcación (NacionalidadEmbarc), c_Pais."""
    gross_tonnage: float
    """Unidades de arqueo bruto (UnidadesDeArqBruto)."""
    cargo_type: str
    """Tipo de carga (TipoCarga), c_ClaveTipoCarga."""
    length: NotRequired[float]
    """Eslora en metros (Eslora)."""
    beam: NotRequired[float]
    """Manga en metros (Manga)."""
    draft: NotRequired[float]
    """Calado en metros (Calado)."""
    depth: NotRequired[float]
    """Puntal en metros (Puntal)."""
    line: NotRequired[str]
    """Línea naviera (LineaNaviera)."""
    agent_name: str
    """Nombre del agente naviero consignatario (NombreAgenteNaviero)."""
    agent_authorization: str
    """Autorización del agente naviero (NumAutorizacionNaviero), c_NumAutorizacionNaviero."""
    voyage: NotRequired[str]
    """Número de viaje (NumViaje)."""
    bill_of_lading: NotRequired[str]
    """Número de conocimiento de embarque (NumConocEmbarc)."""
    temp_permit: NotRequired[str]
    """Permiso temporal de navegación (PermisoTempNavegacion), para una embarcación extranjera."""
    containers: NotRequired[list[InvoiceCreateCartaPorteSeaContainersItem]]
    """Contenedores (Contenedor)."""


class InvoiceCreateCartaPorteAirShipperForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""


class InvoiceCreateCartaPorteAirShipper(TypedDict):
    """Embarcador (RFCEmbarcador o NumRegIdTribEmbarc y ResidenciaFiscalEmbarc, NombreEmbarcador)."""
    tax_id: NotRequired[str]
    """RFC del embarcador (RFCEmbarcador)."""
    foreign: NotRequired[InvoiceCreateCartaPorteAirShipperForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    name: NotRequired[str]
    """Nombre del embarcador (NombreEmbarcador)."""


class InvoiceCreateCartaPorteAir(TypedDict):
    """Transporte aéreo (TransporteAereo): permiso, guía y transportista."""
    permit_type: str
    """Tipo de permiso SCT (PermSCT), c_TipoPermiso."""
    permit_number: str
    """Número de permiso SCT (NumPermisoSCT)."""
    aircraft: NotRequired[str]
    """Matrícula de la aeronave (MatriculaAeronave)."""
    insurer: NotRequired[str]
    """Aseguradora de responsabilidad civil (AseguraRespCivil)."""
    policy: NotRequired[str]
    """Póliza de responsabilidad civil (PolizaRespCivil)."""
    waybill: str
    """Número de guía aérea (NumeroGuia), de 12 a 15 caracteres."""
    contract_place: NotRequired[str]
    """Lugar del contrato (LugarContrato)."""
    carrier: str
    """Código del transportista (CodigoTransportista), c_CodigoTransporteAereo."""
    shipper: NotRequired[InvoiceCreateCartaPorteAirShipper]
    """Embarcador (RFCEmbarcador o NumRegIdTribEmbarc y ResidenciaFiscalEmbarc, NombreEmbarcador)."""
    rate_charge: NotRequired[float]
    """Cargo por tasación (CargoPorTasacion)."""


class InvoiceCreateCartaPorteRailRightsItem(TypedDict):
    type: str
    """Tipo de derecho de paso (TipoDerechoDePaso), c_DerechosDePaso."""
    km: float
    """Kilometraje pagado (KilometrajePagado)."""


class InvoiceCreateCartaPorteRailCarsItemContainersItem(TypedDict):
    type: str
    """Tipo de contenedor (TipoContenedor), c_ContenedorMaritimo o c_Contenedor en ferroviario."""
    empty_kg: float
    """Peso del contenedor vacío en kg (PesoContenedorVacio)."""
    net_kg: float
    """Peso neto en kg (PesoNeto)."""


class InvoiceCreateCartaPorteRailCarsItem(TypedDict):
    type: str
    """Tipo de carro (TipoCarro), c_TipoCarro."""
    registration: str
    """Matrícula (Matricula)."""
    guide: str
    """Guía del carro (GuiaCarro)."""
    net_tons: float
    """Toneladas netas del carro (ToneladasNetasCarro)."""
    containers: NotRequired[list[InvoiceCreateCartaPorteRailCarsItemContainersItem]]
    """Contenedores (Contenedor)."""


class InvoiceCreateCartaPorteRail(TypedDict):
    """Transporte ferroviario (TransporteFerroviario): servicio, tráfico, derechos de paso y carros."""
    service: str
    """Tipo de servicio (TipoDeServicio), c_TipoDeServicio."""
    traffic: str
    """Tipo de tráfico (TipoDeTrafico), c_TipoDeTrafico."""
    insurer: NotRequired[str]
    """Aseguradora de responsabilidad civil (AseguraRespCivil)."""
    policy: NotRequired[str]
    """Póliza de responsabilidad civil (PolizaRespCivil)."""
    rights: NotRequired[list[InvoiceCreateCartaPorteRailRightsItem]]
    """Derechos de paso (DerechosDePaso): tipo y kilómetros."""
    cars: list[InvoiceCreateCartaPorteRailCarsItem]
    """Carros (Carro)."""


class InvoiceCreateCartaPorteDriversItemForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""


class InvoiceCreateCartaPorteDriversItem(TypedDict):
    tax_id: str | Literal[""]
    """RFC del operador (RFCFigura); vacío si es extranjero (con foreign)."""
    license: str
    """Número de licencia (NumLicencia)."""
    name: str
    """Nombre del operador (NombreFigura)."""
    foreign: NotRequired[InvoiceCreateCartaPorteDriversItemForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""


class InvoiceCreateCartaPorteFiguresItemForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""


class InvoiceCreateCartaPorteFiguresItemAddress(TypedDict):
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""
    street: NotRequired[str]
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    zip: str
    """Código postal (CodigoPostal). En México se deducen de él estado, municipio y localidad."""
    country: NotRequired[str]
    """País (Pais), c_Pais. Por omisión MEX."""
    state: NotRequired[str]
    """Estado (Estado): en el extranjero c_Estado para USA y CAN, o texto."""
    municipality: NotRequired[str]
    """Municipio (Municipio), en el extranjero como texto."""
    locality: NotRequired[str]
    """Localidad (Localidad), en el extranjero como texto."""
    colony: NotRequired[str]
    """Colonia (Colonia), en el extranjero como texto."""


class InvoiceCreateCartaPorteFiguresItem(TypedDict):
    type: Literal["02", "03", "04", "05"]
    """Tipo de figura (TipoFigura): 02 propietario, 03 arrendador, 04 notificado, 05 integrante."""
    tax_id: NotRequired[str]
    """RFC de la figura (RFCFigura)."""
    foreign: NotRequired[InvoiceCreateCartaPorteFiguresItemForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    name: str
    """Nombre de la figura (NombreFigura)."""
    parts: NotRequired[list[str]]
    """Partes del transporte que posee o arrienda (ParteTransporte), c_ParteTransporte."""
    address: NotRequired[InvoiceCreateCartaPorteFiguresItemAddress]
    """Domicilio (Domicilio). En México basta el código postal: estado, municipio y localidad se toman de c_CodigoPostal."""


class InvoiceCreateCartaPorte(TypedDict):
    """Complemento Carta Porte 3.1 (traslado de mercancías)."""
    modes: NotRequired[list[Literal["01", "02", "03", "04"]]]
    """Cómo viajan las mercancías (c_CveTransporte): 01 autotransporte, 02 marítimo, 03 aéreo, 04 ferroviario; varios si es intermodal. Por omisión 01."""
    international: NotRequired[InvoiceCreateCartaPorteInternational]
    """Transporte internacional (TranspInternac Sí): entrada o salida, país, vía y regímenes aduaneros."""
    istmo: NotRequired[InvoiceCreateCartaPorteIstmo]
    """Corredor Interoceánico del Istmo de Tehuantepec: polos de origen y destino (c_RegistroISTMO)."""
    reverse_logistics: NotRequired[bool]
    """Autotransporte: true si es logística inversa, recolección o devolución."""
    origin: InvoiceCreateCartaPorteOrigin
    """Ubicación de origen (Ubicacion TipoUbicacion Origen): remitente, fecha y hora de salida y domicilio."""
    destinations: list[InvoiceCreateCartaPorteDestinationsItem]
    """Ubicaciones de destino (TipoUbicacion Destino), en orden: destinatario, llegada, distancia y domicilio."""
    goods: list[InvoiceCreateCartaPorteGoodsItem]
    """Mercancías (Mercancia) que se transportan."""
    vehicle: NotRequired[InvoiceCreateCartaPorteVehicle]
    """Autotransporte (Autotransporte): vehículo, permiso SCT, seguros y remolques."""
    sea: NotRequired[InvoiceCreateCartaPorteSea]
    """Transporte marítimo (TransporteMaritimo): embarcación, naviero y contenedores."""
    air: NotRequired[InvoiceCreateCartaPorteAir]
    """Transporte aéreo (TransporteAereo): permiso, guía y transportista."""
    rail: NotRequired[InvoiceCreateCartaPorteRail]
    """Transporte ferroviario (TransporteFerroviario): servicio, tráfico, derechos de paso y carros."""
    drivers: list[InvoiceCreateCartaPorteDriversItem]
    """Operadores (FiguraTransporte tipo 01): RFC, licencia y nombre."""
    figures: NotRequired[list[InvoiceCreateCartaPorteFiguresItem]]
    """Otras figuras de transporte: 02 propietario, 03 arrendador, 04 notificado, 05 integrante de coordinados."""


class InvoiceCreateIneEntitiesItem(TypedDict):
    key: str
    """Clave de la entidad (ClaveEntidad), 3 letras."""
    scope: NotRequired[Literal["Local", "Federal"]]
    """Ámbito (Ambito): Local o Federal."""
    accounting_ids: NotRequired[list[str]]
    """Claves de contabilidad (IdContabilidad)."""


class InvoiceCreateIne(TypedDict):
    """Complemento INE (procesos electorales)."""
    process: Literal["Ordinario", "Precampaña", "Campaña"]
    """Tipo de proceso (TipoProceso): Ordinario, Precampaña o Campaña."""
    committee: NotRequired[Literal["Ejecutivo Nacional", "Ejecutivo Estatal", "Directivo Estatal"]]
    """Tipo de comité (TipoComite), con el proceso Ordinario."""
    accounting_id: NotRequired[str]
    """Clave de contabilidad (IdContabilidad), hasta 6 dígitos."""
    entities: NotRequired[list[InvoiceCreateIneEntitiesItem]]
    """Entidades (Entidad): clave del estado, ámbito y claves de contabilidad."""


class InvoiceCreateLeyendasItem(TypedDict):
    text: str
    """Texto de la leyenda (textoLeyenda)."""
    disposition: NotRequired[str]
    """Disposición fiscal (disposicionFiscal), por ejemplo LISR."""
    norm: NotRequired[str]
    """Norma o artículo (norma)."""


class InvoiceCreateDonation(TypedDict):
    """Complemento de donatarias: un recibo de donativo. El emisor debe ser donataria (tax_system 603) con su oficio en donation_authorization (POST /v1/issuers/{id})."""
    in_kind: NotRequired[bool]
    """true si el donativo es en especie (bienes): va con forma de pago 12 (dación en pago) y un concepto por cada tipo de bien."""
    deducted: NotRequired[bool]
    """true si el donante ya había deducido los bienes que dona: el recibo dice que el donativo no es deducible."""


class InvoiceCreateLocalTaxesItem(TypedDict):
    retention: bool
    """true si es una retención local; false si es un traslado."""
    name: str
    """Nombre del impuesto local (ImpLocTrasladado o ImpLocRetenido), como ISH."""
    rate: float
    """Tasa en por ciento (TasadeTraslado o TasadeRetencion)."""
    amount: float
    """Importe del impuesto local."""


class InvoiceCreateComercioExteriorOwnersItem(TypedDict):
    tax_id: str
    """Número de registro tributario del propietario (NumRegIdTrib)."""
    country: str
    """País de residencia del propietario (ResidenciaFiscal), c_Pais."""


class InvoiceCreateComercioExteriorIssuerAddress(TypedDict):
    """Domicilio del emisor (Emisor Domicilio): calle y números; lo demás sale de su código postal."""
    street: str
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    zip: NotRequired[str]
    """Código postal del emisor (CodigoPostal)."""


class InvoiceCreateComercioExteriorReceiverAddress(TypedDict):
    """Domicilio del receptor en el extranjero (Receptor Domicilio)."""
    street: str
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    colony: NotRequired[str]
    """Colonia (Colonia), en el extranjero como texto."""
    locality: NotRequired[str]
    """Localidad (Localidad), en el extranjero como texto."""
    municipality: NotRequired[str]
    """Municipio (Municipio), en el extranjero como texto."""
    state: NotRequired[str]
    """Estado (Estado), c_Estado para USA y CAN."""
    country: str
    """País (Pais), c_Pais."""
    zip: str
    """Código postal en su país (CodigoPostal)."""


class InvoiceCreateComercioExteriorRecipientAddress(TypedDict):
    """Domicilio del destinatario (Domicilio)."""
    street: str
    """Calle (Calle)."""
    exterior: NotRequired[str]
    """Número exterior (NumeroExterior)."""
    interior: NotRequired[str]
    """Número interior (NumeroInterior)."""
    colony: NotRequired[str]
    """Colonia (Colonia), en el extranjero como texto."""
    locality: NotRequired[str]
    """Localidad (Localidad), en el extranjero como texto."""
    municipality: NotRequired[str]
    """Municipio (Municipio), en el extranjero como texto."""
    state: NotRequired[str]
    """Estado (Estado): en el extranjero c_Estado para USA y CAN, o texto."""
    country: str
    """País (Pais), c_Pais. Por omisión MEX."""
    zip: str
    """Código postal (CodigoPostal). En México se deducen de él estado, municipio y localidad."""


class InvoiceCreateComercioExteriorRecipient(TypedDict):
    """Destinatario, si no es el receptor (Destinatario)."""
    name: NotRequired[str]
    """Nombre del destinatario (Nombre)."""
    tax_id: NotRequired[str]
    """Número de registro tributario del destinatario (NumRegIdTrib)."""
    address: InvoiceCreateComercioExteriorRecipientAddress
    """Domicilio del destinatario (Domicilio)."""


class InvoiceCreateComercioExteriorGoodsItem(TypedDict):
    id: NotRequired[str]
    """Número de identificación de la mercancía (NoIdentificacion): el sku de su concepto."""
    tariff: NotRequired[str]
    """Fracción arancelaria (FraccionArancelaria), 10 dígitos con el NICO, vigente en c_FraccionArancelaria (búsquela en `GET /v1/sat_catalogs/customs_tariffs`); una que no lo esté se rechaza antes de timbrar."""
    unit: NotRequired[str]
    """Unidad aduana (UnidadAduana), c_UnidadAduana; 99 en un servicio. Con `tariff` puede omitirse: va la UMT de la fracción en el catálogo del SAT (otra la rechaza el SAT con CCE161)."""
    quantity: NotRequired[float]
    """Cantidad en la unidad aduana (CantidadAduana)."""
    unit_value_usd: NotRequired[float]
    """Valor unitario en dólares (ValorUnitarioAduana)."""


class InvoiceCreateComercioExterior(TypedDict):
    """Complemento de comercio exterior 2.0."""
    motive: NotRequired[Literal["05"]]
    """Motivo de traslado (MotivoTraslado): 05 envío de mercancías propias."""
    owners: NotRequired[list[InvoiceCreateComercioExteriorOwnersItem]]
    """Propietarios de la mercancía si no es el emisor (Propietario), con motive 05."""
    incoterm: NotRequired[str]
    """Incoterm (Incoterm), c_INCOTERM: EXW, FOB, CIF, DAP, DDP…"""
    certificate: NotRequired[str]
    """Número de certificado de origen (NumCertificadoOrigen)."""
    usd_rate: float
    """Tipo de cambio a dólares (TipoCambioUSD)."""
    issuer_curp: NotRequired[str]
    """CURP del emisor persona física (Emisor Curp)."""
    issuer_address: NotRequired[InvoiceCreateComercioExteriorIssuerAddress]
    """Domicilio del emisor (Emisor Domicilio): calle y números; lo demás sale de su código postal."""
    receiver_address: NotRequired[InvoiceCreateComercioExteriorReceiverAddress]
    """Domicilio del receptor en el extranjero (Receptor Domicilio)."""
    recipient: NotRequired[InvoiceCreateComercioExteriorRecipient]
    """Destinatario, si no es el receptor (Destinatario)."""
    goods: list[InvoiceCreateComercioExteriorGoodsItem]
    """Mercancías (Mercancia), una por concepto exportado."""
    notes: NotRequired[str]
    """Observaciones del complemento (Observaciones)."""


class InvoiceCreateGlobal(TypedDict):
    """Factura global a público en general (InformacionGlobal): periodicidad, meses y año."""
    periodicity: str
    """Periodicidad (Periodicidad), c_Periodicidad: 01 diario, 02 semanal, 03 quincenal, 04 mensual, 05 bimestral."""
    months: str
    """Meses (Meses), c_Meses: 01 a 12, o 13 a 18 bimestres."""
    year: int
    """Año (Año)."""


class InvoiceCreateAddenda(TypedDict):
    """Addenda del receptor (Walmart, Soriana…), con sus propios campos."""
    type: Literal["walmart", "soriana", "liverpool", "homedepot", "chedraui", "generic"]
    values: dict[str, str]
    customer: NotRequired[dict[str, str]]


class InvoiceCreateRelated(TypedDict):
    """CFDI relacionados (CfdiRelacionados): tipo de relación de c_TipoRelacion y los UUID."""
    relationship: str
    """Tipo de relación (TipoRelacion): 01 nota de crédito, 03 devolución, 04 sustitución, 07 anticipo…"""
    uuids: list[str]
    """Folios fiscales relacionados."""


# Una factura (CFDI 4.0). Un campo que no existe se rechaza con parameter_unknown, nunca se ignora.
InvoiceCreate = TypedDict(
    "InvoiceCreate",
    {
        "issuer": "NotRequired[str]",
        "branch": "NotRequired[str]",
        "cost_center": "NotRequired[str]",
        "warehouse": "NotRequired[str]",
        "customer": "str | InvoiceCreateCustomer",
        "items": "list[InvoiceCreateItemsItem]",
        "type": "NotRequired[Literal[\"I\", \"T\"]]",
        "carta_porte": "NotRequired[InvoiceCreateCartaPorte]",
        "ine": "NotRequired[InvoiceCreateIne]",
        "leyendas": "NotRequired[list[InvoiceCreateLeyendasItem]]",
        "donation": "NotRequired[InvoiceCreateDonation]",
        "local_taxes": "NotRequired[list[InvoiceCreateLocalTaxesItem]]",
        "export": "NotRequired[Literal[\"01\", \"02\", \"03\", \"04\"]]",
        "comercio_exterior": "NotRequired[InvoiceCreateComercioExterior]",
        "global": "NotRequired[InvoiceCreateGlobal]",
        "use": "NotRequired[str]",
        "payment_form": "NotRequired[str]",
        "payment_method": "NotRequired[Literal[\"PUE\", \"PPD\"]]",
        "paid_later": "NotRequired[bool]",
        "currency": "NotRequired[str]",
        "series": "NotRequired[str]",
        "notes": "NotRequired[str]",
        "pdf_language": "NotRequired[Literal[\"es\", \"en\", \"bi\"]]",
        "addenda": "NotRequired[InvoiceCreateAddenda]",
        "related": "NotRequired[InvoiceCreateRelated]",
        "exchange_rate": "NotRequired[float]",
        "folio": "NotRequired[int]",
        "continue_sequence": "NotRequired[bool]",
        "date": "NotRequired[str]",
        "send_email": "NotRequired[bool]",
        "email_cc": "NotRequired[str | None]",
        "metadata": "NotRequired[dict[str, str]]",
    },
)


class ExternalPayrollReceiptCreatePeriod(TypedDict):
    """FechaInicialPago, FechaFinalPago y FechaPago."""
    start: str
    """Primer día del periodo (FechaInicialPago), AAAA-MM-DD."""
    end: str
    """Último día del periodo (FechaFinalPago), AAAA-MM-DD."""
    payment_date: str
    """Fecha de pago (FechaPago), AAAA-MM-DD. Por omisión el último día del periodo."""


class ExternalPayrollReceiptCreateEmployerSncf(TypedDict):
    """EntidadSNCF, solo para entidades adheridas al SNCF."""
    resource_origin: str
    """OrigenRecurso: IP, IF o IM."""
    own_resource_amount: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""


class ExternalPayrollReceiptCreateEmployer(TypedDict):
    """El patrón (Emisor del complemento): registro patronal y CURP si es persona física."""
    registration: NotRequired[str | None]
    """Registro patronal. Sin el campo: el del emisor cuando el contrato es 01–08. null: sin registro patronal."""
    curp: NotRequired[str | None]
    """CURP del patrón persona física. Sin el campo: la guardada en el emisor."""
    origin_tax_id: NotRequired[str]
    """RfcPatronOrigen."""
    sncf: NotRequired[ExternalPayrollReceiptCreateEmployerSncf]
    """EntidadSNCF, solo para entidades adheridas al SNCF."""


class ExternalPayrollReceiptCreateEmployeeSubcontractingItem(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    percentage: float
    """PorcentajeTiempo."""


class ExternalPayrollReceiptCreateEmployee(TypedDict):
    """El empleado (Receptor y Nomina/Receptor) con los datos de su sistema de nómina; no usa ni cambia los empleados de Fiscalisto."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    name: str
    """Nombre."""
    zip: str
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    curp: str
    """CURP, 18 caracteres."""
    number: str
    """NumEmpleado."""
    email: NotRequired[str | None]
    """Para send_email; no va en el XML."""
    social_security_number: NotRequired[str]
    """Número de seguridad social (NumSeguridadSocial), 11 dígitos."""
    start_date: NotRequired[str]
    """FechaInicioRelLaboral."""
    seniority: NotRequired[str]
    """Antigüedad (P52W o P1Y2M3D). Sin el campo y con registro patronal: semanas desde start_date hasta el fin del periodo."""
    contract_type: str
    """Tipo de contrato (TipoContrato), c_TipoContrato. Por omisión 01, por tiempo indeterminado."""
    regime_type: str
    """Tipo de régimen (TipoRegimen): 02 sueldos y salarios."""
    unionized: NotRequired[bool]
    """true si es sindicalizado (Sindicalizado)."""
    workday_type: NotRequired[str]
    """Tipo de jornada (TipoJornada), c_TipoJornada. Por omisión 01, diurna."""
    risk_class: NotRequired[str]
    """Clase de riesgo del puesto ante el IMSS (RiesgoPuesto), 1 a 5. Por omisión 1."""
    department: NotRequired[str]
    """Departamento (Departamento)."""
    position: NotRequired[str]
    """Puesto (Puesto)."""
    contribution_base_salary: NotRequired[float]
    """SalarioBaseCotApor."""
    integrated_daily_salary: NotRequired[float]
    """SalarioDiarioIntegrado."""
    state: str
    """ClaveEntFed (c_Estado): JAL, CMX, NLE…"""
    bank: NotRequired[str]
    """Banco (c_Banco); no va con una CLABE."""
    bank_account: NotRequired[str]
    """CuentaBancaria: CLABE de 18 dígitos, tarjeta o cuenta."""
    subcontracting: NotRequired[list[ExternalPayrollReceiptCreateEmployeeSubcontractingItem]]
    """SubContratacion: el porcentaje suma 100."""


class ExternalPayrollReceiptCreatePerceptionsItemOvertimeItem(TypedDict):
    days: float
    """Días con horas extra (Dias)."""
    hours_type: str
    """c_TipoHoras: 01 dobles, 02 triples, 03 simples."""
    hours: float
    """Horas extra (HorasExtra)."""
    amount_paid: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""


class ExternalPayrollReceiptCreatePerceptionsItemStockOptions(TypedDict):
    """AccionesOTitulos: solo con la percepción 045."""
    market_value: float
    """Valor de mercado (ValorMercado)."""
    grant_price: float
    """Precio al otorgarse (PrecioAlOtorgarse)."""


class ExternalPayrollReceiptCreatePerceptionsItem(TypedDict):
    type: str
    """TipoPercepcion (c_TipoPercepcion): 001 sueldos, 002 aguinaldo…"""
    key: str
    """Clave del patrón (3 a 15 caracteres)."""
    concept: str
    """Concepto del pago (ConceptoPago), c_TipoContribuyenteSujetoRetencion."""
    taxed: float
    """ImporteGravado."""
    exempt: float
    """ImporteExento."""
    overtime: NotRequired[list[ExternalPayrollReceiptCreatePerceptionsItemOvertimeItem]]
    """HorasExtra: solo con la percepción 019."""
    stock_options: NotRequired[ExternalPayrollReceiptCreatePerceptionsItemStockOptions]
    """AccionesOTitulos: solo con la percepción 045."""


class ExternalPayrollReceiptCreateSeparation(TypedDict):
    """SeparacionIndemnizacion: con las percepciones 022, 023 o 025."""
    total_paid: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    years_of_service: float
    """NumAñosServicio."""
    last_monthly_salary: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    accumulable_income: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    non_accumulable_income: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""


class ExternalPayrollReceiptCreateRetirement(TypedDict):
    """JubilacionPensionRetiro: con las percepciones 039 o 044."""
    total_one_payment: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    total_installment: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    daily_amount: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    accumulable_income: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    non_accumulable_income: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""


class ExternalPayrollReceiptCreateDeductionsItem(TypedDict):
    type: str
    """TipoDeduccion (c_TipoDeduccion): 001 IMSS, 002 ISR, 010 Infonavit…"""
    key: str
    """El archivo .key en base64 (puede traer el prefijo data:)."""
    concept: str
    """Concepto de los egresos (IntegracEgresos/ConceptoS), hasta 100 caracteres."""
    amount: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""


class ExternalPayrollReceiptCreateOtherPaymentsItemBalanceCompensation(TypedDict):
    """CompensacionSaldosAFavor: solo con el 004."""
    balance: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    year: float
    """Año (Ejercicio)."""
    remaining: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""


class ExternalPayrollReceiptCreateOtherPaymentsItem(TypedDict):
    type: str
    """TipoOtroPago (c_TipoOtroPago): 002 subsidio para el empleo…"""
    key: str
    """El archivo .key en base64 (puede traer el prefijo data:)."""
    concept: str
    """Concepto del pago (ConceptoPago), c_TipoContribuyenteSujetoRetencion."""
    amount: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    subsidy_caused: NotRequired[float]
    """SubsidioCausado: solo con el 002."""
    balance_compensation: NotRequired[ExternalPayrollReceiptCreateOtherPaymentsItemBalanceCompensation]
    """CompensacionSaldosAFavor: solo con el 004."""


class ExternalPayrollReceiptCreateDisabilitiesItem(TypedDict):
    days: float
    """Días pagados (NumDiasPagados). Por omisión, todos los del periodo que le tocan."""
    type: str
    """Tipo de comprobante (TipoDeComprobante): I ingreso, E egreso, P pago, T traslado, N nómina."""
    amount: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""


class ExternalPayrollReceiptCreateTotals(TypedDict):
    """Los totales que calculó su sistema: Fiscalisto los compara al centavo con las líneas y rechaza el recibo si no cuadran."""
    perceptions: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    deductions: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    other_payments: float
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    net: float
    """Neto: percepciones más otros pagos menos deducciones."""
    salaries: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    separation: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    retirement: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    taxed: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    exempt: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    taxes_withheld: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""
    other_deductions: NotRequired[float]
    """Pesos con hasta 2 decimales, como se timbran: Fiscalisto no los redondea."""


class ExternalPayrollReceiptCreateReferences(TypedDict):
    """Sus ids: el empleado y la corrida de nómina. payroll_run_id es obligatorio en un recibo extraordinario."""
    employee_id: NotRequired[str]
    """El id del empleado en su sistema."""
    payroll_run_id: NotRequired[str]
    """El id de la corrida de nómina en su sistema."""


class ExternalPayrollReceiptCreate(TypedDict):
    """Un recibo de nómina que calculó su sistema, con todos sus conceptos e importes: se timbra tal cual."""
    issuer: NotRequired[str]
    """El emisor (patrón) del recibo; sin él, el único emisor de su cuenta en este modo."""
    type: Literal["O", "E"]
    """TipoNomina: O ordinaria (periodicidad 01–10) o E extraordinaria (periodicidad 99)."""
    periodicity: str
    """PeriodicidadPago (c_PeriodicidadPago)."""
    period: ExternalPayrollReceiptCreatePeriod
    """FechaInicialPago, FechaFinalPago y FechaPago."""
    days: float
    """NumDiasPagados: de 0.001 a 36160, hasta 3 decimales."""
    employer: NotRequired[ExternalPayrollReceiptCreateEmployer]
    """El patrón (Emisor del complemento): registro patronal y CURP si es persona física."""
    employee: ExternalPayrollReceiptCreateEmployee
    """El empleado (Receptor y Nomina/Receptor) con los datos de su sistema de nómina; no usa ni cambia los empleados de Fiscalisto."""
    perceptions: NotRequired[list[ExternalPayrollReceiptCreatePerceptionsItem]]
    """Percepciones (Percepcion): sueldo y demás, gravado y exento."""
    separation: NotRequired[ExternalPayrollReceiptCreateSeparation]
    """SeparacionIndemnizacion: con las percepciones 022, 023 o 025."""
    retirement: NotRequired[ExternalPayrollReceiptCreateRetirement]
    """JubilacionPensionRetiro: con las percepciones 039 o 044."""
    deductions: NotRequired[list[ExternalPayrollReceiptCreateDeductionsItem]]
    """Deducciones (Deduccion): ISR, cuotas IMSS y demás."""
    other_payments: NotRequired[list[ExternalPayrollReceiptCreateOtherPaymentsItem]]
    """Otros pagos (OtroPago): subsidio para el empleo."""
    disabilities: NotRequired[list[ExternalPayrollReceiptCreateDisabilitiesItem]]
    """Incapacidades: con la percepción 014 o la deducción 006."""
    totals: ExternalPayrollReceiptCreateTotals
    """Los totales que calculó su sistema: Fiscalisto los compara al centavo con las líneas y rechaza el recibo si no cuadran."""
    references: NotRequired[ExternalPayrollReceiptCreateReferences]
    """Sus ids: el empleado y la corrida de nómina. payroll_run_id es obligatorio en un recibo extraordinario."""
    replaces: NotRequired[str]
    """El recibo vigente (inv_… o UUID) que este sustituye: relación 04 y se cancela con motivo 01."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class UpdateAccountParams(TypedDict):
    api_version: str
    """La versión de la API de la cuenta: la que reciben sus solicitudes sin Fiscalisto-Version y sus webhooks sin api_version propio. Pruebe antes la nueva con el encabezado."""


class ResetTestDataParams(TypedDict):
    seed: NotRequired[bool]
    """true (por omisión) para dejarle a cada emisor de pruebas 2 clientes y 3 productos de ejemplo. false para dejarlo vacío."""


class CreateSandboxParams(TypedDict):
    name: str
    """Para quién o para qué es, por ejemplo el nombre de quien lo usa."""


class CreateTestClockParams(TypedDict):
    frozen_time: NotRequired[str]
    """Dónde empieza el reloj; si no la manda, ahora."""


class AdvanceTestClockParams(TypedDict):
    frozen_time: str
    """A dónde adelantarlo: después de la hora actual del reloj. Lo que toca en el camino se hace día por día."""


class CreateIssuerParamsDonationAuthorization(TypedDict):
    number: str
    """Número del oficio de autorización, hasta 100 caracteres."""
    date: str
    """Fecha del oficio, AAAA-MM-DD; no puede ser futura."""


class CreateIssuerParams(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    employer_registration: NotRequired[str | None]
    """Registro patronal ante el IMSS (RegistroPatronal), 11 caracteres. Necesario para timbrar nómina."""
    curp: NotRequired[str | None]
    """CURP, 18 caracteres."""
    donation_authorization: NotRequired[CreateIssuerParamsDonationAuthorization | None]
    """Donataria autorizada (régimen 603): el oficio del SAT que la autoriza a recibir donativos deducibles (o su renovación). Va en cada recibo de donativo (`donation` de POST /v1/invoices); null lo quita. El emisor debe tener tax_system 603. En pruebas sirve cualquier número y una fecha pasada."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class ListIssuersParams(TypedDict):
    """Los parámetros de GET /v1/issuers."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    tax_id: NotRequired[str]
    """Solo el de este RFC."""
    include_archived: NotRequired[bool]
    """true para incluir los archivados."""


class UpdateIssuerParamsDonationAuthorization(TypedDict):
    number: str
    """Número del oficio de autorización, hasta 100 caracteres."""
    date: str
    """Fecha del oficio, AAAA-MM-DD; no puede ser futura."""


class UpdateIssuerParams(TypedDict):
    legal_name: NotRequired[str]
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: NotRequired[str]
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    employer_registration: NotRequired[str | None]
    """Registro patronal ante el IMSS (RegistroPatronal), 11 caracteres. Necesario para timbrar nómina."""
    curp: NotRequired[str | None]
    """CURP, 18 caracteres."""
    donation_authorization: NotRequired[UpdateIssuerParamsDonationAuthorization | None]
    """Donataria autorizada (régimen 603): el oficio del SAT que la autoriza a recibir donativos deducibles (o su renovación). Va en cada recibo de donativo (`donation` de POST /v1/invoices); null lo quita. El emisor debe tener tax_system 603. En pruebas sirve cualquier número y una fecha pasada."""
    metadata: NotRequired[dict[str, str] | None]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class UploadCertificateParams(TypedDict):
    cer: str
    """El archivo .cer en base64 (puede traer el prefijo data:)."""
    key: str
    """El archivo .key en base64 (puede traer el prefijo data:)."""
    password: str
    """La contraseña de la llave privada (.key). Se usa para abrirla y no se guarda en texto."""


class SignEfirmaParams(TypedDict):
    cer: str
    """El archivo .cer en base64 (puede traer el prefijo data:)."""
    key: str
    """El archivo .key en base64 (puede traer el prefijo data:)."""
    password: str
    """La contraseña de la llave privada (.key). Se usa para abrirla y no se guarda en texto."""
    keep_for_downloads: NotRequired[bool]
    """true para guardarla (cifrada) y poder pedir al SAT las facturas del emisor con POST /v1/sat_downloads. Sin esto solo firma el contrato con el PAC y no se guarda."""


class CreateIssuerOnboardingLinkParams(TypedDict):
    return_url: NotRequired[str]
    """A dónde regresa el botón al terminar, por ejemplo la página de su plataforma donde su cliente sigue. Sin ella, la página solo dice que ya terminó."""
    expires_in_hours: NotRequired[int]
    """Horas que la liga sirve, de 1 a 168 (7 días). Por omisión 24."""


class ListInvoicesParams(TypedDict):
    """Los parámetros de GET /v1/invoices."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["valid", "pending", "canceled", "rejected", "processing"]]
    """valid, pending, canceled, rejected o processing."""
    type: NotRequired[Literal["I", "E", "P", "T", "N"]]
    """I, E, P, T o N."""
    customer: NotRequired[str]
    """RFC del cliente o su id (cus_…)."""
    payment_status: NotRequired[Literal["unpaid", "partial", "open", "paid"]]
    """Facturas de ingreso por lo que deben: unpaid, partial, open (unpaid o partial) o paid."""
    created_gte: NotRequired[str]
    """Creadas desde, en ISO 8601. Un día solo (2026-10-01) cuenta desde su inicio en hora de la Ciudad de México."""
    created_lte: NotRequired[str]
    """Creadas hasta, en ISO 8601. Un día solo (2026-10-31) incluye el día completo en hora de la Ciudad de México."""
    cost_center: NotRequired[str]
    """Solo las de este centro de costo (ccn_…), o none para las que no tienen."""


class GetInvoiceParams(TypedDict):
    """Los parámetros de GET /v1/invoices/{id}."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""
    refresh: NotRequired[bool]
    """true para preguntar su estado al SAT ahora (cancelaciones en espera)."""


class UpdateInvoiceParams(TypedDict):
    cost_center: NotRequired[str | None]
    """Su centro de costo (ccn_…), o null para quitárselo. Solo facturas, notas de crédito y recibos de nómina timbrados."""


class GetInvoicePdfParams(TypedDict):
    """Los parámetros de GET /v1/invoices/{id}/pdf."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""


class GetInvoiceXmlParams(TypedDict):
    """Los parámetros de GET /v1/invoices/{id}/xml."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""


class SendInvoiceParams(TypedDict):
    to: NotRequired[str]
    """A quién (correos separados por comas)."""
    cc: NotRequired[str | None]
    """Con copia (correos separados por comas)."""


class CancelInvoiceParams(TypedDict):
    motive: NotRequired[Literal["01", "02", "03", "04"]]
    """Motivo de cancelación (c_MotivoCancelacion): 01 con errores con relación (lleva substitution), 02 con errores sin relación (por omisión), 03 no se llevó a cabo, 04 solo en una factura global, cuando una venta incluida se facturó a nombre del cliente."""
    substitution: NotRequired[str]
    """El comprobante que sustituye a este (su id o su UUID), con el motivo 01."""


class MarkInvoicePaidParams(TypedDict):
    paid_on: NotRequired[str]
    """El día en que el cliente pagó (AAAA-MM-DD, no antes de la factura ni después de hoy); hoy si no se indica. Queda en paid_on."""


class ListReceivablesParams(TypedDict):
    """Los parámetros de GET /v1/receivables."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    customer: NotRequired[str]
    """Solo este cliente: su RFC o su id (cus_…)."""


class CreateBankTransactionsParamsTransactionsItem(TypedDict):
    date: str
    """El día del depósito (AAAA-MM-DD)."""
    amount: float
    """Lo depositado, en pesos. Los retiros no se mandan."""
    description: str
    """El concepto del banco, como viene (SPEI, nombre del ordenante…)."""
    reference: NotRequired[str]
    """La referencia o clave de rastreo."""
    payer_tax_id: NotRequired[str]
    """El RFC de quien depositó, si lo sabe (ayuda a sugerir la factura)."""


class CreateBankTransactionsParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    account: NotRequired[str]
    """La cuenta (CLABE o número; se guardan sus últimos 4 dígitos)."""
    transactions: list[CreateBankTransactionsParamsTransactionsItem]
    """Los depósitos, hasta 1,000 por solicitud."""


class ListBankTransactionsParams(TypedDict):
    """Los parámetros de GET /v1/bank_transactions."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["open", "matched", "classified"]]
    """open (sin conciliar), matched o classified."""


class MatchBankTransactionParams(TypedDict):
    invoices: NotRequired[list[str]]
    """Las facturas (inv_… o UUID) que pagó este depósito, de un mismo cliente. Sin ellas, las de suggested_match."""


class ClassifyBankTransactionParams(TypedDict):
    classification: Literal["venta", "prestamo", "traspaso", "devolucion"]
    """venta (una venta que aún no se factura), prestamo, traspaso (entre cuentas propias) o devolucion."""
    note: NotRequired[str]
    """Una nota para su equipo (de dónde vino, por qué)."""


class CreatePurchaseReceiptParamsFieldsItem(TypedDict):
    label: str
    """Cómo lo llama el ticket (Web ID, Sucursal…)."""
    value: str
    """Lo que dice el ticket en ese dato."""


class CreatePurchaseReceiptParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    file: str
    """La foto (JPG, PNG o WebP) o el PDF, en base64; hasta 8 MB."""
    file_type: Literal["image/jpeg", "image/png", "image/webp", "application/pdf"]
    """image/jpeg, image/png, image/webp o application/pdf."""
    qr_text: NotRequired[str]
    """Lo que dice el código QR del ticket, si ya lo leyó (suele ser la liga del portal)."""
    store_name: NotRequired[str | None]
    """El nombre de la tienda."""
    store_tax_id: NotRequired[str | None]
    """El RFC de la tienda (el que factura)."""
    date: NotRequired[str | None]
    """El día de la compra (AAAA-MM-DD)."""
    total: NotRequired[float | None]
    """El total pagado, en pesos."""
    payment_method: NotRequired[Literal["efectivo", "tarjeta", "otro"] | None]
    """efectivo, tarjeta u otro."""
    folio: NotRequired[str | None]
    """El folio o número de ticket."""
    fields: NotRequired[list[CreatePurchaseReceiptParamsFieldsItem]]
    """Otros datos que pide el portal de la tienda (Web ID, sucursal, caja…), hasta 8."""
    portal_url: NotRequired[str | None]
    """La dirección del portal de facturación de la tienda (o la liga de autofactura de su QR)."""
    store_email: NotRequired[str | None]
    """El correo de facturación de la tienda."""
    use: NotRequired[str | None]
    """El uso del CFDI (G03, I01…). Por omisión G03 si el régimen del emisor lo permite."""
    note: NotRequired[str | None]
    """Una nota para su equipo."""


class ListPurchaseReceiptsParams(TypedDict):
    """Los parámetros de GET /v1/purchase_receipts."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["pending", "requested", "invoiced", "non_deductible"]]
    """pending, requested, invoiced o non_deductible."""


class UpdatePurchaseReceiptParamsFieldsItem(TypedDict):
    label: str
    """Cómo lo llama el ticket (Web ID, Sucursal…)."""
    value: str
    """Lo que dice el ticket en ese dato."""


class UpdatePurchaseReceiptParams(TypedDict):
    store_name: NotRequired[str | None]
    """El nombre de la tienda."""
    store_tax_id: NotRequired[str | None]
    """El RFC de la tienda (el que factura)."""
    date: NotRequired[str | None]
    """El día de la compra (AAAA-MM-DD)."""
    total: NotRequired[float | None]
    """El total pagado, en pesos."""
    payment_method: NotRequired[Literal["efectivo", "tarjeta", "otro"] | None]
    """efectivo, tarjeta u otro."""
    folio: NotRequired[str | None]
    """El folio o número de ticket."""
    fields: NotRequired[list[UpdatePurchaseReceiptParamsFieldsItem]]
    """Otros datos que pide el portal de la tienda (Web ID, sucursal, caja…), hasta 8."""
    portal_url: NotRequired[str | None]
    """La dirección del portal de facturación de la tienda (o la liga de autofactura de su QR)."""
    store_email: NotRequired[str | None]
    """El correo de facturación de la tienda."""
    use: NotRequired[str | None]
    """El uso del CFDI (G03, I01…). Por omisión G03 si el régimen del emisor lo permite."""
    note: NotRequired[str | None]
    """Una nota para su equipo."""


class RequestPurchaseReceiptInvoiceParams(TypedDict):
    method: Literal["fiscalisto", "email", "portal", "manual"]
    """fiscalisto (la tienda factura con Fiscalisto: se timbra al momento), email (le mandamos a la tienda sus datos y la foto), portal o manual (usted la pidió; solo se marca pedida)."""
    to: NotRequired[str]
    """email: el correo de la tienda. Por omisión, store_email."""
    message: NotRequired[str]
    """email: unas líneas para la tienda."""
    reply_to: NotRequired[str]
    """email y fiscalisto: el correo al que la tienda manda la factura. Por omisión, el correo de respuesta del emisor."""


class MarkPurchaseReceiptInvoicedParams(TypedDict):
    invoice: NotRequired[str]
    """La factura recibida que lo cubre: su id (sat_…) o su folio fiscal (UUID). Sin ella, solo se marca facturado."""


class CreatePaymentParamsDocumentsItem(TypedDict):
    invoice: str
    """La factura (inv_… o su UUID)."""
    amount: float
    """Lo que se paga de esa factura (ImpPagado), en la moneda de la factura."""
    received: NotRequired[float | None]
    """Solo si la factura es de otra moneda que el pago: lo que recibió por ella en la moneda del pago. Fiscalisto calcula la equivalencia (EquivalenciaDR)."""


class CreatePaymentParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    date: NotRequired[str]
    """Fecha en que le pagaron (FechaPago), AAAA-MM-DD. Por omisión hoy."""
    payment_form: str
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    operation_number: NotRequired[str | None]
    """Número de operación del pago (NumOperacion), como el rastreo SPEI."""
    currency: NotRequired[str]
    """Moneda, clave ISO 4217 de c_Moneda (MXN, USD, EUR…). Por omisión MXN."""
    exchange_rate: NotRequired[float | None]
    """Tipo de cambio a pesos (TipoCambio). Obligatorio si la moneda no es MXN; use el del DOF del día anterior."""
    series: NotRequired[str]
    """Serie (Serie), hasta 25 caracteres. Cada serie lleva sus propios folios."""
    documents: list[CreatePaymentParamsDocumentsItem]
    """Las facturas que paga (DoctoRelacionado)."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    email: NotRequired[str]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    email_cc: NotRequired[str | None]
    """Correos con copia, separados por comas."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""
    bank_transaction: NotRequired[str]
    """El depósito (btx_…) con que le pagaron: queda conciliado con este complemento, y date es su día si no manda otra."""


class CreateCreditNoteParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    invoice: str
    """La factura (inv_… o su UUID)."""
    amount: float
    """Importe de la nota antes de impuestos: Fiscalisto agrega el IVA y las retenciones de la factura en la misma proporción."""
    description: NotRequired[str]
    """Descripción del concepto de la nota (Descripcion), como «Descuento por pronto pago»."""
    payment_form: str
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    relationship: NotRequired[Literal["01", "03"]]
    """Tipo de relación (TipoRelacion) con la factura: 01 nota de crédito (por omisión) o 03 devolución de mercancía."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    email: NotRequired[str]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    email_cc: NotRequired[str | None]
    """Correos con copia, separados por comas."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class CreateAdvanceParamsCustomerForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class CreateAdvanceParamsCustomer(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal del cliente (DomicilioFiscalReceptor), 5 dígitos."""
    email: NotRequired[str | None]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    foreign: NotRequired[CreateAdvanceParamsCustomerForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class CreateAdvanceParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    customer: str | CreateAdvanceParamsCustomer
    """Cliente (Receptor): el id de uno de su catálogo (cus_…) o sus datos en un objeto."""
    use: NotRequired[str]
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    amount: float
    """Lo que pagó el cliente, con IVA incluido."""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    payment_form: str
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    currency: NotRequired[str]
    """Moneda, clave ISO 4217 de c_Moneda (MXN, USD, EUR…). Por omisión MXN."""
    exchange_rate: NotRequired[float]
    """Tipo de cambio a pesos (TipoCambio). Obligatorio si la moneda no es MXN; use el del DOF del día anterior."""
    series: NotRequired[str]
    """Serie (Serie), hasta 25 caracteres. Cada serie lleva sus propios folios."""
    notes: NotRequired[str]
    """Observaciones que aparecen en el PDF (no van en el XML)."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    email_cc: NotRequired[str | None]
    """Correos con copia, separados por comas."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class ListAdvancesParams(TypedDict):
    """Los parámetros de GET /v1/advances."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    customer: NotRequired[str]
    """RFC del cliente o su id (cus_…)."""


class ApplyAdvanceParamsRemainder(TypedDict):
    """Cómo se paga lo que falta del anticipo: ahora con su forma de pago, o después (PPD)."""
    paid_now: bool
    """true si lo que falta se paga ahora (PUE); false si después (PPD)."""
    payment_form: NotRequired[str]
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""


class CreateRetentionParamsRecipient(TypedDict):
    """Receptor de la constancia (Receptor): nacional con RFC y código postal, o extranjero."""
    foreign: NotRequired[bool]
    """true si el receptor es extranjero (sin RFC)."""
    tax_id: NotRequired[str | None]
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    curp: NotRequired[str | None]
    """CURP, 18 caracteres."""


class CreateRetentionParamsPeriod(TypedDict):
    """Periodo (Periodo): mes inicial, mes final y año."""
    year: int
    """Año (Ejercicio)."""
    month: NotRequired[int]
    """Un solo mes, del 1 al 12 (MesIni y MesFin iguales)."""
    from_month: NotRequired[int]
    """Mes inicial (MesIni), 1 a 12."""
    to_month: NotRequired[int]
    """Mes final (MesFin), 1 a 12, del mismo año."""


class CreateRetentionParamsTotals(TypedDict):
    """Totales (Totales)."""
    operation: float
    """Monto total de la operación (MontoTotOperacion)."""
    taxed: NotRequired[float]
    """Monto gravado (MontoTotGrav). Por omisión, operation menos exempt."""
    exempt: NotRequired[float]
    """Monto exento (MontoTotExent). Por omisión 0."""


class CreateRetentionParamsTaxesItem(TypedDict):
    tax: str
    """Impuesto: isr, iva o ieps (ImpuestoRet 001, 002, 003)."""
    base: float
    """Base del impuesto retenido (BaseRet)."""
    amount: float
    """Monto retenido (MontoRet)."""
    payment_type: NotRequired[str]
    """Tipo de pago de la retención (TipoPagoRet): 01 definitivo IVA, 02 definitivo IEPS, 03 definitivo ISR, 04 provisional ISR. Por omisión el usual de cada impuesto."""


class CreateRetentionParamsPlatformServicesItemCommission(TypedDict):
    amount: float
    """Importe."""
    percent: NotRequired[float | None]
    """El porcentaje de la comisión sobre el precio, de 0.001 a 1 (0.25 es 25%). Opcional."""


class CreateRetentionParamsPlatformServicesItemContribution(TypedDict):
    amount: float
    """Importe."""
    state: str
    """Entidad federativa donde trabaja (ClaveEntFed): JAL, CMX, NLE…"""


class CreateRetentionParamsPlatformServicesItem(TypedDict):
    date: str
    """Fecha en que el cliente pagó (FechaServ), AAAA-MM-DD, dentro del mes del periodo."""
    payment_form: str
    """Forma de pago de la operación (FormaPagoServ), c_FormaPagoServ: 01 efectivo, 02 transferencia, 03 tarjeta de crédito, 04 monedero, 05 dinero electrónico, 06 débito, 07 tarjeta de servicios, 08 intermediario de pagos, 09 premios o bonificaciones."""
    price: float
    """Precio sin IVA (PrecioServSinIVA)."""
    rate: NotRequired[float | str | None]
    """Tasa del impuesto trasladado (TasaCuota): 0.16 (por omisión), 0.08 o 0 de IVA; 0.5 de IEPS solo con type 11, donde cada jugada va dos veces: una operación con su IVA y otra con su IEPS (el SAT pide un impuesto por operación). Sin tasa en premios (09), que desde 2026 no suman en totals."""
    subtype: NotRequired[str | None]
    """Subtipo (SubTipServ), c_SubTipoServ: con type 01, 01 personal (por omisión), 02 compartido, 03 plus o 04 cancelación; con type 11, 08 apuestas (por omisión) o 09 sorteos."""
    authorized_tax_id: NotRequired[str | None]
    """RFC (persona física) del tercero autorizado que prestó el servicio (RFCTerceroAutorizado)."""
    commission: NotRequired[CreateRetentionParamsPlatformServicesItemCommission | None]
    """Comisión de la plataforma por la operación (ComisionDelServicio): amount mayor que cero y percent opcional (0.001 a 1). Obligatoria en cada operación con IVA; no va en premios ni en las de IEPS."""
    contribution: NotRequired[CreateRetentionParamsPlatformServicesItemContribution | None]
    """Contribución gubernamental pagada, como el impuesto sobre hospedaje (ContribucionGubernamental): amount de al menos 1.00 y state (01 a 32)."""


class CreateRetentionParamsPlatform(TypedDict):
    """Complemento de servicios de plataformas tecnológicas (ServiciosPlataformasTecnologicas 1.0), obligatorio con code 26: una constancia por mes, receptor y tipo de servicio. totals y taxes se calculan de services con las tasas del SAT (ISR de LISR 113-A y LIF 2026 art. 25; IVA 50% o 100%; IEPS en apuestas); si los manda, deben coincidir."""
    type: str
    """Tipo de servicio (TipoDeServ), c_TipoDeServ: 01 transporte de pasajeros, 02 entrega de alimentos, 03 entrega de bienes, 04 hospedaje, 05 comercio de bienes, 06 otros servicios, 07 a 09 servicios digitales de extranjeros, 11 apuestas y sorteos (desde 2026)."""
    periodicity: NotRequired[str]
    """Cada cuánto paga la plataforma (Periodicidad): 01 semanal, 02 mensual (por omisión), 03 diaria, 04 quincenal, 05 otra."""
    isr_definitive: NotRequired[bool]
    """true si la persona física optó por que el ISR retenido sea pago definitivo (LISR 113-B): TipoPagoRet 03 en lugar de 04."""
    foreign_account: NotRequired[bool]
    """true si se le deposita en una cuenta en el extranjero: se retiene el 100% del IVA (LIF 2026 art. 25-IX-c)."""
    services: list[CreateRetentionParamsPlatformServicesItem]
    """Cada operación (DetallesDelServicio), hasta 5,000. Lo pagado en efectivo (payment_form 01) va en la constancia pero no en las bases."""


class CreateRetentionParamsDividends(TypedDict):
    """Complemento de dividendos."""
    type: Literal["01", "02", "03", "04", "05", "06"]
    """Tipo de dividendo o utilidad distribuida (CveTipDivOUtil), c_TipoDividendoOUtilidadDistribuida."""
    isr_mexico: float
    """ISR acreditable en México (MontISRAcredRetMexico)."""
    isr_foreign: float
    """ISR acreditable en el extranjero (MontISRAcredRetExtranjero)."""
    foreign_retention: NotRequired[float | None]
    """Retención en el extranjero sobre dividendos (MontRetExtDivExt)."""
    company: Literal["nacional", "extranjera"]
    """Tipo de sociedad que distribuye (TipoSocDistrDiv): nacional o extranjera."""
    national_credit: NotRequired[float | None]
    """ISR acreditable nacional (MontISRAcredNal)."""
    accumulated_national: NotRequired[float | None]
    """Dividendo acumulable nacional (MontDivAcumNal)."""
    accumulated_foreign: NotRequired[float | None]
    """Dividendo acumulable extranjero (MontDivAcumExt)."""


class CreateRetentionParamsInterest(TypedDict):
    """Complemento de intereses."""
    financial_system: bool
    """true si los intereses vienen del sistema financiero (SistFinanciero)."""
    retirement: bool
    """true si se retiraron los intereses en el periodo (RetiroAORESRetInt)."""
    derivatives: bool
    """true si son operaciones financieras derivadas (OperFinancDerivad)."""
    nominal: float
    """Interés nominal (MontIntNominal)."""
    real: float
    """Interés real (MontIntReal)."""
    loss: float
    """Pérdida (Perdida)."""


class CreateRetentionParamsForeignPayment(TypedDict):
    """Complemento de pagos a extranjeros."""
    beneficiary: bool
    """true si quien recibe es el beneficiario efectivo (EsBenefEfectDelCobro)."""
    country: NotRequired[str | None]
    """País de residencia del extranjero (PaisDeResidParaEfecFisc), 2 letras."""
    concept: Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    """Concepto del pago (ConceptoPago), c_TipoContribuyenteSujetoRetencion."""
    description: str
    """Descripción del concepto (DescripcionConcepto)."""
    beneficiary_tax_id: NotRequired[str | None]
    """RFC del beneficiario, si no es quien recibe (RFC)."""
    beneficiary_curp: NotRequired[str | None]
    """CURP del beneficiario (CURP)."""
    beneficiary_name: NotRequired[str | None]
    """Nombre o razón social del beneficiario (NomDenRazSocB)."""


class CreateRetentionParamsTrustLease(TypedDict):
    """Complemento de arrendamiento en fideicomiso (Arrendamientoenfideicomiso 1.0), obligatorio con code 17."""
    trustee_payment: float
    """Pago provisional que el fiduciario efectuó al arrendador en el periodo (PagProvEfecPorFiduc)."""
    income: float
    """Rendimientos del periodo por el arrendamiento de los bienes (RendimFideicom)."""
    deductions: float
    """Deducciones del arrendamiento en el periodo (DeduccCorresp)."""
    withheld_total: NotRequired[float | None]
    """Monto total retenido del arrendamiento en el periodo (MontTotRet)."""
    fibra_result: NotRequired[float | None]
    """Resultado fiscal distribuido por FIBRAS (MontResFiscDistFibras)."""
    other_amount: NotRequired[float | None]
    """Monto de otros conceptos distribuidos (MontOtrosConceptDistr)."""
    other_description: NotRequired[str | None]
    """Qué son los otros conceptos distribuidos (DescrMontOtrosConceptDistr); obligatoria con other_amount."""


class CreateRetentionParamsShareSale(TypedDict):
    """Complemento de enajenación de acciones u operaciones de valores (EnajenaciondeAcciones 1.0), obligatorio con code 19."""
    contract: str
    """Descripción del contrato de intermediación (ContratoIntermediacion)."""
    gain: float
    """Ganancia obtenida (Ganancia)."""
    loss: float
    """Pérdida (Perdida)."""


class CreateRetentionParamsPrize(TypedDict):
    """Complemento de premios (Premios 1.0), obligatorio con code 20. Sus montos son los de totals."""
    state: str
    """Entidad federativa donde se paga el premio (EntidadFederativa), c_EntidadesFederativas de catRetenciones: 01 Aguascalientes … 09 Ciudad de México … 32 Zacatecas."""


class CreateRetentionParamsTrustIncome(TypedDict):
    """Ingresos o entradas del fideicomiso en el periodo (IngresosOEntradas) y la parte del receptor."""
    concept: str
    """Concepto de los ingresos (IntegracIngresos/Concepto), hasta 100 caracteres."""
    total: float
    """Ingresos totales del fideicomiso en el periodo (MontTotEntradasPeriodo)."""
    share: float
    """Parte proporcional de los ingresos acumulables del receptor (PartPropAcumDelFideicom)."""
    proportion: float
    """Proporción de participación del receptor según el contrato (PropDelMontTot)."""


class CreateRetentionParamsTrustDeductions(TypedDict):
    """Deducciones o salidas del fideicomiso en el periodo (DeduccOSalidas) y la parte del receptor."""
    concept: str
    """Concepto de los egresos (IntegracEgresos/ConceptoS), hasta 100 caracteres."""
    total: float
    """Egresos totales del fideicomiso en el periodo (MontTotEgresPeriodo)."""
    share: float
    """Parte proporcional de las deducciones autorizadas del receptor (PartPropDelFideicom)."""
    proportion: float
    """Proporción de participación del receptor según el contrato (PropDelMontTot)."""


class CreateRetentionParamsTrustWithholding(TypedDict):
    """Retención efectuada al fideicomiso (RetEfectFideicomiso)."""
    amount: float
    """Monto de la retención (MontRetRelPagFideic)."""
    description: str
    """Descripción de la retención (DescRetRelPagFideic), hasta 100 caracteres."""


class CreateRetentionParamsTrust(TypedDict):
    """Complemento de fideicomisos que no realizan actividades empresariales (Fideicomisonoempresarial 1.0), obligatorio con code 21."""
    income: CreateRetentionParamsTrustIncome
    """Ingresos o entradas del fideicomiso en el periodo (IngresosOEntradas) y la parte del receptor."""
    deductions: CreateRetentionParamsTrustDeductions
    """Deducciones o salidas del fideicomiso en el periodo (DeduccOSalidas) y la parte del receptor."""
    withholding: CreateRetentionParamsTrustWithholding
    """Retención efectuada al fideicomiso (RetEfectFideicomiso)."""


class CreateRetentionParamsRetirementPlanContributionsItem(TypedDict):
    type: Literal["a", "b", "c"]
    """Tipo de aportación (TipoAportacionODeposito): a (art. 151 fracc. V LISR), b (art. 185 LISR) o c (art. 258 RLISR, con trustee_rfc)."""
    amount: float
    """Monto de la aportación o depósito (MontAportODep)."""
    trustee_rfc: NotRequired[str | None]
    """RFC de la fiduciaria que administra el plan (RFCFiduciaria); obligatorio con el tipo c."""


class CreateRetentionParamsRetirementPlan(TypedDict):
    """Complemento de planes personales de retiro (Planesderetiro 1.1), obligatorio con code 22: lo del año anterior."""
    financial_system: bool
    """true si el plan es del sistema financiero (SistemaFinanc)."""
    contributions_last_year: NotRequired[float | None]
    """Aportaciones actualizadas del año anterior (MontTotAportAnioInmAnterior)."""
    real_interest: float
    """Intereses reales devengados o percibidos el año anterior (MontIntRealesDevengAniooInmAnt)."""
    early_withdrawals: bool
    """true si hubo retiros antes de cumplir los requisitos de permanencia (HuboRetirosAnioInmAntPer)."""
    early_withdrawn: NotRequired[float | None]
    """Monto retirado antes de cumplir la permanencia (MontTotRetiradoAnioInmAntPer); obligatorio con early_withdrawals."""
    exempt_withdrawn: NotRequired[float | None]
    """Monto exento de lo retirado el año anterior (MontTotExentRetiradoAnioInmAnt)."""
    excess_withdrawn: NotRequired[float | None]
    """Excedente del monto exento de lo retirado el año anterior (MontTotExedenteAnioInmAnt)."""
    withdrawals: bool
    """true si hubo retiros el año anterior (HuboRetirosAnioInmAnt)."""
    withdrawn: NotRequired[float | None]
    """Monto retirado el año anterior (MontTotRetiradoAnioInmAnt); obligatorio con withdrawals."""
    reference: NotRequired[str | None]
    """Número de referencia, contrato o cuenta del cliente (NumReferencia)."""
    contributions: NotRequired[list[CreateRetentionParamsRetirementPlanContributionsItem]]
    """Aportaciones o depósitos (AportacionesODepositos), uno por tipo y hasta tres."""


class CreateRetentionParamsMortgageInterest(TypedDict):
    """Complemento de intereses reales deducibles por créditos hipotecarios (Intereseshipotecarios 1.0), obligatorio con code 23."""
    financial_institution: bool
    """true si el crédito lo otorgó una institución financiera (CreditoDeInstFinanc)."""
    outstanding_balance: float
    """Saldo insoluto al 31 de diciembre del año anterior, o a la fecha del contrato si es de este año (SaldoInsoluto)."""
    deductible_proportion: NotRequired[float | None]
    """Proporción deducible del crédito sobre los intereses reales devengados y pagados (PropDeducDelCredit)."""
    nominal_accrued: NotRequired[float | None]
    """Intereses nominales devengados (MontTotIntNominalesDev)."""
    nominal_accrued_paid: NotRequired[float | None]
    """Intereses nominales devengados y pagados (MontTotIntNominalesDevYPag)."""
    real_deductible: NotRequired[float | None]
    """Intereses reales pagados deducibles (MontTotIntRealPagDeduc)."""
    contract: NotRequired[str | None]
    """Número de contrato del crédito hipotecario (NumContrato)."""


class CreateRetentionParamsFinancialDerivatives(TypedDict):
    """Complemento de operaciones financieras derivadas de capital (Operacionesconderivados 1.0), obligatorio con code 24."""
    gain: float
    """Ganancia acumulable (MontGanAcum)."""
    loss: float
    """Pérdida deducible (MontPerdDed)."""


class CreateRetentionParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    code: str
    """Clave de la retención (CveRetenc), c_CveRetenc: 01 servicios profesionales, 05 arrendamiento, 14 dividendos, 16 intereses, 18 pagos al extranjero… Las claves 14, 16, 17 y 18 a 24 llevan su complemento (dividends, interest, trust_lease, foreign_payment, share_sale, prize, trust, retirement_plan, mortgage_interest, financial_derivatives); la 26 (plataformas tecnológicas) lleva platform, y sus totals y taxes se calculan de las operaciones."""
    description: NotRequired[str | None]
    """Descripción de la retención (DescRetenc); obligatoria con la clave 25 (otro tipo)."""
    recipient: CreateRetentionParamsRecipient
    """Receptor de la constancia (Receptor): nacional con RFC y código postal, o extranjero."""
    period: CreateRetentionParamsPeriod
    """Periodo (Periodo): mes inicial, mes final y año."""
    totals: NotRequired[CreateRetentionParamsTotals]
    """Totales (Totales)."""
    taxes: NotRequired[list[CreateRetentionParamsTaxesItem]]
    """Impuestos del comprobante, por tipo."""
    platform: NotRequired[CreateRetentionParamsPlatform]
    """Complemento de servicios de plataformas tecnológicas (ServiciosPlataformasTecnologicas 1.0), obligatorio con code 26: una constancia por mes, receptor y tipo de servicio. totals y taxes se calculan de services con las tasas del SAT (ISR de LISR 113-A y LIF 2026 art. 25; IVA 50% o 100%; IEPS en apuestas); si los manda, deben coincidir."""
    dividends: NotRequired[CreateRetentionParamsDividends]
    """Complemento de dividendos."""
    interest: NotRequired[CreateRetentionParamsInterest]
    """Complemento de intereses."""
    foreign_payment: NotRequired[CreateRetentionParamsForeignPayment]
    """Complemento de pagos a extranjeros."""
    trust_lease: NotRequired[CreateRetentionParamsTrustLease]
    """Complemento de arrendamiento en fideicomiso (Arrendamientoenfideicomiso 1.0), obligatorio con code 17."""
    share_sale: NotRequired[CreateRetentionParamsShareSale]
    """Complemento de enajenación de acciones u operaciones de valores (EnajenaciondeAcciones 1.0), obligatorio con code 19."""
    prize: NotRequired[CreateRetentionParamsPrize]
    """Complemento de premios (Premios 1.0), obligatorio con code 20. Sus montos son los de totals."""
    trust: NotRequired[CreateRetentionParamsTrust]
    """Complemento de fideicomisos que no realizan actividades empresariales (Fideicomisonoempresarial 1.0), obligatorio con code 21."""
    retirement_plan: NotRequired[CreateRetentionParamsRetirementPlan]
    """Complemento de planes personales de retiro (Planesderetiro 1.1), obligatorio con code 22: lo del año anterior."""
    mortgage_interest: NotRequired[CreateRetentionParamsMortgageInterest]
    """Complemento de intereses reales deducibles por créditos hipotecarios (Intereseshipotecarios 1.0), obligatorio con code 23."""
    financial_derivatives: NotRequired[CreateRetentionParamsFinancialDerivatives]
    """Complemento de operaciones financieras derivadas de capital (Operacionesconderivados 1.0), obligatorio con code 24."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    email: NotRequired[str]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class ListRetentionsParams(TypedDict):
    """Los parámetros de GET /v1/retentions."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["valid", "canceled", "rejected", "processing"]]
    """valid, canceled, rejected o processing."""
    recipient: NotRequired[str]
    """RFC del receptor."""
    year: NotRequired[str]
    """Ejercicio, 4 dígitos."""


class GetRetentionParams(TypedDict):
    """Los parámetros de GET /v1/retentions/{id}."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""
    refresh: NotRequired[bool]
    """true para preguntar su estado al SAT ahora (cancelaciones en espera)."""


class GetRetentionPdfParams(TypedDict):
    """Los parámetros de GET /v1/retentions/{id}/pdf."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""


class GetRetentionXmlParams(TypedDict):
    """Los parámetros de GET /v1/retentions/{id}/xml."""
    issuer: NotRequired[str]
    """Con un UUID en vez del id, el emisor (iss_…) si la cuenta tiene varios."""


class SendRetentionParams(TypedDict):
    to: NotRequired[str]
    """A quién (correos separados por comas)."""


class CancelRetentionParams(TypedDict):
    motive: NotRequired[Literal["01", "02", "03", "04"]]
    """Motivo de cancelación (c_MotivoCancelacion): 01 con errores con relación (lleva substitution), 02 con errores sin relación (por omisión), 03 no se llevó a cabo, 04 solo en una factura global, cuando una venta incluida se facturó a nombre del cliente."""
    substitution: NotRequired[str]
    """El comprobante que sustituye a este (su id o su UUID), con el motivo 01."""


class CreateEmployeeParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    number: str
    """Número de empleado (NumEmpleado)."""
    name: str
    """Nombre completo del empleado, como en su constancia de situación fiscal."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    curp: str
    """CURP, 18 caracteres."""
    social_security_number: str
    """Número de seguridad social (NumSeguridadSocial), 11 dígitos."""
    zip: str
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: NotRequired[str | None]
    """Correo del empleado, a donde van sus recibos con send_email."""
    start_date: str
    """Fecha de inicio de la relación laboral (FechaInicioRelLaboral), AAAA-MM-DD."""
    end_date: NotRequired[str | None]
    """Último día trabajado si ya no trabaja ahí, AAAA-MM-DD."""
    daily_salary: float
    """Salario diario."""
    integrated_daily_salary: float
    """Salario diario integrado (SalarioDiarioIntegrado): no menor al salario diario."""
    contract_type: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Tipo de contrato (TipoContrato), c_TipoContrato. Por omisión 01, por tiempo indeterminado."""
    workday_type: NotRequired[str]
    """Tipo de jornada (TipoJornada), c_TipoJornada. Por omisión 01, diurna."""
    periodicity: NotRequired[str]
    """Periodicidad del pago (PeriodicidadPago): 02 semanal, 03 catorcenal, 04 quincenal (por omisión), 05 mensual."""
    risk_class: NotRequired[str]
    """Clase de riesgo del puesto ante el IMSS (RiesgoPuesto), 1 a 5. Por omisión 1."""
    state: str
    """Entidad federativa donde trabaja (ClaveEntFed): JAL, CMX, NLE…"""
    border_zone: NotRequired[bool]
    """true si trabaja en la zona libre de la frontera norte (salario mínimo de frontera)."""
    unionized: NotRequired[bool]
    """true si es sindicalizado (Sindicalizado)."""
    department: NotRequired[str | None]
    """Departamento (Departamento)."""
    position: NotRequired[str | None]
    """Puesto (Puesto)."""
    clabe: NotRequired[str | None]
    """CLABE de 18 dígitos de la cuenta del empleado: a donde le paga el archivo para el banco (POST /v1/payroll_bank_files)."""
    given_names: NotRequired[str | None]
    """Nombre(s), como en su CURP. Con first_surname y second_surname, los archivos del IMSS (IDSE y SUA) escriben el nombre en sus tres partes; sin ellos, Fiscalisto lo separa con la CURP."""
    first_surname: NotRequired[str | None]
    """Primer apellido, como en su CURP."""
    second_surname: NotRequired[str | None]
    """Segundo apellido (vacío si tiene uno)."""
    imss_worker_type: NotRequired[Literal["1", "2", "3", "4"]]
    """Tipo de trabajador del IMSS: 1 permanente, 2 eventual de la ciudad, 3 eventual de la construcción, 4 eventual del campo. Por omisión 1."""
    imss_salary_type: NotRequired[Literal["0", "1", "2"]]
    """Tipo de salario del IMSS: 0 fijo, 1 variable, 2 mixto. Por omisión 0."""
    imss_reduced_week: NotRequired[Literal["0", "1", "2", "3", "4", "5", "6"]]
    """Semana o jornada reducida: 0 normal, 1 a 5 los días que trabaja a la semana, 6 jornada de menos de 8 horas. Por omisión 0."""
    family_medicine_unit: NotRequired[str | None]
    """Unidad de medicina familiar (UMF) del IMSS, opcional."""
    exit_reason: NotRequired[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "A"] | None]
    """Causa de la baja ante el IMSS, con end_date: 1 término de contrato, 2 separación voluntaria (la usual), 3 abandono, 4 defunción, 5 clausura, 6 otras, 7 ausentismo, 8 rescisión, 9 jubilación, A pensión."""


class ListEmployeesParams(TypedDict):
    """Los parámetros de GET /v1/employees."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class UpdateEmployeeParams(TypedDict):
    number: NotRequired[str]
    """Número de empleado (NumEmpleado)."""
    name: NotRequired[str]
    """Nombre completo del empleado, como en su constancia de situación fiscal."""
    tax_id: NotRequired[str]
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    curp: NotRequired[str]
    """CURP, 18 caracteres."""
    social_security_number: NotRequired[str]
    """Número de seguridad social (NumSeguridadSocial), 11 dígitos."""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: NotRequired[str | None]
    """Correo del empleado, a donde van sus recibos con send_email."""
    start_date: NotRequired[str]
    """Fecha de inicio de la relación laboral (FechaInicioRelLaboral), AAAA-MM-DD."""
    end_date: NotRequired[str | None]
    """Último día trabajado si ya no trabaja ahí, AAAA-MM-DD."""
    daily_salary: NotRequired[float]
    """Salario diario."""
    integrated_daily_salary: NotRequired[float]
    """Salario diario integrado (SalarioDiarioIntegrado): no menor al salario diario."""
    contract_type: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Tipo de contrato (TipoContrato), c_TipoContrato. Por omisión 01, por tiempo indeterminado."""
    workday_type: NotRequired[str]
    """Tipo de jornada (TipoJornada), c_TipoJornada. Por omisión 01, diurna."""
    periodicity: NotRequired[str]
    """Periodicidad del pago (PeriodicidadPago): 02 semanal, 03 catorcenal, 04 quincenal (por omisión), 05 mensual."""
    risk_class: NotRequired[str]
    """Clase de riesgo del puesto ante el IMSS (RiesgoPuesto), 1 a 5. Por omisión 1."""
    state: NotRequired[str]
    """Entidad federativa donde trabaja (ClaveEntFed): JAL, CMX, NLE…"""
    border_zone: NotRequired[bool]
    """true si trabaja en la zona libre de la frontera norte (salario mínimo de frontera)."""
    unionized: NotRequired[bool]
    """true si es sindicalizado (Sindicalizado)."""
    department: NotRequired[str | None]
    """Departamento (Departamento)."""
    position: NotRequired[str | None]
    """Puesto (Puesto)."""
    clabe: NotRequired[str | None]
    """CLABE de 18 dígitos de la cuenta del empleado: a donde le paga el archivo para el banco (POST /v1/payroll_bank_files)."""
    given_names: NotRequired[str | None]
    """Nombre(s), como en su CURP. Con first_surname y second_surname, los archivos del IMSS (IDSE y SUA) escriben el nombre en sus tres partes; sin ellos, Fiscalisto lo separa con la CURP."""
    first_surname: NotRequired[str | None]
    """Primer apellido, como en su CURP."""
    second_surname: NotRequired[str | None]
    """Segundo apellido (vacío si tiene uno)."""
    imss_worker_type: NotRequired[Literal["1", "2", "3", "4"]]
    """Tipo de trabajador del IMSS: 1 permanente, 2 eventual de la ciudad, 3 eventual de la construcción, 4 eventual del campo. Por omisión 1."""
    imss_salary_type: NotRequired[Literal["0", "1", "2"]]
    """Tipo de salario del IMSS: 0 fijo, 1 variable, 2 mixto. Por omisión 0."""
    imss_reduced_week: NotRequired[Literal["0", "1", "2", "3", "4", "5", "6"]]
    """Semana o jornada reducida: 0 normal, 1 a 5 los días que trabaja a la semana, 6 jornada de menos de 8 horas. Por omisión 0."""
    family_medicine_unit: NotRequired[str | None]
    """Unidad de medicina familiar (UMF) del IMSS, opcional."""
    exit_reason: NotRequired[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "A"] | None]
    """Causa de la baja ante el IMSS, con end_date: 1 término de contrato, 2 separación voluntaria (la usual), 3 abandono, 4 defunción, 5 clausura, 6 otras, 7 ausentismo, 8 rescisión, 9 jubilación, A pensión."""


class CreatePayrollReceiptParamsPeriod(TypedDict):
    """El periodo de pago: primer y último día (FechaInicialPago, FechaFinalPago) y, si no es el último, el día de pago (FechaPago)."""
    start: str
    """Primer día del periodo (FechaInicialPago), AAAA-MM-DD."""
    end: str
    """Último día del periodo (FechaFinalPago), AAAA-MM-DD."""
    payment_date: NotRequired[str]
    """Fecha de pago (FechaPago), AAAA-MM-DD. Por omisión el último día del periodo."""


class CreatePayrollReceiptParams(TypedDict):
    employee: str
    """El empleado (emp_…)."""
    period: CreatePayrollReceiptParamsPeriod
    """El periodo de pago: primer y último día (FechaInicialPago, FechaFinalPago) y, si no es el último, el día de pago (FechaPago)."""
    days: NotRequired[float]
    """Días pagados (NumDiasPagados). Por omisión, todos los del periodo que le tocan."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""
    confirmation_token: NotRequired[str]
    """El confirmation_token de POST /v1/payroll_receipts/preview: timbra solo si el recibo calculado ahora es exactamente el que revisó (si no, 409 payroll_calculation_changed y no timbra). Sin él, timbra el que calcule en ese momento."""


class PreviewPayrollReceiptParamsPeriod(TypedDict):
    """El periodo de pago: primer y último día (FechaInicialPago, FechaFinalPago) y, si no es el último, el día de pago (FechaPago)."""
    start: str
    """Primer día del periodo (FechaInicialPago), AAAA-MM-DD."""
    end: str
    """Último día del periodo (FechaFinalPago), AAAA-MM-DD."""
    payment_date: NotRequired[str]
    """Fecha de pago (FechaPago), AAAA-MM-DD. Por omisión el último día del periodo."""


class PreviewPayrollReceiptParams(TypedDict):
    employee: str
    """El empleado (emp_…)."""
    period: PreviewPayrollReceiptParamsPeriod
    """El periodo de pago: primer y último día (FechaInicialPago, FechaFinalPago) y, si no es el último, el día de pago (FechaPago)."""
    days: NotRequired[float]
    """Días pagados (NumDiasPagados). Por omisión, todos los del periodo que le tocan."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    metadata: NotRequired[dict[str, str]]
    """Sus propios datos: hasta 50 llaves de 40 caracteres con valores de texto de hasta 500. No van al CFDI; vuelven en el objeto y en los webhooks."""


class CreatePayrollBatchParamsPeriod(TypedDict):
    """El periodo de pago: primer y último día (FechaInicialPago, FechaFinalPago) y, si no es el último, el día de pago (FechaPago). Va para todos los recibos de receipts que no traen el suyo."""
    start: str
    """Primer día pagado (FechaInicialPago)."""
    end: str
    """Último día pagado (FechaFinalPago)."""
    payment_date: NotRequired[str]
    """Día de pago (FechaPago); sin él, el último día del periodo."""


class CreatePayrollBatchParamsReceiptsItemPeriod(TypedDict):
    """Su periodo de pago (FechaInicialPago, FechaFinalPago y FechaPago), si no es el del lote (period)."""
    start: str
    """Primer día pagado (FechaInicialPago)."""
    end: str
    """Último día pagado (FechaFinalPago)."""
    payment_date: NotRequired[str]
    """Día de pago (FechaPago); sin él, el último día del periodo."""


class CreatePayrollBatchParamsReceiptsItem(TypedDict):
    employee: str
    """El empleado (emp_…) del emisor del lote."""
    period: NotRequired[CreatePayrollBatchParamsReceiptsItemPeriod]
    """Su periodo de pago (FechaInicialPago, FechaFinalPago y FechaPago), si no es el del lote (period)."""
    days: NotRequired[float]
    """Días pagados; sin él, todos los días que le tocan del periodo."""
    send_email: NotRequired[bool]
    """Mandarle su recibo por correo; sin él, lo que diga send_email del lote. Con true el empleado debe tener correo."""
    reference: NotRequired[str]
    """Su identificador de este recibo, hasta 100 caracteres."""


class CreatePayrollBatchParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    name: NotRequired[str]
    """Nombre del lote, para usted (Quincena 20)."""
    period: NotRequired[CreatePayrollBatchParamsPeriod]
    """El periodo de pago: primer y último día (FechaInicialPago, FechaFinalPago) y, si no es el último, el día de pago (FechaPago). Va para todos los recibos de receipts que no traen el suyo."""
    send_email: NotRequired[bool]
    """Mandar a cada empleado su recibo por correo (a los que tienen correo). Solo con receipts."""
    receipts: NotRequired[list[CreatePayrollBatchParamsReceiptsItem]]
    """Los recibos que Fiscalisto calcula: un empleado (emp_…) en cada uno, como en POST /v1/payroll_receipts."""
    external_receipts: NotRequired[list[CreatePayrollBatchParamsExternalReceiptsItem]]
    """Los recibos que calculó su sistema de nómina, timbrados tal cual. En lugar de receipts."""


class ListPayrollBatchesParams(TypedDict):
    """Los parámetros de GET /v1/payroll_batches."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class CreatePayrollBankFileParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    payment_date: str
    """La fecha de pago de los recibos (FechaPago): se pagan los recibos de nómina timbrados con esa fecha, sumados por empleado. También es el día en que el banco aplica el archivo."""
    layout: NotRequired[Literal["bbva", "banamex", "banorte", "santander", "spei"]]
    """El formato del banco: bbva (Net Cash), banamex (BancaNet, layout D), banorte (Banorte en su Empresa), santander (Enlace, solo cuentas Santander) o spei (CSV para cualquier banco). Por omisión, el del banco de account."""
    account: NotRequired[str]
    """La CLABE de la cuenta de cargo del emisor. Por omisión, la que se usó la última vez en la app, o su primera cuenta bancaria."""
    sequence: NotRequired[int]
    """El archivo del día (1 a 99): un segundo archivo el mismo día lleva otro número. Por omisión 1."""
    client_number: NotRequired[str]
    """Banamex: su número de cliente de BancaNet (12 dígitos)."""
    issuer_number: NotRequired[str]
    """Banorte: su número de emisora (5 dígitos)."""


class CreateImssMovementParams(TypedDict):
    employee: str
    """El empleado (emp_…)."""
    kind: Literal["alta", "reingreso", "modificacion", "baja"]
    """alta (o reingreso): tipo 08; modificacion: cambio de salario, tipo 07; baja: tipo 02."""
    date: str
    """El día en que surte efecto (AAAA-MM-DD, hora de México). El IMSS no acepta más de unos días de anticipación."""
    integrated_daily_salary: NotRequired[float | None]
    """El salario diario integrado que se declara (en altas, reingresos y modificaciones). El archivo lo topa a 25 UMA y nunca baja del salario mínimo."""
    exit_reason: NotRequired[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "A"] | None]
    """Solo en bajas: 1 término de contrato, 2 separación voluntaria, 3 abandono, 4 defunción, 5 clausura, 6 otras, 7 ausentismo, 8 rescisión, 9 jubilación, A pensión."""


class ListImssMovementsParams(TypedDict):
    """Los parámetros de GET /v1/imss_movements."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["pending", "reported"]]
    """pending (por omisión) o reported."""


class ReportImssMovementsParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    movements: list[str]
    """Los movimientos (imv_…) que el IMSS ya recibió, hasta 1,000."""
    reported: NotRequired[bool]
    """true (por omisión): marcarlos como presentados; false: devolverlos a pendientes (si los marcó por error)."""


class UpdateImssMovementParams(TypedDict):
    kind: NotRequired[Literal["alta", "reingreso", "modificacion", "baja"]]
    """alta (o reingreso): tipo 08; modificacion: cambio de salario, tipo 07; baja: tipo 02."""
    date: NotRequired[str]
    """El día en que surte efecto (AAAA-MM-DD, hora de México). El IMSS no acepta más de unos días de anticipación."""
    integrated_daily_salary: NotRequired[float | None]
    """El salario diario integrado que se declara (en altas, reingresos y modificaciones). El archivo lo topa a 25 UMA y nunca baja del salario mínimo."""
    exit_reason: NotRequired[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "A"] | None]
    """Solo en bajas: 1 término de contrato, 2 separación voluntaria, 3 abandono, 4 defunción, 5 clausura, 6 otras, 7 ausentismo, 8 rescisión, 9 jubilación, A pensión."""


class CreateImssFilesParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    format: Literal["idse", "sua"]
    """idse: los archivos de IDSE (uno por tipo: reingresos, modificaciones, bajas); sua: ASEG.TXT (altas) y MOVT.TXT (los demás) para importar en SUA."""
    movements: NotRequired[list[str]]
    """Los movimientos (imv_…) pendientes que van en los archivos. Por omisión, todos los pendientes."""
    guide: NotRequired[str]
    """IDSE: la guía de 5 dígitos de su subdelegación. Por omisión, la que se guardó en la app."""


class CreateInvoiceBatchParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    name: NotRequired[str]
    """Nombre del lote, para usted."""
    invoices: list[CreateInvoiceBatchParamsInvoicesItem]
    """Las facturas, como el cuerpo de POST /v1/invoices, con reference opcional."""


class ListInvoiceBatchesParams(TypedDict):
    """Los parámetros de GET /v1/invoice_batches."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class ValidateTaxIdParams(TypedDict):
    tax_id: str
    """El RFC del cliente."""
    legal_name: NotRequired[str]
    """El nombre o razón social que va a poner en la factura."""
    tax_system: NotRequired[str]
    """Su régimen fiscal (c_RegimenFiscal), como 601 o 612."""
    zip: NotRequired[str]
    """El código postal de su domicilio fiscal."""
    use: NotRequired[str]
    """El uso del CFDI (c_UsoCFDI), como G03."""
    cif_id: NotRequired[str]
    """El idCIF de su constancia de situación fiscal (11 dígitos, arriba a la izquierda, junto al QR). Con él se compara todo con lo que tiene el SAT."""


class CreateBranchParamsAddress(TypedDict):
    """La dirección que va en el PDF de sus facturas."""
    street: NotRequired[str | None]
    """Calle."""
    exterior: NotRequired[str | None]
    """Número exterior."""
    interior: NotRequired[str | None]
    """Número interior."""
    neighborhood: NotRequired[str | None]
    """Colonia."""
    city: NotRequired[str | None]
    """Municipio o alcaldía."""
    state: NotRequired[str | None]
    """Estado; por omisión, el de su código postal."""


class CreateBranchParamsSeries(TypedDict):
    """La serie de cada tipo de CFDI que se timbra desde ella (invoice, credit_note, payment, transfer), hasta 25 caracteres cada una; la que no mande usa la del emisor."""
    invoice: NotRequired[str | None]
    """Serie de sus facturas (tipo I); sin ella, la del emisor."""
    credit_note: NotRequired[str | None]
    """Serie de sus notas de crédito (tipo E); sin ella, la del emisor."""
    payment: NotRequired[str | None]
    """Serie de sus complementos de pago (tipo P); sin ella, la del emisor."""
    transfer: NotRequired[str | None]
    """Serie de sus traslados (tipo T); sin ella, la del emisor."""


class CreateBranchParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…). Por omisión, su único emisor."""
    name: str
    """Cómo la llama su equipo, por ejemplo «Sucursal Monterrey». Va en el PDF."""
    zip: str
    """Su código postal (LugarExpedicion de sus CFDI). Varias sucursales pueden compartirlo, y también el del domicilio fiscal del emisor."""
    address: NotRequired[CreateBranchParamsAddress]
    """La dirección que va en el PDF de sus facturas."""
    phone: NotRequired[str | None]
    """Teléfono, para el PDF."""
    email: NotRequired[str | None]
    """Correo, para el PDF."""
    series: NotRequired[CreateBranchParamsSeries]
    """La serie de cada tipo de CFDI que se timbra desde ella (invoice, credit_note, payment, transfer), hasta 25 caracteres cada una; la que no mande usa la del emisor."""
    trade_name: NotRequired[str | None]
    """Su nombre comercial, si se presenta con otra marca: va en grande en el PDF de lo que se factura desde ella, en el correo y en la página de la factura. null toma el del emisor."""
    pdf_color: NotRequired[str | None]
    """Color del PDF de sus facturas, como #2563EB. null toma el del emisor."""
    pdf_style: NotRequired[Literal["clasico", "moderno", "compacto", "minimalista"] | None]
    """Estilo del PDF de sus facturas: clasico, moderno, compacto o minimalista. null toma el del emisor."""


class ListBranchesParams(TypedDict):
    """Los parámetros de GET /v1/branches."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    include_archived: NotRequired[bool]
    """true para incluir las archivadas."""
    zip: NotRequired[str]
    """Solo la de este código postal."""


class UpdateBranchParamsAddress(TypedDict):
    """La dirección que va en el PDF de sus facturas."""
    street: NotRequired[str | None]
    """Calle."""
    exterior: NotRequired[str | None]
    """Número exterior."""
    interior: NotRequired[str | None]
    """Número interior."""
    neighborhood: NotRequired[str | None]
    """Colonia."""
    city: NotRequired[str | None]
    """Municipio o alcaldía."""
    state: NotRequired[str | None]
    """Estado; por omisión, el de su código postal."""


class UpdateBranchParamsSeries(TypedDict):
    """La serie de cada tipo de CFDI que se timbra desde ella (invoice, credit_note, payment, transfer), hasta 25 caracteres cada una; la que no mande usa la del emisor."""
    invoice: NotRequired[str | None]
    """Serie de sus facturas (tipo I); sin ella, la del emisor."""
    credit_note: NotRequired[str | None]
    """Serie de sus notas de crédito (tipo E); sin ella, la del emisor."""
    payment: NotRequired[str | None]
    """Serie de sus complementos de pago (tipo P); sin ella, la del emisor."""
    transfer: NotRequired[str | None]
    """Serie de sus traslados (tipo T); sin ella, la del emisor."""


class UpdateBranchParams(TypedDict):
    name: NotRequired[str]
    """Cómo la llama su equipo, por ejemplo «Sucursal Monterrey». Va en el PDF."""
    zip: NotRequired[str]
    """Su código postal (LugarExpedicion de sus CFDI). Varias sucursales pueden compartirlo, y también el del domicilio fiscal del emisor."""
    address: NotRequired[UpdateBranchParamsAddress]
    """La dirección que va en el PDF de sus facturas."""
    phone: NotRequired[str | None]
    """Teléfono, para el PDF."""
    email: NotRequired[str | None]
    """Correo, para el PDF."""
    series: NotRequired[UpdateBranchParamsSeries]
    """La serie de cada tipo de CFDI que se timbra desde ella (invoice, credit_note, payment, transfer), hasta 25 caracteres cada una; la que no mande usa la del emisor."""
    trade_name: NotRequired[str | None]
    """Su nombre comercial, si se presenta con otra marca: va en grande en el PDF de lo que se factura desde ella, en el correo y en la página de la factura. null toma el del emisor."""
    pdf_color: NotRequired[str | None]
    """Color del PDF de sus facturas, como #2563EB. null toma el del emisor."""
    pdf_style: NotRequired[Literal["clasico", "moderno", "compacto", "minimalista"] | None]
    """Estilo del PDF de sus facturas: clasico, moderno, compacto o minimalista. null toma el del emisor."""
    archived: NotRequired[bool]
    """true la archiva: ya no se puede facturar desde ella, y sus facturas la siguen nombrando. false la restaura."""


class CreateCostCenterParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…). Por omisión, su único emisor."""
    name: str
    """Cómo lo llama su equipo, por ejemplo «Obra Norte». No se repite en el emisor (sin importar mayúsculas)."""
    code: NotRequired[str | None]
    """Su clave, si su contabilidad usa claves (por ejemplo «CC-01»)."""


class ListCostCentersParams(TypedDict):
    """Los parámetros de GET /v1/cost_centers."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    include_archived: NotRequired[bool]
    """true para incluir los archivados."""


class UpdateCostCenterParams(TypedDict):
    name: NotRequired[str]
    """Cómo lo llama su equipo, por ejemplo «Obra Norte». No se repite en el emisor (sin importar mayúsculas)."""
    code: NotRequired[str | None]
    """Su clave, si su contabilidad usa claves (por ejemplo «CC-01»)."""
    archived: NotRequired[bool]
    """true lo archiva: ya no se pueden poner facturas en él, pero las suyas lo conservan. false lo restaura."""


class DeleteCostCenterParams(TypedDict):
    """Los parámetros de DELETE /v1/cost_centers/{id}."""
    move_to: NotRequired[str]
    """Otro centro de costo (ccn_…) que se queda con sus facturas."""


class CreatePriceListParamsItemsItem(TypedDict):
    product: str
    """El producto (prd_…)."""
    unit: NotRequired[str | None]
    """Una presentación del producto (su id de unidad, un entero de GET /v1/products/{id}/units), por ejemplo una caja de 12; null o sin él: su propia unidad."""
    min_quantity: NotRequired[float]
    """Desde cuántas aplica (1 por omisión): varios renglones del mismo producto son sus escalones de mayoreo."""
    unit_price: NotRequired[float]
    """Su precio por unidad sin IVA. Mande este o discount_percent."""
    discount_percent: NotRequired[float]
    """Un descuento sobre el precio de la lista. Mande este o unit_price."""


class CreatePriceListParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    name: str
    """Mayoreo, Distribuidor, Buen Fin…"""
    description: NotRequired[str | None]
    """Descripción."""
    base_list: NotRequired[str | None]
    """Otra lista (prl_…) de la que parte; null o sin ella: el precio del catálogo."""
    adjust_percent: NotRequired[float]
    """Cuánto mueve el precio del que parte: −10 lo baja 10 %, 5 lo sube 5 %."""
    round_to: NotRequired[float | None]
    """Redondea a: 0.5, 1, 5, 10… (null: a centavos)."""
    starts_on: NotRequired[str | None]
    """Desde qué día vale (YYYY-MM-DD, Ciudad de México), o null desde siempre."""
    ends_on: NotRequired[str | None]
    """Hasta qué día vale, ese día incluido (YYYY-MM-DD), o null sin fin."""
    is_default: NotRequired[bool]
    """La tienen los clientes sin otra lista (ni ellos ni su grupo). Solo una lo es."""
    items: NotRequired[list[CreatePriceListParamsItemsItem]]
    """Sus precios propios; al mandarlos reemplazan a los que tenía."""


class ListPriceListsParams(TypedDict):
    """Los parámetros de GET /v1/price_lists."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class UpdatePriceListParamsItemsItem(TypedDict):
    product: str
    """El producto (prd_…)."""
    unit: NotRequired[str | None]
    """Una presentación del producto (su id de unidad, un entero de GET /v1/products/{id}/units), por ejemplo una caja de 12; null o sin él: su propia unidad."""
    min_quantity: NotRequired[float]
    """Desde cuántas aplica (1 por omisión): varios renglones del mismo producto son sus escalones de mayoreo."""
    unit_price: NotRequired[float]
    """Su precio por unidad sin IVA. Mande este o discount_percent."""
    discount_percent: NotRequired[float]
    """Un descuento sobre el precio de la lista. Mande este o unit_price."""


class UpdatePriceListParams(TypedDict):
    name: NotRequired[str]
    """Mayoreo, Distribuidor, Buen Fin…"""
    description: NotRequired[str | None]
    """Descripción."""
    base_list: NotRequired[str | None]
    """Otra lista (prl_…) de la que parte; null o sin ella: el precio del catálogo."""
    adjust_percent: NotRequired[float]
    """Cuánto mueve el precio del que parte: −10 lo baja 10 %, 5 lo sube 5 %."""
    round_to: NotRequired[float | None]
    """Redondea a: 0.5, 1, 5, 10… (null: a centavos)."""
    starts_on: NotRequired[str | None]
    """Desde qué día vale (YYYY-MM-DD, Ciudad de México), o null desde siempre."""
    ends_on: NotRequired[str | None]
    """Hasta qué día vale, ese día incluido (YYYY-MM-DD), o null sin fin."""
    is_default: NotRequired[bool]
    """La tienen los clientes sin otra lista (ni ellos ni su grupo). Solo una lo es."""
    items: NotRequired[list[UpdatePriceListParamsItemsItem]]
    """Sus precios propios; al mandarlos reemplazan a los que tenía."""


class CreateCustomerGroupParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    name: str
    """Nombre."""
    color: NotRequired[Literal["info", "warning", "positive", "critical", "muted"]]
    """Color de su etiqueta en la app: info, warning, positive, critical o muted."""
    price_list: NotRequired[str | None]
    """Su lista (prl_…); null: la que aplica a todos."""
    discount_percent: NotRequired[float]
    """Un descuento en cada concepto, como descuento del CFDI."""
    credit_days: NotRequired[int | None]
    """Días de crédito que se le dan, de 0 a 365, o null para no cambiar los del cliente."""
    min_order: NotRequired[float | None]
    """El pedido mínimo antes de IVA desde el Portal del cliente."""
    portal_ordering: NotRequired[bool]
    """Sus clientes pueden hacer pedidos desde su Portal del cliente (true por omisión)."""


class ListCustomerGroupsParams(TypedDict):
    """Los parámetros de GET /v1/customer_groups."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class UpdateCustomerGroupParams(TypedDict):
    name: NotRequired[str]
    """Nombre."""
    color: NotRequired[Literal["info", "warning", "positive", "critical", "muted"]]
    """Color de su etiqueta en la app: info, warning, positive, critical o muted."""
    price_list: NotRequired[str | None]
    """Su lista (prl_…); null: la que aplica a todos."""
    discount_percent: NotRequired[float]
    """Un descuento en cada concepto, como descuento del CFDI."""
    credit_days: NotRequired[int | None]
    """Días de crédito que se le dan, de 0 a 365, o null para no cambiar los del cliente."""
    min_order: NotRequired[float | None]
    """El pedido mínimo antes de IVA desde el Portal del cliente."""
    portal_ordering: NotRequired[bool]
    """Sus clientes pueden hacer pedidos desde su Portal del cliente (true por omisión)."""


class QuotePricesParamsItemsItem(TypedDict):
    product: str
    """El producto (prd_…)."""
    quantity: NotRequired[float]
    """Cantidad (Cantidad). Por omisión 1."""
    unit: NotRequired[str | None]
    """Unidad aduana (UnidadAduana), c_UnidadAduana."""


class QuotePricesParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    customer: str
    """El cliente (cus_…) o su RFC."""
    items: list[QuotePricesParamsItemsItem]
    """Conceptos (Conceptos), al menos uno."""


class CreateExpensePersonParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…). Por omisión, su único emisor."""
    kind: Literal["empleado", "honorarios"]
    """empleado (sus viáticos van en su recibo de nómina; sus facturas pueden ir a su nombre en un viaje) o honorarios (sus facturas deben ir a nombre del emisor)."""
    employee: NotRequired[str | None]
    """Un empleado de Nómina (emp_…): su nombre, RFC y correo se toman de ahí y sus viáticos van en su recibo. Solo con kind empleado."""
    name: NotRequired[str | None]
    """Su nombre. Obligatorio sin employee."""
    tax_id: NotRequired[str | None]
    """Su RFC."""
    email: NotRequired[str | None]
    """Su correo: para mandarle su enlace y avisarle cuando se aprueba o se le paga."""
    base_city: NotRequired[str | None]
    """Dónde trabaja (por ejemplo «Guadalajara, Jal.»): un viaje a menos de 50 km no es deducible como viáticos."""
    department: NotRequired[str | None]
    """Su área."""


class ListExpensePeopleParams(TypedDict):
    """Los parámetros de GET /v1/expense_people."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    include_archived: NotRequired[bool]
    """true para incluir las archivadas."""


class UpdateExpensePersonParams(TypedDict):
    kind: NotRequired[Literal["empleado", "honorarios"]]
    """empleado (sus viáticos van en su recibo de nómina; sus facturas pueden ir a su nombre en un viaje) o honorarios (sus facturas deben ir a nombre del emisor)."""
    employee: NotRequired[str | None]
    """Un empleado de Nómina (emp_…): su nombre, RFC y correo se toman de ahí y sus viáticos van en su recibo. Solo con kind empleado."""
    name: NotRequired[str | None]
    """Su nombre. Obligatorio sin employee."""
    tax_id: NotRequired[str | None]
    """Su RFC."""
    email: NotRequired[str | None]
    """Su correo: para mandarle su enlace y avisarle cuando se aprueba o se le paga."""
    base_city: NotRequired[str | None]
    """Dónde trabaja (por ejemplo «Guadalajara, Jal.»): un viaje a menos de 50 km no es deducible como viáticos."""
    department: NotRequired[str | None]
    """Su área."""
    archived: NotRequired[bool]
    """true la archiva (y apaga su enlace): ya no se le abren comprobaciones. false la restaura."""


class CreateExpensePersonLinkParams(TypedDict):
    renew: NotRequired[bool]
    """true le da un enlace nuevo: el anterior deja de funcionar en ese momento (por ejemplo, si se compartió por error)."""


class CreateExpenseReportParams(TypedDict):
    person: str
    """La persona (exp_…)."""
    kind: NotRequired[Literal["viaje", "gastos"]]
    """viaje (por omisión) o gastos (gastos de oficina de un periodo que la empresa reembolsa)."""
    title: NotRequired[str | None]
    """Su nombre. Por omisión, «Viaje a {destination}» o el periodo."""
    purpose: NotRequired[str | None]
    """Para qué fue: el SAT pide que el viaje sea por el negocio."""
    destination: NotRequired[str | None]
    """A dónde."""
    abroad: NotRequired[bool]
    """Al extranjero: cambian los topes de alimentos y hospedaje."""
    far: NotRequired[bool]
    """A más de 50 km de donde trabaja la persona (por omisión, true). Más cerca, no son viáticos deducibles."""
    start_date: NotRequired[str | None]
    """La salida (o el inicio del periodo)."""
    end_date: NotRequired[str | None]
    """El regreso (o el fin del periodo)."""


class ListExpenseReportsParams(TypedDict):
    """Los parámetros de GET /v1/expense_reports."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[str]
    """Solo las de un estado: draft, submitted, rejected, approved o closed."""
    person: NotRequired[str]
    """Solo las de una persona (exp_…)."""


class UpdateExpenseReportParams(TypedDict):
    title: NotRequired[str | None]
    """Su nombre. Por omisión, «Viaje a {destination}» o el periodo."""
    purpose: NotRequired[str | None]
    """Para qué fue: el SAT pide que el viaje sea por el negocio."""
    destination: NotRequired[str | None]
    """A dónde."""
    abroad: NotRequired[bool]
    """Al extranjero: cambian los topes de alimentos y hospedaje."""
    far: NotRequired[bool]
    """A más de 50 km de donde trabaja la persona (por omisión, true). Más cerca, no son viáticos deducibles."""
    start_date: NotRequired[str | None]
    """La salida (o el inicio del periodo)."""
    end_date: NotRequired[str | None]
    """El regreso (o el fin del periodo)."""


class ApproveExpenseReportParams(TypedDict):
    note: NotRequired[str | None]
    """Una nota para la persona."""


class ReturnExpenseReportParams(TypedDict):
    note: str
    """Qué debe corregir: se le manda a la persona."""


class CreateExpenseItemParams(TypedDict):
    uuid: NotRequired[str]
    """El UUID de una factura recibida del emisor (GET /v1/sat_invoices): la fecha, el monto, el proveedor y la forma de pago salen de ella."""
    category: Literal["hospedaje", "alimentos", "avion", "transporte", "auto", "combustible", "comidas", "papeleria", "mensajeria", "software", "otros"]
    """De qué es: hospedaje, alimentos, avion, transporte, auto, combustible (gasolina, casetas y estacionamiento), comidas (en restaurante, fuera de viaje), papeleria, mensajeria, software u otros."""
    date: NotRequired[str]
    """Cuándo se gastó. Con uuid, la fecha de la factura."""
    description: NotRequired[str | None]
    """Qué fue (el proveedor). Con uuid, su emisor."""
    amount: NotRequired[float]
    """En pesos. Con uuid, el total de la factura."""
    foreign_amount: NotRequired[float | None]
    """En su moneda, si fue en otra."""
    foreign_currency: NotRequired[str | None]
    """La moneda (USD, EUR…)."""
    people: NotRequired[int]
    """En alimentos, cuántas personas comieron: el tope es por persona."""
    payment: NotRequired[Literal["tarjeta_empresa", "tarjeta_propia", "efectivo", "transferencia", "otro"] | None]
    """Cómo se pagó: tarjeta_empresa (no se le reembolsa), tarjeta_propia, efectivo, transferencia u otro."""
    receipt: NotRequired[Literal["cfdi", "extranjero", "ticket", "ninguno"]]
    """Su comprobante: cfdi, extranjero, ticket o ninguno. Con uuid, cfdi."""
    note: NotRequired[str | None]
    """Por qué, si pasa la política (la política puede pedirla)."""


class UpdateExpenseItemParams(TypedDict):
    category: NotRequired[Literal["hospedaje", "alimentos", "avion", "transporte", "auto", "combustible", "comidas", "papeleria", "mensajeria", "software", "otros"]]
    """De qué es: hospedaje, alimentos, avion, transporte, auto, combustible (gasolina, casetas y estacionamiento), comidas (en restaurante, fuera de viaje), papeleria, mensajeria, software u otros."""
    date: NotRequired[str]
    """Cuándo se gastó. Con uuid, la fecha de la factura."""
    description: NotRequired[str | None]
    """Qué fue (el proveedor). Con uuid, su emisor."""
    amount: NotRequired[float]
    """En pesos. Con uuid, el total de la factura."""
    foreign_amount: NotRequired[float | None]
    """En su moneda, si fue en otra."""
    foreign_currency: NotRequired[str | None]
    """La moneda (USD, EUR…)."""
    people: NotRequired[int]
    """En alimentos, cuántas personas comieron: el tope es por persona."""
    payment: NotRequired[Literal["tarjeta_empresa", "tarjeta_propia", "efectivo", "transferencia", "otro"] | None]
    """Cómo se pagó: tarjeta_empresa (no se le reembolsa), tarjeta_propia, efectivo, transferencia u otro."""
    receipt: NotRequired[Literal["cfdi", "extranjero", "ticket", "ninguno"]]
    """Su comprobante: cfdi, extranjero, ticket o ninguno. Con uuid, cfdi."""
    note: NotRequired[str | None]
    """Por qué, si pasa la política (la política puede pedirla)."""
    rejected: NotRequired[bool]
    """Al aprobar: true lo rechaza (no se paga ni se deduce), false lo vuelve a incluir. Solo en una comprobación enviada."""
    reject_reason: NotRequired[str | None]
    """Por qué se rechaza."""


class CreateExpenseMovementParams(TypedDict):
    kind: Literal["anticipo", "reembolso", "devolucion"]
    """anticipo (dinero que se le da antes o durante; hasta que se aprueba), reembolso (lo que la empresa le debe, ya aprobada) o devolucion (lo que le sobró, ya aprobada)."""
    amount: float
    """En pesos."""
    date: str
    """Cuándo se pagó."""
    method: NotRequired[Literal["transferencia", "efectivo", "tarjeta", "nomina"]]
    """transferencia (por omisión), efectivo, tarjeta o nomina (en el siguiente recibo de nómina del empleado; solo si está en Nómina)."""
    reference: NotRequired[str | None]
    """Su referencia (folio de la transferencia)."""


class GetExpensePolicyParams(TypedDict):
    """Los parámetros de GET /v1/expense_policy."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class UpdateExpensePolicyParamsLimitsValue(TypedDict):
    domestic: float | None
    """En México; null sin tope."""
    abroad: float | None
    """En el extranjero; null sin tope."""
    per: Literal["dia", "gasto"]
    """dia (al día y por persona) o gasto."""


class UpdateExpensePolicyParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…). Por omisión, su único emisor."""
    limits: NotRequired[dict[str, UpdateExpensePolicyParamsLimitsValue | None]]
    """Topes por categoría. Una categoría con null deja de tener tope; las que no manda no cambian. Un gasto que pase un tope no se rechaza: se marca para quien aprueba."""
    ticket_limit: NotRequired[float]
    """Hasta cuánto se acepta un gasto sin factura; 0: todos la piden."""
    due_days: NotRequired[int]
    """Días después del regreso para comprobar."""
    note_over_limit: NotRequired[bool]
    """Pedir una nota en cada gasto que pase un tope."""
    notify_approvers: NotRequired[bool]
    """Avisar por correo a quien aprueba cuando le envían una comprobación."""
    notify_people: NotRequired[bool]
    """Avisar a la persona cuando se aprueba, se devuelve o se le paga."""


class CreateCustomerParamsForeign(TypedDict):
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class CreateCustomerParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: NotRequired[str | None]
    """Correo del cliente (varios separados por comas), a donde van sus facturas con send_email."""
    use: NotRequired[str]
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    foreign: NotRequired[CreateCustomerParamsForeign | None]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    group: NotRequired[str | None]
    """Su grupo de clientes (cgr_…), o null para ninguno."""
    price_list: NotRequired[str | None]
    """Su propia lista de precios (prl_…), que gana sobre la de su grupo; null: la de su grupo o la de todos."""
    discount_percent: NotRequired[float | None]
    """Su propio descuento en cada concepto, en %; null: el de su grupo."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class ListCustomersParams(TypedDict):
    """Los parámetros de GET /v1/customers."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    tax_id: NotRequired[str]
    """Solo el de este RFC."""


class UpdateCustomerParamsForeign(TypedDict):
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class UpdateCustomerParams(TypedDict):
    tax_id: NotRequired[str]
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: NotRequired[str]
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: NotRequired[str]
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: NotRequired[str]
    """Código postal del domicilio fiscal, 5 dígitos, como en la constancia de situación fiscal. El de un emisor es el lugar de expedición (LugarExpedicion) de sus comprobantes."""
    email: NotRequired[str | None]
    """Correo del cliente (varios separados por comas), a donde van sus facturas con send_email."""
    use: NotRequired[str]
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    foreign: NotRequired[UpdateCustomerParamsForeign | None]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    group: NotRequired[str | None]
    """Su grupo de clientes (cgr_…), o null para ninguno."""
    price_list: NotRequired[str | None]
    """Su propia lista de precios (prl_…), que gana sobre la de su grupo; null: la de su grupo o la de todos."""
    discount_percent: NotRequired[float | None]
    """Su propio descuento en cada concepto, en %; null: el de su grupo."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class CreateCustomerDataRequestParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…) que va a facturarle. Por omisión, su único emisor."""
    reference: NotRequired[str]
    """Su id para este cliente o pedido, como «Pedido 1042». El cliente la ve arriba del formulario y viene de vuelta en el evento."""
    description: NotRequired[str]
    """Una línea que el cliente ve arriba del formulario: para qué son sus datos."""
    expires_in_days: NotRequired[int]
    """Días que la liga sirve, de 1 a 60. Por omisión 60."""


class ListCustomerDataRequestsParams(TypedDict):
    """Los parámetros de GET /v1/customer_data_requests."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class CreateProductParamsLocalTaxesItem(TypedDict):
    retention: bool
    """true si es una retención local; false si es un traslado."""
    name: str
    """Nombre del impuesto local (ImpLocTrasladado o ImpLocRetenido), como ISH."""
    rate: float
    """Tasa en por ciento (TasadeTraslado o TasadeRetencion)."""


class CreateProductParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    name: NotRequired[str | None]
    """Nombre corto para encontrarlo, solo para usted; en el CFDI va description."""
    description: str
    """Descripción."""
    product_key: str
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: NotRequired[str | None]
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: NotRequired[str | None]
    """Número de identificación o SKU (NoIdentificacion)."""
    unit_price: NotRequired[float]
    """Precio unitario antes de impuestos (ValorUnitario)."""
    open_price: NotRequired[bool]
    """Precio abierto: sin precio fijo (una noche de hotel que cambia cada día); cada factura manda su unit_price."""
    taxability: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: NotRequired[float | None]
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: NotRequired[Literal["Tasa", "Cuota"]]
    """Tasa o Cuota (TipoFactor del IEPS)."""
    iva_retention: NotRequired[float]
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: NotRequired[float]
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""
    local_taxes: NotRequired[list[CreateProductParamsLocalTaxesItem]]
    """Impuestos locales que lleva, como el ISH 3% de hospedaje: van en cada factura con él, sobre sus conceptos."""
    track_stock: NotRequired[bool]
    """Lleva existencias (Inventario): cada factura que lo vende las saca del almacén de su sucursal, y una cancelada las regresa. Ver GET /v1/products/{id}/stock."""
    cost: NotRequired[float | None]
    """Su costo por unidad en pesos sin IVA, hasta que sus compras den otro: vale las existencias que entran sin unit_cost."""
    barcode: NotRequired[str | None]
    """Código de barras (EAN, UPC o el suyo). Una factura cuyo concepto lo trae como NoIdentificacion saca existencias de este producto."""
    min_stock: NotRequired[float | None]
    """Existencia mínima: por debajo, el aviso de existencias bajas lo incluye."""
    portal_visible: NotRequired[bool]
    """Se vende en el Portal del cliente: sus clientes lo piden desde ahí, a sus precios (listas de precios), y el pedido llega por confirmar."""
    min_order_qty: NotRequired[float | None]
    """Lo menos que se le pide desde el portal, en su unidad."""
    order_step: NotRequired[float | None]
    """Se pide de tantos en tantos desde el portal (12: de 12 en 12)."""
    category: NotRequired[str | None]
    """Su categoría, con las de arriba separadas por › (también > o /): «Ferretería › Tornillos». Si no existe, se crea. null la quita."""


class ListProductsParams(TypedDict):
    """Los parámetros de GET /v1/products."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    sku: NotRequired[str]
    """Solo el de este SKU."""
    product_key: NotRequired[str]
    """Solo los de esta clave del SAT."""
    category: NotRequired[str]
    """Solo los de esta categoría y sus subcategorías: «Ferretería» o «Ferretería › Tornillos»."""


class UpdateProductParamsLocalTaxesItem(TypedDict):
    retention: bool
    """true si es una retención local; false si es un traslado."""
    name: str
    """Nombre del impuesto local (ImpLocTrasladado o ImpLocRetenido), como ISH."""
    rate: float
    """Tasa en por ciento (TasadeTraslado o TasadeRetencion)."""


class UpdateProductParams(TypedDict):
    name: NotRequired[str | None]
    """Nombre corto para encontrarlo, solo para usted; en el CFDI va description."""
    description: NotRequired[str]
    """Descripción."""
    product_key: NotRequired[str]
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: NotRequired[str | None]
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: NotRequired[str | None]
    """Número de identificación o SKU (NoIdentificacion)."""
    unit_price: NotRequired[float]
    """Precio unitario antes de impuestos (ValorUnitario)."""
    open_price: NotRequired[bool]
    """Precio abierto: sin precio fijo (una noche de hotel que cambia cada día); cada factura manda su unit_price."""
    taxability: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: NotRequired[float | None]
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: NotRequired[Literal["Tasa", "Cuota"]]
    """Tasa o Cuota (TipoFactor del IEPS)."""
    iva_retention: NotRequired[float]
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: NotRequired[float]
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""
    local_taxes: NotRequired[list[UpdateProductParamsLocalTaxesItem]]
    """Impuestos locales que lleva, como el ISH 3% de hospedaje: van en cada factura con él, sobre sus conceptos."""
    track_stock: NotRequired[bool]
    """Lleva existencias (Inventario): cada factura que lo vende las saca del almacén de su sucursal, y una cancelada las regresa. Ver GET /v1/products/{id}/stock."""
    cost: NotRequired[float | None]
    """Su costo por unidad en pesos sin IVA, hasta que sus compras den otro: vale las existencias que entran sin unit_cost."""
    barcode: NotRequired[str | None]
    """Código de barras (EAN, UPC o el suyo). Una factura cuyo concepto lo trae como NoIdentificacion saca existencias de este producto."""
    min_stock: NotRequired[float | None]
    """Existencia mínima: por debajo, el aviso de existencias bajas lo incluye."""
    portal_visible: NotRequired[bool]
    """Se vende en el Portal del cliente: sus clientes lo piden desde ahí, a sus precios (listas de precios), y el pedido llega por confirmar."""
    min_order_qty: NotRequired[float | None]
    """Lo menos que se le pide desde el portal, en su unidad."""
    order_step: NotRequired[float | None]
    """Se pide de tantos en tantos desde el portal (12: de 12 en 12)."""
    category: NotRequired[str | None]
    """Su categoría, con las de arriba separadas por › (también > o /): «Ferretería › Tornillos». Si no existe, se crea. null la quita."""


class ListSatMailboxMessagesParams(TypedDict):
    """Los parámetros de GET /v1/sat_mailbox_messages."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    unread: NotRequired[bool]
    """true para solo los no leídos en el SAT, false para los leídos."""


class ListSatFindingsParams(TypedDict):
    """Los parámetros de GET /v1/sat_findings."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    direction: NotRequired[Literal["issued", "received"]]
    """issued (emitidos) o received (recibidos); sin él, los dos."""
    date_gte: NotRequired[str]
    """CFDI desde este día (AAAA-MM-DD)."""
    date_lte: NotRequired[str]
    """CFDI hasta este día (AAAA-MM-DD, completo)."""
    severity: NotRequired[Literal["critical", "warning", "info"]]
    """Solo los de esta gravedad: critical, warning o info."""
    counterparty: NotRequired[str]
    """Solo los CFDI de este proveedor o cliente (su RFC): qué hallazgos tiene."""


class ListSatFindingCounterpartiesParams(TypedDict):
    """Los parámetros de GET /v1/sat_finding_counterparties."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    direction: NotRequired[Literal["issued", "received"]]
    """issued (emitidos: clientes) o received (recibidos: proveedores); sin él, los dos."""
    date_gte: NotRequired[str]
    """CFDI desde este día (AAAA-MM-DD)."""
    date_lte: NotRequired[str]
    """CFDI hasta este día (AAAA-MM-DD, completo)."""
    severity: NotRequired[Literal["critical", "warning", "info"]]
    """Solo los de esta gravedad: critical, warning o info."""
    code: NotRequired[str]
    """Solo quienes tienen este hallazgo (efos_definitivo, cancelado, regla_12…; el code de GET /v1/sat_findings)."""


class ListWarehousesParams(TypedDict):
    """Los parámetros de GET /v1/warehouses."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    include_archived: NotRequired[bool]
    """true para incluir los archivados."""


class ListWarehouseStockParams(TypedDict):
    """Los parámetros de GET /v1/warehouses/{id}/stock."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    include_empty: NotRequired[bool]
    """true para incluir los productos con track_stock que están en 0."""


class ListStockMovementsParams(TypedDict):
    """Los parámetros de GET /v1/stock_movements."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    product: NotRequired[str]
    """Solo los de este producto (prd_…)."""
    warehouse: NotRequired[str]
    """Solo los de este almacén (whs_…)."""
    type: NotRequired[Literal["sale", "purchase", "customer_return", "supplier_return", "adjustment", "count", "transfer_out", "transfer_in", "initial", "cost", "reversal"]]
    """Solo los de este tipo."""
    date_gte: NotRequired[str]
    """Desde este día (AAAA-MM-DD) u hora (AAAA-MM-DDTHH:MM:SS) de la Ciudad de México."""
    date_lte: NotRequired[str]
    """Hasta este día (completo) u hora de la Ciudad de México."""


class CreateStockAdjustmentParamsLinesItem(TypedDict):
    product: str
    """El producto (prd_…), con track_stock: true."""
    quantity: float
    """Cuánto entra (positivo) o sale (negativo), en la unidad del producto."""
    unit_cost: NotRequired[float]
    """Lo que costó cada unidad que entra, en pesos sin IVA; sin él, el costo promedio de hoy."""
    lot: NotRequired[str]
    """El lote o número de serie, si el producto los lleva."""
    expires_on: NotRequired[str]
    """La caducidad de un lote nuevo (AAAA-MM-DD)."""


class CreateStockAdjustmentParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…). Por omisión, su único emisor."""
    warehouse: NotRequired[str]
    """El almacén (whs_…). Por omisión, el de la Matriz."""
    reason: Literal["shrinkage", "theft", "damage", "expiration", "internal_use", "gift", "initial", "surplus", "count", "other"]
    """Por qué: shrinkage (merma), theft (robo o extravío), damage (daño), expiration (caducidad), internal_use (uso interno), gift (muestra o regalo), initial (inventario inicial), surplus (sobrante), count (conteo físico) u other."""
    note: NotRequired[str | None]
    """Una nota, para el kárdex."""
    lines: list[CreateStockAdjustmentParamsLinesItem]
    """Lo que entra o sale de cada producto, hasta 500 líneas."""


class ListStockAdjustmentsParams(TypedDict):
    """Los parámetros de GET /v1/stock_adjustments."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    warehouse: NotRequired[str]
    """Solo los de este almacén (whs_…)."""
    status: NotRequired[Literal["applied", "pending", "rejected", "reversed"]]
    """applied, pending, rejected o reversed."""


class GetSatCatalogParams(TypedDict):
    """Los parámetros de GET /v1/sat_catalogs/{name}."""
    q: NotRequired[str]
    """Qué buscar: palabras («consultoría») o una clave."""
    limit: NotRequired[int]
    """Hasta cuántos, de 1 a 100 (búsquedas). Por omisión 20."""


class CheckSatListsParams(TypedDict):
    tax_ids: list[str]
    """Los RFC a revisar, hasta 1000."""


CreateSatDownloadParams = TypedDict(
    "CreateSatDownloadParams",
    {
        "issuer": "NotRequired[str]",
        "direction": "NotRequired[Literal[\"received\", \"issued\"]]",
        "from": "str",
        "to": "str",
        "type": "NotRequired[Literal[\"I\", \"E\", \"P\", \"T\", \"N\"]]",
        "counterparty_tax_id": "NotRequired[str]",
        "uuid": "NotRequired[str]",
    },
)


class ListSatDownloadsParams(TypedDict):
    """Los parámetros de GET /v1/sat_downloads."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class ListSatInvoicesParams(TypedDict):
    """Los parámetros de GET /v1/sat_invoices."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    direction: NotRequired[Literal["received", "issued"]]
    """received (por omisión) o issued."""
    type: NotRequired[Literal["I", "E", "P", "T", "N"]]
    """I, E, P, T o N."""
    counterparty_tax_id: NotRequired[str]
    """El RFC de quien la emitió (recibidas) o de quien la recibió (emitidas)."""
    date_gte: NotRequired[str]
    """Con fecha desde este día (AAAA-MM-DD)."""
    date_lte: NotRequired[str]
    """Con fecha hasta este día (AAAA-MM-DD), incluido."""
    cost_center: NotRequired[str]
    """Solo las de este centro de costo (ccn_…), o none para las que no tienen."""


class UpdateSatInvoiceParams(TypedDict):
    cost_center: NotRequired[str | None]
    """Su centro de costo (ccn_…), o null para quitárselo. Los complementos de pago y los traslados no llevan."""


class ListSatRetentionsParams(TypedDict):
    """Los parámetros de GET /v1/sat_retentions."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    direction: NotRequired[Literal["received", "issued"]]
    """received (por omisión) o issued."""
    status: NotRequired[Literal["active", "canceled"]]
    """active o canceled. Sin él, las dos."""
    counterparty_tax_id: NotRequired[str]
    """El RFC de quien retuvo (recibidas) o a quien le retuvo (emitidas)."""
    code: NotRequired[str]
    """Clave de la retención (CveRetenc) de dos dígitos, como 16 o 26."""
    year: NotRequired[int]
    """Solo las de un ejercicio, como 2025."""
    month: NotRequired[int]
    """Solo las que cubren este mes (1 a 12): una anual de enero a diciembre cubre todos."""


class ListPortalSuppliersParams(TypedDict):
    """Los parámetros de GET /v1/portal_suppliers."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["invited", "onboarding", "in_review", "approved", "rejected", "suspended"]]
    """Solo los que estén en este estado."""
    tax_id: NotRequired[str]
    """Solo el de este RFC."""


class ListSupplierInvoicesParams(TypedDict):
    """Los parámetros de GET /v1/supplier_invoices."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["received", "approved", "scheduled", "paid", "rejected"]]
    """Solo las que estén en este estado."""
    supplier: NotRequired[str]
    """Solo las de este proveedor (sup_…)."""
    received_since: NotRequired[str]
    """Solo las que llegaron desde este día (AAAA-MM-DD)."""


class ScheduleSupplierInvoiceParams(TypedDict):
    pay_on: str
    """El día en que la pagará (AAAA-MM-DD, hoy o después). El proveedor lo ve."""


class MarkSupplierInvoicePaidParams(TypedDict):
    paid_on: str
    """El día en que la pagó (AAAA-MM-DD, hoy o antes)."""
    reference: NotRequired[str | None]
    """La referencia del pago (la de la transferencia o del ERP), o null."""


class RefreshSatDeclarationsParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…). Por omisión, su único emisor."""


class ListSatDeclarationsParams(TypedDict):
    """Los parámetros de GET /v1/sat_declarations."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    year: NotRequired[int]
    """Solo las de un ejercicio, como 2025."""
    source: NotRequired[Literal["monthly", "annual", "dyp"]]
    """monthly (provisionales o definitivas), annual (la anual) o dyp (Declaraciones y pagos)."""
    month: NotRequired[int]
    """Solo las de un mes (1 a 12)."""
    type: NotRequired[Literal["normal", "complementary"]]
    """normal o complementary (complementarias)."""


class GetSatDeclarationCalendarParams(TypedDict):
    """Los parámetros de GET /v1/sat_declarations/calendar."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    year: NotRequired[int]
    """El ejercicio, como 2026. Por omisión, el actual."""


class CreateTicketParamsBuyer(TypedDict):
    """Quién pagó, para reconocer la venta en Tickets. No es el receptor de la factura (eso lo escribe el comprador en el portal) y no se le manda nada."""
    name: NotRequired[str]
    """Su nombre o el de su empresa, como lo conoce su sistema."""
    email: NotRequired[str]
    """Su correo."""


class CreateTicketParamsLinesItem(TypedDict):
    product: NotRequired[str]
    """Un producto (prd_…) de su catálogo: sus claves, IVA e impuestos locales."""
    description: NotRequired[str]
    """El concepto. Con `product`, reemplaza su descripción; sin él, va con `product_key`."""
    product_key: NotRequired[str]
    """c_ClaveProdServ (8 dígitos), si no usa `product`."""
    unit_key: NotRequired[str]
    """c_ClaveUnidad. Por omisión, la de la clave del producto."""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA incluida en su total. Por omisión 0.16."""
    quantity: NotRequired[float]
    """Unidades (noches, piezas). Por omisión 1."""
    total: float
    """Lo que se cobró por este concepto, impuestos incluidos."""


class CreateTicketParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…) que vendió. Por omisión, su único emisor."""
    folio: str
    """El folio de la venta en su sistema, único por emisor: letras, números, - _ / y punto. Registrar el mismo folio con el mismo total responde el ticket que ya existe."""
    total: NotRequired[float]
    """Lo que se cobró, impuestos incluidos y sin propina. Con `lines` puede omitirlo (es su suma); si lo manda, debe ser igual."""
    tip: NotRequired[float]
    """Propina: no va en la factura. El cliente puede escribir el total con ella o sin ella."""
    payment_form: str
    """c_FormaPago de la venta: 01 efectivo, 04 tarjeta de crédito…"""
    sold_at: NotRequired[str]
    """Cuándo se vendió: ISO 8601 (2026-10-02T13:45:00-06:00) o la hora de la Ciudad de México sin zona. Por omisión, ahora."""
    product: NotRequired[str]
    """Un producto (prd_…) de su catálogo: el concepto de la factura."""
    description: NotRequired[str]
    """El concepto. Con `product`, reemplaza su descripción; sin él, va con `product_key`."""
    product_key: NotRequired[str]
    """c_ClaveProdServ (8 dígitos), si no usa `product`."""
    unit_key: NotRequired[str]
    """c_ClaveUnidad. Por omisión, la de la clave del producto."""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA incluida en el total. Por omisión 0.16."""
    buyer: NotRequired[CreateTicketParamsBuyer]
    """Quién pagó, para reconocer la venta en Tickets. No es el receptor de la factura (eso lo escribe el comprador en el portal) y no se le manda nada."""
    lines: NotRequired[list[CreateTicketParamsLinesItem]]
    """Una venta de varios conceptos (el folio de un hotel: noches, desayunos, lavandería), cada uno con su producto o sus claves, sus impuestos y lo que se cobró por él; hasta 200. En lugar de `product`, `description`, `product_key`, `unit_key` e `iva`. La factura del cliente lleva un concepto por línea; la factura global, uno por cada combinación de impuestos del ticket."""


class ListTicketsParams(TypedDict):
    """Los parámetros de GET /v1/tickets."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["pending", "invoiced", "global", "cancelled"]]
    """pending, invoiced, global o cancelled."""
    sold_at_gte: NotRequired[str]
    """Vendidos desde (ISO 8601 o AAAA-MM-DD)."""
    sold_at_lte: NotRequired[str]
    """Vendidos hasta (ISO 8601 o AAAA-MM-DD, el día completo)."""


class UpdateSelfInvoicingParams(TypedDict):
    window: NotRequired[Literal["month", "days"]]
    """Hasta cuándo se puede facturar un ticket: `month`, hasta el fin del mes de la venta (lo usual ante el SAT); `days`, `window_days` días después."""
    window_days: NotRequired[int]
    """Días para facturar con `window: days`."""
    global_periodicity: NotRequired[Literal["01", "02", "03", "04"]]
    """c_Periodicidad de la factura global con los tickets que nadie facturó: 01 diaria, 02 semanal, 03 quincenal, 04 mensual."""
    global_invoice: NotRequired[Literal["auto", "off"]]
    """`auto` (por omisión): los tickets que nadie facturó van solos a la factura global al terminar su periodo. `off`: Fiscalisto no hace factura global de los tickets (por ejemplo, porque su punto de venta ya la hace); quedan pendientes y usted responde por ellos ante el SAT."""
    ask_total: NotRequired[bool]
    """`true` (por omisión): el comprador busca su ticket con el código y el total. `false`: solo con el código (sus 4 caracteres al azar; cada ticket se bloquea tras varios intentos fallidos)."""
    portal_title: NotRequired[str | None]
    """El título del portal, en lugar de «Facture su ticket». `null` lo quita."""
    portal_message: NotRequired[str | None]
    """Un mensaje bajo el título (instrucciones, horario, a quién escribir). `null` lo quita."""
    code_hint: NotRequired[str | None]
    """Dónde encuentra el comprador su código, bajo el campo («Viene en su correo de salida»). `null` pone el de Fiscalisto."""
    portal_theme: NotRequired[Literal["auto", "light", "dark"]]
    """El tema del portal: `auto` (por omisión), el del dispositivo del comprador, que puede cambiarlo; `light` o `dark`, siempre ese. Vale en su página, sus QR y dentro de su sitio (salvo que el código para incrustarlo elija otro)."""
    portal_accent: NotRequired[str | None]
    """El color de los botones del portal, como `#0b7c77`. `null` pone el de Fiscalisto."""
    portal_radius: NotRequired[int | None]
    """Lo redondo de las esquinas del portal, en píxeles (0 a 24). `null` pone el de Fiscalisto (10)."""


class ListJournalEntriesParams(TypedDict):
    """Los parámetros de GET /v1/accounting/journal_entries."""
    month: str
    """El mes (AAAA-MM)."""
    limit: NotRequired[int]
    """Cuántas por página, de 1 a 1,000. Por omisión 100."""
    starting_after: NotRequired[str]
    """El id de la última póliza de la página anterior."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class GetTrialBalanceParams(TypedDict):
    """Los parámetros de GET /v1/accounting/trial_balance."""
    month: str
    """El mes (AAAA-MM)."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class GetFinancialStatementsParams(TypedDict):
    """Los parámetros de GET /v1/accounting/financial_statements."""
    month: str
    """El mes (AAAA-MM)."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class GetCrossChecksParams(TypedDict):
    """Los parámetros de GET /v1/accounting/cross_checks."""
    year: NotRequired[int]
    """El ejercicio. Por omisión, el actual."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class GetVatRefundParams(TypedDict):
    """Los parámetros de GET /v1/accounting/vat_refund."""
    month: NotRequired[str]
    """El mes del saldo a revisar (AAAA-MM). Sin él, solo los saldos."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class GetCrossCheckCfdiParams(TypedDict):
    """Los parámetros de GET /v1/accounting/cross_checks/cfdi."""
    month: str
    """El mes (AAAA-MM), cuya declaración ya venció."""
    key: Literal["vat_charged", "vat_creditable", "vat_withheld", "isr_income", "isr_withheld_salaries", "isr_withheld_suppliers", "vat_withheld_suppliers"]
    """La cifra: vat_charged, vat_creditable, vat_withheld, isr_income, isr_withheld_salaries, isr_withheld_suppliers o vat_withheld_suppliers."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class ListLedgerAccountsParams(TypedDict):
    """Los parámetros de GET /v1/accounting/accounts."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class GetElectronicAccountingParams(TypedDict):
    """Los parámetros de GET /v1/accounting/electronic_accounting."""
    month: str
    """El mes (AAAA-MM)."""
    type: NotRequired[Literal["normal", "complementary"]]
    """normal (BN, por omisión) o complementary (BC, con modified_on)."""
    modified_on: NotRequired[str]
    """complementary: el día en que se modificó (AAAA-MM-DD)."""
    journal_request: NotRequired[Literal["AF", "FC", "DE", "CO"]]
    """Para incluir las pólizas: AF acto de fiscalización, FC fiscalización compulsa (con order_number), DE devolución o CO compensación (con procedure_number)."""
    order_number: NotRequired[str]
    """AF y FC: el número de orden (ABC1234567/26)."""
    procedure_number: NotRequired[str]
    """DE y CO: el número de trámite (AB123456789012)."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class GetDiotParams(TypedDict):
    """Los parámetros de GET /v1/accounting/diot."""
    month: str
    """El mes (AAAA-MM)."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class GetDiotFileParams(TypedDict):
    """Los parámetros de GET /v1/accounting/diot/file."""
    month: str
    """El mes (AAAA-MM)."""
    group_small_suppliers: NotRequired[bool]
    """true para agrupar proveedores de hasta $50,000 en el mes (regla 4.5.2)."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class CreateStoreConnectionParamsSettings(TypedDict):
    """Cómo se vuelve ticket cada pedido."""
    product_key: NotRequired[str]
    """c_ClaveProdServ de lo que vende (8 dígitos)."""
    unit_key: NotRequired[str]
    """c_ClaveUnidad. Por omisión, la de la clave del producto."""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA incluida en los precios. Por omisión 0.16."""
    description: NotRequired[str]
    """El concepto de cada ticket. Por omisión, el pedido y sus artículos («Pedido 1001: Playera (2), Gorra»)."""
    folio_prefix: NotRequired[str]
    """Lo que va antes del número del pedido en el folio del ticket. Por omisión SHOP- o ML-."""
    payment_form: NotRequired[str]
    """c_FormaPago cuando la forma de pago del pedido no está en payment_forms. Por omisión 04 (Shopify) o 31 (Mercado Libre)."""
    payment_forms: NotRequired[dict[str, str]]
    """c_FormaPago por pasarela de Shopify (shopify_payments, paypal, manual…) o tipo de pago de Mercado Libre (credit_card, debit_card, account_money, ticket, bank_transfer)."""
    auto_invoice: NotRequired[bool]
    """Mercado Libre: timbrar en cuanto se paga si el comprador dejó sus datos fiscales completos. Por omisión true."""
    notify_buyer: NotRequired[bool]
    """WooCommerce y Tiendanube: mandar al comprador el enlace para facturar (WooCommerce, como nota al cliente del pedido; Tiendanube, por correo). Por omisión true."""


class CreateStoreConnectionParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…) dueño de la tienda. Por omisión, su único emisor."""
    platform: Literal["shopify", "mercadolibre", "amazon", "tiendanube", "woocommerce"]
    """shopify, woocommerce, mercadolibre, tiendanube o amazon."""
    shop: NotRequired[str]
    """Shopify: el dominio de la tienda (mi-tienda.myshopify.com)."""
    client_id: NotRequired[str]
    """Shopify: el Client ID de la app de la tienda (Dev Dashboard)."""
    client_secret: NotRequired[str]
    """Shopify: el Client secret de esa app; con él se firman los webhooks. Se guarda cifrado y nunca se muestra."""
    access_token: NotRequired[str]
    """Shopify, solo apps personalizadas antiguas: su token de la Admin API (shpat_…); client_secret es entonces su API secret key."""
    site: NotRequired[str]
    """WooCommerce: la dirección de la tienda (https://mitienda.com)."""
    consumer_key: NotRequired[str]
    """WooCommerce: la Clave de cliente (ck_…) de una llave de la API REST con permisos de Lectura/Escritura."""
    consumer_secret: NotRequired[str]
    """WooCommerce: la Clave secreta de cliente (cs_…) de esa llave. Se guarda cifrada y nunca se muestra."""
    return_url: NotRequired[str]
    """Mercado Libre, Tiendanube y Amazon: a dónde volver después de autorizar (se agregan store_connection y status)."""
    settings: NotRequired[CreateStoreConnectionParamsSettings]
    """Cómo se vuelve ticket cada pedido."""


class ListStoreConnectionsParams(TypedDict):
    """Los parámetros de GET /v1/store_connections."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""


class UpdateStoreConnectionParamsSettings(TypedDict):
    """Lo que cambia; lo demás queda."""
    product_key: NotRequired[str]
    """c_ClaveProdServ de lo que vende (8 dígitos)."""
    unit_key: NotRequired[str]
    """c_ClaveUnidad. Por omisión, la de la clave del producto."""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA incluida en los precios. Por omisión 0.16."""
    description: NotRequired[str]
    """El concepto de cada ticket. Por omisión, el pedido y sus artículos («Pedido 1001: Playera (2), Gorra»)."""
    folio_prefix: NotRequired[str]
    """Lo que va antes del número del pedido en el folio del ticket. Por omisión SHOP- o ML-."""
    payment_form: NotRequired[str]
    """c_FormaPago cuando la forma de pago del pedido no está en payment_forms. Por omisión 04 (Shopify) o 31 (Mercado Libre)."""
    payment_forms: NotRequired[dict[str, str]]
    """c_FormaPago por pasarela de Shopify (shopify_payments, paypal, manual…) o tipo de pago de Mercado Libre (credit_card, debit_card, account_money, ticket, bank_transfer)."""
    auto_invoice: NotRequired[bool]
    """Mercado Libre: timbrar en cuanto se paga si el comprador dejó sus datos fiscales completos. Por omisión true."""
    notify_buyer: NotRequired[bool]
    """WooCommerce y Tiendanube: mandar al comprador el enlace para facturar (WooCommerce, como nota al cliente del pedido; Tiendanube, por correo). Por omisión true."""


class UpdateStoreConnectionParams(TypedDict):
    settings: UpdateStoreConnectionParamsSettings
    """Lo que cambia; lo demás queda."""


class ImportStoreOrdersParams(TypedDict):
    since: NotRequired[str]
    """Desde qué día (AAAA-MM-DD, hasta 31 días atrás). Por omisión, hace 7 días."""


class CreateRecurringInvoiceParamsSchedule(TypedDict):
    """Cada cuánto y a qué hora se timbra."""
    frequency: Literal["monthly", "weekly", "daily"]
    """monthly: cada interval meses en day_of_month. weekly o daily: cada interval semanas o días desde start_date."""
    interval: NotRequired[int]
    """Cada cuántos meses, semanas o días. Por omisión 1. Hasta 24 meses, 52 semanas o 365 días."""
    day_of_month: NotRequired[int | Literal["last"]]
    """Con monthly: el día, del 1 al 28, o "last" (el último del mes). Por omisión el día de start_date, o el de hoy."""
    start_date: NotRequired[str]
    """La primera factura, AAAA-MM-DD (hoy o después). Por omisión: con monthly, el próximo day_of_month; con weekly o daily, hoy."""
    hour: NotRequired[int]
    """La hora (0 a 23) en que se timbra, en time_zone. Por omisión 7."""
    time_zone: NotRequired[Literal["America/Mexico_City", "America/Cancun", "America/Mazatlan", "America/Hermosillo", "America/Tijuana", "America/Ciudad_Juarez"]]
    """La zona de esa hora. Por omisión America/Mexico_City."""


class CreateRecurringInvoiceParams(TypedDict):
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    name: str
    """Para reconocerla: «Renta oficina 3», «Plan Pro de ACME»."""
    schedule: CreateRecurringInvoiceParamsSchedule
    """Cada cuánto y a qué hora se timbra."""
    invoice: CreateRecurringInvoiceParamsInvoice
    """La factura que se repite: el cuerpo de POST /v1/invoices, sin issuer, folio, date, global ni metadata. En description puede usar {mes}, {mes anterior}, {mes siguiente}, {año}, {año anterior}, {año siguiente} y {periodo}: cada factura los llena con su fecha. Como se escriben es como salen: {mes} «noviembre», {Mes} «Noviembre», {MES} «NOVIEMBRE»."""
    send_email: NotRequired[bool]
    """Mandar cada factura al correo del cliente (customer.email o el del catálogo). Por omisión true."""
    catch_up: NotRequired[Literal["all", "latest"]]
    """Si quedaron periodos sin timbrar (sin timbres, en pausa con su fecha pasada): all los timbra todos, cada uno con su mes; latest solo el más reciente. Por omisión all."""


class ListRecurringInvoicesParams(TypedDict):
    """Los parámetros de GET /v1/recurring_invoices."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["active", "paused"]]
    """active o paused."""


class UpdateRecurringInvoiceParamsSchedule(TypedDict):
    """Cada cuánto y a qué hora se timbra."""
    frequency: NotRequired[Literal["monthly", "weekly", "daily"]]
    """monthly: cada interval meses en day_of_month. weekly o daily: cada interval semanas o días desde start_date."""
    interval: NotRequired[int]
    """Cada cuántos meses, semanas o días. Por omisión 1. Hasta 24 meses, 52 semanas o 365 días."""
    day_of_month: NotRequired[int | Literal["last"]]
    """Con monthly: el día, del 1 al 28, o "last" (el último del mes). Por omisión el día de start_date, o el de hoy."""
    start_date: NotRequired[str]
    """La primera factura, AAAA-MM-DD (hoy o después). Por omisión: con monthly, el próximo day_of_month; con weekly o daily, hoy."""
    hour: NotRequired[int]
    """La hora (0 a 23) en que se timbra, en time_zone. Por omisión 7."""
    time_zone: NotRequired[Literal["America/Mexico_City", "America/Cancun", "America/Mazatlan", "America/Hermosillo", "America/Tijuana", "America/Ciudad_Juarez"]]
    """La zona de esa hora. Por omisión America/Mexico_City."""


class UpdateRecurringInvoiceParams(TypedDict):
    name: NotRequired[str]
    """Nombre."""
    schedule: NotRequired[UpdateRecurringInvoiceParamsSchedule]
    """Cada cuánto y a qué hora se timbra."""
    invoice: NotRequired[UpdateRecurringInvoiceParamsInvoice]
    """La factura completa que se repite desde la siguiente vez (reemplaza la anterior)."""
    send_email: NotRequired[bool]
    """true para mandar el PDF y el XML por correo al timbrar, con el diseño de Fiscalisto. Por omisión no se envía."""
    catch_up: NotRequired[Literal["all", "latest"]]
    """Si quedaron periodos sin timbrar: all los timbra todos, cada uno con su mes; latest solo el más reciente."""
    active: NotRequired[bool]
    """false la pausa; true la reanuda desde hoy, sin timbrar las fechas que pasaron en pausa."""


class CreateQuoteParamsCustomer1Foreign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class CreateQuoteParamsCustomer1(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal del cliente (DomicilioFiscalReceptor), 5 dígitos."""
    email: NotRequired[str | None]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    foreign: NotRequired[CreateQuoteParamsCustomer1Foreign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class CreateQuoteParamsCustomer2(TypedDict):
    name: str
    """A quién va dirigida."""
    email: NotRequired[str]
    """Su correo (hasta 5, separados por comas)."""


class CreateQuoteParamsItemsItemThirdParty(TypedDict):
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    tax_id: str
    """RFC de a cuenta de quién (RfcACuentaTerceros)."""
    name: str
    """Nombre (NombreACuentaTerceros)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscalACuentaTerceros), c_RegimenFiscal."""
    zip: str
    """Código postal de su domicilio fiscal (DomicilioFiscalACuentaTerceros)."""


class CreateQuoteParamsItemsItemIedu(TypedDict):
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    student_name: str
    """Nombre del alumno (nombreAlumno)."""
    curp: str
    """CURP, 18 caracteres."""
    level: Literal["Preescolar", "Primaria", "Secundaria", "Profesional técnico", "Bachillerato o su equivalente"]
    """Nivel educativo (nivelEducativo)."""
    rvoe: str
    """Reconocimiento de validez oficial de estudios (autRVOE)."""
    payer_tax_id: NotRequired[str | None]
    """RFC de quien paga, si no es el receptor (rfcPago)."""


class CreateQuoteParamsItemsItemUsedVehicleCustomsItem(TypedDict):
    number: str
    """Número del documento de importación (numero)."""
    date: str
    """Fecha del documento (fecha), AAAA-MM-DD."""
    office: NotRequired[str]
    """Aduana (aduana)."""


class CreateQuoteParamsItemsItemUsedVehicle(TypedDict):
    """Complemento de vehículo usado."""
    purchase_amount: float
    """Monto de adquisición (montoAdquisicion)."""
    sale_amount: float
    """Monto de enajenación (montoEnajenacion)."""
    vehicle_key: str
    """Clave vehicular (claveVehicular)."""
    make: str
    """Marca (marca)."""
    type: str
    """Tipo o versión (tipo)."""
    model: str
    """Año del modelo (modelo), 4 dígitos."""
    engine_number: NotRequired[str]
    """Número de motor (numeroMotor)."""
    serial_number: NotRequired[str]
    """Número de serie (numeroSerie)."""
    niv: NotRequired[str]
    """Número de identificación vehicular (NIV)."""
    guide_value: float
    """Valor según la guía EBC o Libro Azul (valor)."""
    customs: NotRequired[list[CreateQuoteParamsItemsItemUsedVehicleCustomsItem]]
    """Información aduanera de la importación del vehículo (InformacionAduanera)."""


class CreateQuoteParamsItemsItem(TypedDict):
    """Un concepto. description, product_key y unit_price son obligatorios, salvo que mande product (prd_…): entonces vienen de su catálogo y lo que mande encima gana."""
    product: NotRequired[str]
    """Un producto de su catálogo (prd_…): toma su clave, unidad, precio e impuestos."""
    description: NotRequired[str]
    """Descripción del concepto (Descripcion), hasta 1,000 caracteres."""
    product_key: NotRequired[str]
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: NotRequired[str | None]
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: NotRequired[str | None]
    """Número de identificación o SKU (NoIdentificacion)."""
    quantity: NotRequired[float]
    """Cantidad (Cantidad). Por omisión 1."""
    unit_price: NotRequired[float]
    """Precio unitario antes de impuestos (ValorUnitario)."""
    discount: NotRequired[float]
    """Descuento (Descuento)."""
    taxability: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: NotRequired[float]
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: NotRequired[Literal["Tasa", "Cuota"]]
    """Tasa o Cuota (TipoFactor del IEPS)."""
    ieps_units: NotRequired[float]
    """Unidades de IEPS a cuota (litros, cigarros…), si no son la cantidad."""
    iva_retention: NotRequired[float]
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: NotRequired[float]
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""
    predial: NotRequired[list[str]]
    """Números de cuenta predial (CuentaPredial) en arrendamiento."""
    pedimentos: NotRequired[list[str]]
    """Números de pedimento (InformacionAduanera) de mercancía importada."""
    third_party: NotRequired[CreateQuoteParamsItemsItemThirdParty]
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    iedu: NotRequired[CreateQuoteParamsItemsItemIedu]
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    used_vehicle: NotRequired[CreateQuoteParamsItemsItemUsedVehicle]
    """Complemento de vehículo usado."""
    addenda: NotRequired[dict[str, str]]
    """Addenda del receptor (Walmart, Soriana…), con sus propios campos."""


class CreateQuoteParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    customer: str | CreateQuoteParamsCustomer1 | CreateQuoteParamsCustomer2
    """Un cliente de su catálogo (cus_…), uno con sus datos fiscales (como en POST /v1/invoices: se agrega a sus clientes) o solo name y email si aún no los tiene."""
    items: list[CreateQuoteParamsItemsItem]
    """Los conceptos, como en POST /v1/invoices."""
    currency: NotRequired[str]
    """Moneda, clave ISO 4217 de c_Moneda (MXN, USD, EUR…). Por omisión MXN."""
    exchange_rate: NotRequired[float]
    """Tipo de cambio a pesos (TipoCambio). Obligatorio si la moneda no es MXN; use el del DOF del día anterior."""
    payment_form: NotRequired[str]
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    payment_method: NotRequired[Literal["PUE", "PPD"]]
    """Método de pago (MetodoPago): PUE (una sola exhibición, por omisión) o PPD (en parcialidades o diferido, se cobra con complementos de pago)."""
    use: NotRequired[str]
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    notes: NotRequired[str]
    """Observaciones que aparecen en el PDF (no van en el XML)."""
    valid_until: NotRequired[str]
    """Hasta cuándo es válida (AAAA-MM-DD, hasta un año). Por omisión, en 15 días."""
    terms: NotRequired[str]
    """Condiciones: tiempo de entrega, anticipo, garantía…"""
    auto_invoice: NotRequired[bool]
    """Al aceptarla, timbrar la factura sola (con los datos fiscales del cliente; si no los tiene, la página se los pide primero). Por omisión false: la factura se timbra con POST /v1/quotes/{id}/invoice."""


class ListQuotesParams(TypedDict):
    """Los parámetros de GET /v1/quotes."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["draft", "sent", "viewed", "accepted", "rejected", "withdrawn", "expired", "invoiced"]]
    """Solo las que estén en este estado."""


class UpdateQuoteParamsCustomer1Foreign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class UpdateQuoteParamsCustomer1(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal del cliente (DomicilioFiscalReceptor), 5 dígitos."""
    email: NotRequired[str | None]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    foreign: NotRequired[UpdateQuoteParamsCustomer1Foreign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class UpdateQuoteParamsCustomer2(TypedDict):
    name: str
    """A quién va dirigida."""
    email: NotRequired[str]
    """Su correo (hasta 5, separados por comas)."""


class UpdateQuoteParamsItemsItemThirdParty(TypedDict):
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    tax_id: str
    """RFC de a cuenta de quién (RfcACuentaTerceros)."""
    name: str
    """Nombre (NombreACuentaTerceros)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscalACuentaTerceros), c_RegimenFiscal."""
    zip: str
    """Código postal de su domicilio fiscal (DomicilioFiscalACuentaTerceros)."""


class UpdateQuoteParamsItemsItemIedu(TypedDict):
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    student_name: str
    """Nombre del alumno (nombreAlumno)."""
    curp: str
    """CURP, 18 caracteres."""
    level: Literal["Preescolar", "Primaria", "Secundaria", "Profesional técnico", "Bachillerato o su equivalente"]
    """Nivel educativo (nivelEducativo)."""
    rvoe: str
    """Reconocimiento de validez oficial de estudios (autRVOE)."""
    payer_tax_id: NotRequired[str | None]
    """RFC de quien paga, si no es el receptor (rfcPago)."""


class UpdateQuoteParamsItemsItemUsedVehicleCustomsItem(TypedDict):
    number: str
    """Número del documento de importación (numero)."""
    date: str
    """Fecha del documento (fecha), AAAA-MM-DD."""
    office: NotRequired[str]
    """Aduana (aduana)."""


class UpdateQuoteParamsItemsItemUsedVehicle(TypedDict):
    """Complemento de vehículo usado."""
    purchase_amount: float
    """Monto de adquisición (montoAdquisicion)."""
    sale_amount: float
    """Monto de enajenación (montoEnajenacion)."""
    vehicle_key: str
    """Clave vehicular (claveVehicular)."""
    make: str
    """Marca (marca)."""
    type: str
    """Tipo o versión (tipo)."""
    model: str
    """Año del modelo (modelo), 4 dígitos."""
    engine_number: NotRequired[str]
    """Número de motor (numeroMotor)."""
    serial_number: NotRequired[str]
    """Número de serie (numeroSerie)."""
    niv: NotRequired[str]
    """Número de identificación vehicular (NIV)."""
    guide_value: float
    """Valor según la guía EBC o Libro Azul (valor)."""
    customs: NotRequired[list[UpdateQuoteParamsItemsItemUsedVehicleCustomsItem]]
    """Información aduanera de la importación del vehículo (InformacionAduanera)."""


class UpdateQuoteParamsItemsItem(TypedDict):
    """Un concepto. description, product_key y unit_price son obligatorios, salvo que mande product (prd_…): entonces vienen de su catálogo y lo que mande encima gana."""
    product: NotRequired[str]
    """Un producto de su catálogo (prd_…): toma su clave, unidad, precio e impuestos."""
    description: NotRequired[str]
    """Descripción del concepto (Descripcion), hasta 1,000 caracteres."""
    product_key: NotRequired[str]
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: NotRequired[str | None]
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: NotRequired[str | None]
    """Número de identificación o SKU (NoIdentificacion)."""
    quantity: NotRequired[float]
    """Cantidad (Cantidad). Por omisión 1."""
    unit_price: NotRequired[float]
    """Precio unitario antes de impuestos (ValorUnitario)."""
    discount: NotRequired[float]
    """Descuento (Descuento)."""
    taxability: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: NotRequired[float]
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: NotRequired[Literal["Tasa", "Cuota"]]
    """Tasa o Cuota (TipoFactor del IEPS)."""
    ieps_units: NotRequired[float]
    """Unidades de IEPS a cuota (litros, cigarros…), si no son la cantidad."""
    iva_retention: NotRequired[float]
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: NotRequired[float]
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""
    predial: NotRequired[list[str]]
    """Números de cuenta predial (CuentaPredial) en arrendamiento."""
    pedimentos: NotRequired[list[str]]
    """Números de pedimento (InformacionAduanera) de mercancía importada."""
    third_party: NotRequired[UpdateQuoteParamsItemsItemThirdParty]
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    iedu: NotRequired[UpdateQuoteParamsItemsItemIedu]
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    used_vehicle: NotRequired[UpdateQuoteParamsItemsItemUsedVehicle]
    """Complemento de vehículo usado."""
    addenda: NotRequired[dict[str, str]]
    """Addenda del receptor (Walmart, Soriana…), con sus propios campos."""


class UpdateQuoteParams(TypedDict):
    customer: NotRequired[str | UpdateQuoteParamsCustomer1 | UpdateQuoteParamsCustomer2]
    """Un cliente de su catálogo (cus_…), uno con sus datos fiscales (como en POST /v1/invoices: se agrega a sus clientes) o solo name y email si aún no los tiene."""
    items: NotRequired[list[UpdateQuoteParamsItemsItem]]
    """Los conceptos, como en POST /v1/invoices."""
    currency: NotRequired[str]
    """Moneda, clave ISO 4217 de c_Moneda (MXN, USD, EUR…). Por omisión MXN."""
    exchange_rate: NotRequired[float]
    """Tipo de cambio a pesos (TipoCambio). Obligatorio si la moneda no es MXN; use el del DOF del día anterior."""
    payment_form: NotRequired[str]
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    payment_method: NotRequired[Literal["PUE", "PPD"]]
    """Método de pago (MetodoPago): PUE (una sola exhibición, por omisión) o PPD (en parcialidades o diferido, se cobra con complementos de pago)."""
    use: NotRequired[str]
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    notes: NotRequired[str]
    """Observaciones que aparecen en el PDF (no van en el XML)."""
    valid_until: NotRequired[str]
    """Hasta cuándo es válida (AAAA-MM-DD, hasta un año). Por omisión, en 15 días."""
    terms: NotRequired[str]
    """Condiciones: tiempo de entrega, anticipo, garantía…"""


class SendQuoteParams(TypedDict):
    send_email: NotRequired[bool]
    """Mandarla por correo, con su PDF y la liga (por omisión true). Con false solo se marca enviada y contesta url, para que usted la mande."""
    to: NotRequired[str]
    """A quién (hasta 5 correos). Por omisión, el correo del cliente."""
    message: NotRequired[str]
    """Un mensaje en el correo."""
    auto_invoice: NotRequired[bool]
    """Al aceptarla, timbrar la factura sola (con los datos fiscales del cliente; si no los tiene, la página se los pide primero). Por omisión false: la factura se timbra con POST /v1/quotes/{id}/invoice."""
    remind: NotRequired[bool]
    """Recordarle por correo, a los mismos destinatarios, 3 días antes de su último día si no ha respondido (una vez). Solo al mandarla por correo; por omisión false."""


class WithdrawQuoteParams(TypedDict):
    note: NotRequired[str]
    """Por qué (queda en customer_comment; el cliente no la ve)."""


class RejectQuoteParams(TypedDict):
    note: NotRequired[str]
    """Por qué (queda en customer_comment; el cliente no la ve)."""


class CreateSalesOrderParamsCustomerForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class CreateSalesOrderParamsCustomer(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal del cliente (DomicilioFiscalReceptor), 5 dígitos."""
    email: NotRequired[str | None]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    foreign: NotRequired[CreateSalesOrderParamsCustomerForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class CreateSalesOrderParamsItemsItemThirdParty(TypedDict):
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    tax_id: str
    """RFC de a cuenta de quién (RfcACuentaTerceros)."""
    name: str
    """Nombre (NombreACuentaTerceros)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscalACuentaTerceros), c_RegimenFiscal."""
    zip: str
    """Código postal de su domicilio fiscal (DomicilioFiscalACuentaTerceros)."""


class CreateSalesOrderParamsItemsItemIedu(TypedDict):
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    student_name: str
    """Nombre del alumno (nombreAlumno)."""
    curp: str
    """CURP, 18 caracteres."""
    level: Literal["Preescolar", "Primaria", "Secundaria", "Profesional técnico", "Bachillerato o su equivalente"]
    """Nivel educativo (nivelEducativo)."""
    rvoe: str
    """Reconocimiento de validez oficial de estudios (autRVOE)."""
    payer_tax_id: NotRequired[str | None]
    """RFC de quien paga, si no es el receptor (rfcPago)."""


class CreateSalesOrderParamsItemsItemUsedVehicleCustomsItem(TypedDict):
    number: str
    """Número del documento de importación (numero)."""
    date: str
    """Fecha del documento (fecha), AAAA-MM-DD."""
    office: NotRequired[str]
    """Aduana (aduana)."""


class CreateSalesOrderParamsItemsItemUsedVehicle(TypedDict):
    """Complemento de vehículo usado."""
    purchase_amount: float
    """Monto de adquisición (montoAdquisicion)."""
    sale_amount: float
    """Monto de enajenación (montoEnajenacion)."""
    vehicle_key: str
    """Clave vehicular (claveVehicular)."""
    make: str
    """Marca (marca)."""
    type: str
    """Tipo o versión (tipo)."""
    model: str
    """Año del modelo (modelo), 4 dígitos."""
    engine_number: NotRequired[str]
    """Número de motor (numeroMotor)."""
    serial_number: NotRequired[str]
    """Número de serie (numeroSerie)."""
    niv: NotRequired[str]
    """Número de identificación vehicular (NIV)."""
    guide_value: float
    """Valor según la guía EBC o Libro Azul (valor)."""
    customs: NotRequired[list[CreateSalesOrderParamsItemsItemUsedVehicleCustomsItem]]
    """Información aduanera de la importación del vehículo (InformacionAduanera)."""


class CreateSalesOrderParamsItemsItem(TypedDict):
    """Un concepto. description, product_key y unit_price son obligatorios, salvo que mande product (prd_…): entonces vienen de su catálogo y lo que mande encima gana."""
    product: NotRequired[str]
    """Un producto de su catálogo (prd_…): toma su clave, unidad, precio e impuestos."""
    description: NotRequired[str]
    """Descripción del concepto (Descripcion), hasta 1,000 caracteres."""
    product_key: NotRequired[str]
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: NotRequired[str | None]
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: NotRequired[str | None]
    """Número de identificación o SKU (NoIdentificacion)."""
    quantity: NotRequired[float]
    """Cantidad (Cantidad). Por omisión 1."""
    unit_price: NotRequired[float]
    """Precio unitario antes de impuestos (ValorUnitario)."""
    discount: NotRequired[float]
    """Descuento (Descuento)."""
    taxability: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: NotRequired[float]
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: NotRequired[Literal["Tasa", "Cuota"]]
    """Tasa o Cuota (TipoFactor del IEPS)."""
    ieps_units: NotRequired[float]
    """Unidades de IEPS a cuota (litros, cigarros…), si no son la cantidad."""
    iva_retention: NotRequired[float]
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: NotRequired[float]
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""
    predial: NotRequired[list[str]]
    """Números de cuenta predial (CuentaPredial) en arrendamiento."""
    pedimentos: NotRequired[list[str]]
    """Números de pedimento (InformacionAduanera) de mercancía importada."""
    third_party: NotRequired[CreateSalesOrderParamsItemsItemThirdParty]
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    iedu: NotRequired[CreateSalesOrderParamsItemsItemIedu]
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    used_vehicle: NotRequired[CreateSalesOrderParamsItemsItemUsedVehicle]
    """Complemento de vehículo usado."""
    addenda: NotRequired[dict[str, str]]
    """Addenda del receptor (Walmart, Soriana…), con sus propios campos."""


class CreateSalesOrderParams(TypedDict):
    issuer: NotRequired[str]
    """Emisor (iss_…). Si la llave tiene un solo emisor o la cuenta tiene uno solo, puede omitirse."""
    quote: NotRequired[str]
    """Hacerlo de una cotización (quo_…): toma su cliente y sus conceptos, y la cotización queda aceptada. Sin customer ni items."""
    customer: NotRequired[str | CreateSalesOrderParamsCustomer]
    """Un cliente de su catálogo (cus_…) o uno con sus datos fiscales (como en POST /v1/invoices: se agrega a sus clientes)."""
    items: NotRequired[list[CreateSalesOrderParamsItemsItem]]
    """Los conceptos, como en POST /v1/invoices (hasta 200)."""
    confirm: NotRequired[bool]
    """Confirmarlo en el mismo paso (por omisión false: queda en draft). Confirmado, aparta lo pedido en el almacén."""
    currency: NotRequired[str]
    """Moneda, clave ISO 4217 de c_Moneda (MXN, USD, EUR…). Por omisión MXN."""
    exchange_rate: NotRequired[float]
    """Tipo de cambio a pesos (TipoCambio). Obligatorio si la moneda no es MXN; use el del DOF del día anterior."""
    payment_form: NotRequired[str]
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    payment_method: NotRequired[Literal["PUE", "PPD"]]
    """Método de pago (MetodoPago): PUE (una sola exhibición, por omisión) o PPD (en parcialidades o diferido, se cobra con complementos de pago)."""
    use: NotRequired[str]
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    notes: NotRequired[str]
    """Observaciones que aparecen en el PDF (no van en el XML)."""
    customer_po: NotRequired[str]
    """El número de orden de compra de su cliente (va en la nota de cada factura)."""
    email: NotRequired[str]
    """A dónde mandarle el pedido y sus remisiones (hasta 5 correos, separados por comas). Por omisión, el del cliente."""
    expected_on: NotRequired[str]
    """Entrega estimada (AAAA-MM-DD)."""
    payment_days: NotRequired[int]
    """Días de crédito (0: de contado)."""
    invoice_policy: NotRequired[Literal["delivered", "ordered"]]
    """Qué se factura: delivered (por omisión), lo ya entregado; ordered, todo lo pedido desde el inicio (por ejemplo con pago por adelantado)."""
    ship_to: NotRequired[str]
    """Dónde se entrega."""
    terms: NotRequired[str]
    """Condiciones del pedido."""
    internal_note: NotRequired[str]
    """Nota interna (su cliente no la ve)."""


class ListSalesOrdersParams(TypedDict):
    """Los parámetros de GET /v1/sales_orders."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    issuer: NotRequired[str]
    """El emisor (iss_…). Puede omitirse si la llave o la cuenta tienen uno solo."""
    status: NotRequired[Literal["draft", "confirmed", "partially_delivered", "delivered", "invoiced", "paid", "closed", "canceled"]]
    """Solo los que estén en este estado."""
    customer: NotRequired[str]
    """Solo los de este RFC."""


class UpdateSalesOrderParamsCustomerForeign(TypedDict):
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    country: str
    """País de residencia fiscal, clave de 3 letras de c_Pais (USA, CAN…)."""
    tax_id: str
    """Número de registro de identidad fiscal en su país (NumRegIdTrib)."""


class UpdateSalesOrderParamsCustomer(TypedDict):
    tax_id: str
    """RFC (Rfc), 12 caracteres una persona moral y 13 una física."""
    legal_name: str
    """Nombre o razón social tal como está en la constancia de situación fiscal, sin el régimen de capital (sin «S.A. de C.V.»)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscal), clave de c_RegimenFiscal: 601, 612, 626…"""
    zip: str
    """Código postal del domicilio fiscal del cliente (DomicilioFiscalReceptor), 5 dígitos."""
    email: NotRequired[str | None]
    """Correo a donde se envía (varios separados por comas). Solo se usa si se pide enviarlo."""
    foreign: NotRequired[UpdateSalesOrderParamsCustomerForeign]
    """Si es extranjero: su país de residencia (ResidenciaFiscal, c_Pais) y su número de registro tributario (NumRegIdTrib), con el RFC genérico XEXX010101000."""
    ieps_taxpayer: NotRequired[bool]
    """true si el cliente es contribuyente de IEPS: el IEPS va desglosado en vez de sumado al precio."""


class UpdateSalesOrderParamsItemsItemThirdParty(TypedDict):
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    tax_id: str
    """RFC de a cuenta de quién (RfcACuentaTerceros)."""
    name: str
    """Nombre (NombreACuentaTerceros)."""
    tax_system: str
    """Régimen fiscal (RegimenFiscalACuentaTerceros), c_RegimenFiscal."""
    zip: str
    """Código postal de su domicilio fiscal (DomicilioFiscalACuentaTerceros)."""


class UpdateSalesOrderParamsItemsItemIedu(TypedDict):
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    student_name: str
    """Nombre del alumno (nombreAlumno)."""
    curp: str
    """CURP, 18 caracteres."""
    level: Literal["Preescolar", "Primaria", "Secundaria", "Profesional técnico", "Bachillerato o su equivalente"]
    """Nivel educativo (nivelEducativo)."""
    rvoe: str
    """Reconocimiento de validez oficial de estudios (autRVOE)."""
    payer_tax_id: NotRequired[str | None]
    """RFC de quien paga, si no es el receptor (rfcPago)."""


class UpdateSalesOrderParamsItemsItemUsedVehicleCustomsItem(TypedDict):
    number: str
    """Número del documento de importación (numero)."""
    date: str
    """Fecha del documento (fecha), AAAA-MM-DD."""
    office: NotRequired[str]
    """Aduana (aduana)."""


class UpdateSalesOrderParamsItemsItemUsedVehicle(TypedDict):
    """Complemento de vehículo usado."""
    purchase_amount: float
    """Monto de adquisición (montoAdquisicion)."""
    sale_amount: float
    """Monto de enajenación (montoEnajenacion)."""
    vehicle_key: str
    """Clave vehicular (claveVehicular)."""
    make: str
    """Marca (marca)."""
    type: str
    """Tipo o versión (tipo)."""
    model: str
    """Año del modelo (modelo), 4 dígitos."""
    engine_number: NotRequired[str]
    """Número de motor (numeroMotor)."""
    serial_number: NotRequired[str]
    """Número de serie (numeroSerie)."""
    niv: NotRequired[str]
    """Número de identificación vehicular (NIV)."""
    guide_value: float
    """Valor según la guía EBC o Libro Azul (valor)."""
    customs: NotRequired[list[UpdateSalesOrderParamsItemsItemUsedVehicleCustomsItem]]
    """Información aduanera de la importación del vehículo (InformacionAduanera)."""


class UpdateSalesOrderParamsItemsItem(TypedDict):
    """Un concepto. description, product_key y unit_price son obligatorios, salvo que mande product (prd_…): entonces vienen de su catálogo y lo que mande encima gana."""
    product: NotRequired[str]
    """Un producto de su catálogo (prd_…): toma su clave, unidad, precio e impuestos."""
    description: NotRequired[str]
    """Descripción del concepto (Descripcion), hasta 1,000 caracteres."""
    product_key: NotRequired[str]
    """Clave del producto o servicio (ClaveProdServ), 8 dígitos de c_ClaveProdServ. Búsquela con GET /v1/sat_catalogs/product_keys?q=…"""
    unit_key: NotRequired[str]
    """Clave de unidad (ClaveUnidad) de c_ClaveUnidad: E48 unidad de servicio (por omisión), H87 pieza, ACT actividad…"""
    unit_name: NotRequired[str | None]
    """Nombre de la unidad (Unidad), hasta 20 caracteres."""
    sku: NotRequired[str | None]
    """Número de identificación o SKU (NoIdentificacion)."""
    quantity: NotRequired[float]
    """Cantidad (Cantidad). Por omisión 1."""
    unit_price: NotRequired[float]
    """Precio unitario antes de impuestos (ValorUnitario)."""
    discount: NotRequired[float]
    """Descuento (Descuento)."""
    taxability: NotRequired[Literal["01", "02", "03", "04", "05", "06", "07", "08"]]
    """Objeto de impuesto (ObjetoImp), c_ObjetoImp: 01 no objeto, 02 sí objeto (por omisión), 03 sin desglose, 04 no causa…"""
    iva: NotRequired[Literal["0", "0.16", "0.08", "exento"]]
    """Tasa de IVA trasladado: 0.16 (por omisión), 0.08 (región fronteriza), 0 o exento."""
    ieps: NotRequired[float]
    """IEPS trasladado: tasa (0.265…) o cuota en pesos por unidad, según ieps_factor."""
    ieps_factor: NotRequired[Literal["Tasa", "Cuota"]]
    """Tasa o Cuota (TipoFactor del IEPS)."""
    ieps_units: NotRequired[float]
    """Unidades de IEPS a cuota (litros, cigarros…), si no son la cantidad."""
    iva_retention: NotRequired[float]
    """Tasa de IVA retenido (por ejemplo 0.106667, dos terceras partes del 16%)."""
    isr_retention: NotRequired[float]
    """Tasa de ISR retenido (por ejemplo 0.10 honorarios, 0.0125 RESICO)."""
    predial: NotRequired[list[str]]
    """Números de cuenta predial (CuentaPredial) en arrendamiento."""
    pedimentos: NotRequired[list[str]]
    """Números de pedimento (InformacionAduanera) de mercancía importada."""
    third_party: NotRequired[UpdateSalesOrderParamsItemsItemThirdParty]
    """A cuenta de terceros (ACuentaTerceros): RFC, nombre, régimen y código postal."""
    iedu: NotRequired[UpdateSalesOrderParamsItemsItemIedu]
    """Complemento de instituciones educativas privadas (IEDU): alumno, CURP, nivel y RVOE."""
    used_vehicle: NotRequired[UpdateSalesOrderParamsItemsItemUsedVehicle]
    """Complemento de vehículo usado."""
    addenda: NotRequired[dict[str, str]]
    """Addenda del receptor (Walmart, Soriana…), con sus propios campos."""


class UpdateSalesOrderParams(TypedDict):
    customer: NotRequired[str | UpdateSalesOrderParamsCustomer]
    """Un cliente de su catálogo (cus_…) o uno con sus datos fiscales (como en POST /v1/invoices: se agrega a sus clientes)."""
    items: NotRequired[list[UpdateSalesOrderParamsItemsItem]]
    """Los conceptos, como en POST /v1/invoices (hasta 200)."""
    currency: NotRequired[str]
    """Moneda, clave ISO 4217 de c_Moneda (MXN, USD, EUR…). Por omisión MXN."""
    exchange_rate: NotRequired[float]
    """Tipo de cambio a pesos (TipoCambio). Obligatorio si la moneda no es MXN; use el del DOF del día anterior."""
    payment_form: NotRequired[str]
    """Forma de pago (FormaPago), clave de c_FormaPago: 01 efectivo, 03 transferencia, 04 tarjeta de crédito, 28 débito, 99 por definir… Obligatoria con PUE; con PPD es 99."""
    payment_method: NotRequired[Literal["PUE", "PPD"]]
    """Método de pago (MetodoPago): PUE (una sola exhibición, por omisión) o PPD (en parcialidades o diferido, se cobra con complementos de pago)."""
    use: NotRequired[str]
    """Uso del CFDI (UsoCFDI), clave de c_UsoCFDI. Por omisión G03, o S01 con régimen 616."""
    notes: NotRequired[str]
    """Observaciones que aparecen en el PDF (no van en el XML)."""
    customer_po: NotRequired[str]
    """El número de orden de compra de su cliente (va en la nota de cada factura)."""
    email: NotRequired[str]
    """A dónde mandarle el pedido y sus remisiones (hasta 5 correos, separados por comas). Por omisión, el del cliente."""
    expected_on: NotRequired[str]
    """Entrega estimada (AAAA-MM-DD)."""
    payment_days: NotRequired[int]
    """Días de crédito (0: de contado)."""
    invoice_policy: NotRequired[Literal["delivered", "ordered"]]
    """Qué se factura: delivered (por omisión), lo ya entregado; ordered, todo lo pedido desde el inicio (por ejemplo con pago por adelantado)."""
    ship_to: NotRequired[str]
    """Dónde se entrega."""
    terms: NotRequired[str]
    """Condiciones del pedido."""
    internal_note: NotRequired[str]
    """Nota interna (su cliente no la ve)."""


class CreateSalesOrderDeliveryParamsItemsItem(TypedDict):
    line: int
    """El id del concepto (items[].id)."""
    quantity: float
    """Cantidad (Cantidad). Por omisión 1."""


class CreateSalesOrderDeliveryParams(TypedDict):
    items: NotRequired[list[CreateSalesOrderDeliveryParamsItemsItem]]
    """Cuánto sale de cada concepto. Por omisión, todo lo que falta por entregar."""
    delivered_on: NotRequired[str]
    """Por omisión, hoy."""
    carrier: NotRequired[str]
    """Transporte."""
    tracking: NotRequired[str]
    """Número de guía."""
    note: NotRequired[str]
    """Una nota en la remisión."""
    received_by: NotRequired[str]
    """Quién recibió, si ya lo sabe (si no, su cliente lo firma en url)."""


class CancelSalesOrderDeliveryParams(TypedDict):
    reason: NotRequired[str]
    """Por qué (queda en el historial)."""


class InvoiceSalesOrderParamsItemsItem(TypedDict):
    line: int
    """El id del concepto (items[].id)."""
    quantity: float
    """Cantidad (Cantidad). Por omisión 1."""


class InvoiceSalesOrderParams(TypedDict):
    items: NotRequired[list[InvoiceSalesOrderParamsItemsItem]]
    """Cuánto facturar de cada concepto. Por omisión, lo entregado sin facturar (o todo lo pedido con invoice_policy ordered)."""
    include_undelivered: NotRequired[bool]
    """Facturar también lo que aún no se entrega (con invoice_policy delivered)."""
    deliver: NotRequired[bool]
    """Registrar también la entrega de lo que lleva la factura al timbrarla (venta de mostrador)."""


class SendSalesOrderParams(TypedDict):
    send_email: NotRequired[bool]
    """Mandarlo por correo, con su PDF y url (por omisión true). Con false solo contesta url, para que usted la mande."""
    to: NotRequired[str]
    """A quién (hasta 5 correos). Por omisión, el correo del pedido."""
    message: NotRequired[str]
    """Qué pasó y cómo corregirlo, para una persona."""


class CloseSalesOrderParams(TypedDict):
    reason: NotRequired[str]
    """Por qué (queda en el historial)."""


class CancelSalesOrderParams(TypedDict):
    reason: NotRequired[str]
    """Por qué (queda en el historial)."""


class CreateWebhookEndpointParams(TypedDict):
    url: str
    """Dirección https de su servidor que recibe los avisos."""
    events: NotRequired[list[str] | None]
    """Eventos que quiere recibir, o ["*"] para todos (por omisión). La lista con cuándo llega cada uno: [Tipos de evento](https://fiscalisto.com/docs/api/webhooks#tipos-de-evento)."""
    description: NotRequired[str | None]
    """Para qué es, para usted (no se manda en los eventos)."""
    api_version: NotRequired[str | None]
    """La versión de la API en que llegan sus eventos (por ejemplo 2026-10-24); null o sin mandar: la de la cuenta. Así actualiza un endpoint a la vez."""


class ListWebhookEndpointsParams(TypedDict):
    """Los parámetros de GET /v1/webhook_endpoints."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""


class UpdateWebhookEndpointParams(TypedDict):
    url: NotRequired[str]
    """Dirección https de su servidor que recibe los avisos."""
    events: NotRequired[list[str] | None]
    """Eventos que quiere recibir, o ["*"] para todos (por omisión). La lista con cuándo llega cada uno: [Tipos de evento](https://fiscalisto.com/docs/api/webhooks#tipos-de-evento)."""
    description: NotRequired[str | None]
    """Para qué es, para usted (no se manda en los eventos)."""
    disabled: NotRequired[bool]
    """true para apagarlo sin borrarlo."""
    api_version: NotRequired[str | None]
    """La versión de la API en que llegan sus eventos (por ejemplo 2026-10-24); null o sin mandar: la de la cuenta. Así actualiza un endpoint a la vez."""


class RollWebhookSecretParams(TypedDict):
    previous_secret_expires_in: NotRequired[int]
    """Segundos que el secreto anterior sigue firmando, de 0 (deja de firmar ya: úselo si se filtró) a 86400. Por omisión 86400 (24 horas)."""


class TestWebhookEndpointParams(TypedDict):
    type: NotRequired[Literal["invoice.stamped", "invoice.failed", "invoice.canceled", "invoice.cancellation_pending", "invoice.cancellation_rejected", "invoice.paid", "invoice.partially_paid", "invoice.email_bounced", "invoice.email_complained", "retention.stamped", "retention.failed", "retention.canceled", "invoice_batch.completed", "payroll_batch.completed", "customer_data_request.completed", "sat_download.completed", "sat_download.failed", "sat_declaration.created", "sat_declaration.updated", "ticket.invoiced", "ticket.included_in_global", "recurring_invoice.failed", "quote.viewed", "quote.accepted", "quote.changes_requested", "quote.rejected", "quote.withdrawn", "sales_order.confirmed", "sales_order.customer_confirmed", "sales_order.delivered", "sales_order.paid", "sales_order.canceled", "supplier_invoice.received", "supplier_invoice.approved", "supplier_invoice.rejected", "supplier_invoice.scheduled", "supplier_invoice.paid", "portal_supplier.approved", "issuer.ready", "balance.low", "usage.high", "test_clock.ready"]]
    """El evento a mandar. Por omisión invoice.stamped."""


class ListEventsParams(TypedDict):
    """Los parámetros de GET /v1/events."""
    limit: NotRequired[int]
    """Cuántos por página, de 1 a 100. Por omisión 10."""
    starting_after: NotRequired[str]
    """El id del último de la página anterior, para la siguiente."""
    type: NotRequired[Literal["invoice.stamped", "invoice.failed", "invoice.canceled", "invoice.cancellation_pending", "invoice.cancellation_rejected", "invoice.paid", "invoice.partially_paid", "invoice.email_bounced", "invoice.email_complained", "retention.stamped", "retention.failed", "retention.canceled", "invoice_batch.completed", "payroll_batch.completed", "customer_data_request.completed", "sat_download.completed", "sat_download.failed", "sat_declaration.created", "sat_declaration.updated", "ticket.invoiced", "ticket.included_in_global", "recurring_invoice.failed", "quote.viewed", "quote.accepted", "quote.changes_requested", "quote.rejected", "quote.withdrawn", "sales_order.confirmed", "sales_order.customer_confirmed", "sales_order.delivered", "sales_order.paid", "sales_order.canceled", "supplier_invoice.received", "supplier_invoice.approved", "supplier_invoice.rejected", "supplier_invoice.scheduled", "supplier_invoice.paid", "portal_supplier.approved", "issuer.ready", "balance.low", "usage.high", "test_clock.ready", "invoice.*", "invoice_batch.*", "payroll_batch.*", "recurring_invoice.*", "quote.*", "sales_order.*", "supplier_invoice.*", "portal_supplier.*", "ticket.*", "retention.*", "customer_data_request.*", "sat_download.*", "sat_declaration.*", "issuer.*", "balance.*", "usage.*", "test_clock.*"]]
    """Solo de este tipo (invoice.stamped), o todos los de un recurso con un comodín (invoice.*)."""
    object: NotRequired[str]
    """Solo los de este objeto (inv_…, ret_…, bat_…)."""
    delivery_success: NotRequired[bool]
    """false: los que algún webhook no recibió (su último intento falló). true: los que recibieron todos los webhooks a los que se mandaron."""


class ApplyAdvanceParams(InvoiceCreate):
    """El cuerpo de POST /v1/invoices (la factura de lo vendido) con method y remainder."""
    method: NotRequired[Literal["egreso", "remanente"]]
    """egreso (la factura completa y después una nota de crédito por el anticipo, opción A) o remanente (la factura solo por lo que falta, opción B)."""
    remainder: NotRequired[ApplyAdvanceParamsRemainder]
    """Cómo se paga lo que falta del anticipo: ahora con su forma de pago, o después (PPD)."""


class CreatePayrollBatchParamsExternalReceiptsItem(ExternalPayrollReceiptCreate):
    """Un recibo que calculó su sistema: el cuerpo de POST /v1/payroll_receipts/external, sin issuer, metadata ni replaces, con su reference."""
    reference: NotRequired[str]
    """Su identificador de este recibo, hasta 100 caracteres."""


class CreateInvoiceBatchParamsInvoicesItem(InvoiceCreate):
    """Una factura del lote: el cuerpo de POST /v1/invoices, sin issuer, type, global ni metadata (el lote es de un emisor y de facturas de ingreso), con su reference."""
    reference: NotRequired[str]
    """Su identificador de esta factura (su número de pedido), hasta 100 caracteres."""


class CreateRecurringInvoiceParamsInvoice(InvoiceCreate):
    """La factura que se repite: el cuerpo de POST /v1/invoices, sin issuer, folio, date, global ni metadata. En description puede usar {mes}, {mes anterior}, {mes siguiente}, {año}, {año anterior}, {año siguiente} y {periodo}: cada factura los llena con su fecha. Como se escriben es como salen: {mes} «noviembre», {Mes} «Noviembre», {MES} «NOVIEMBRE»."""
    pass


class UpdateRecurringInvoiceParamsInvoice(InvoiceCreate):
    """La factura completa que se repite desde la siguiente vez (reemplaza la anterior)."""
    pass
