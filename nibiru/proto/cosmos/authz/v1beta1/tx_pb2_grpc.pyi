"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import cosmos.authz.v1beta1.tx_pb2
import grpc

class MsgStub:
    """Msg defines the authz Msg service."""
    def __init__(self, channel: grpc.Channel) -> None: ...
    Grant: grpc.UnaryUnaryMultiCallable[
        cosmos.authz.v1beta1.tx_pb2.MsgGrant,
        cosmos.authz.v1beta1.tx_pb2.MsgGrantResponse]
    """Grant grants the provided authorization to the grantee on the granter's
    account with the provided expiration time. If there is already a grant
    for the given (granter, grantee, Authorization) triple, then the grant
    will be overwritten.
    """

    Exec: grpc.UnaryUnaryMultiCallable[
        cosmos.authz.v1beta1.tx_pb2.MsgExec,
        cosmos.authz.v1beta1.tx_pb2.MsgExecResponse]
    """Exec attempts to execute the provided messages using
    authorizations granted to the grantee. Each message should have only
    one signer corresponding to the granter of the authorization.
    """

    Revoke: grpc.UnaryUnaryMultiCallable[
        cosmos.authz.v1beta1.tx_pb2.MsgRevoke,
        cosmos.authz.v1beta1.tx_pb2.MsgRevokeResponse]
    """Revoke revokes any authorization corresponding to the provided method name on the
    granter's account that has been granted to the grantee.
    """


class MsgServicer(metaclass=abc.ABCMeta):
    """Msg defines the authz Msg service."""
    @abc.abstractmethod
    def Grant(self,
        request: cosmos.authz.v1beta1.tx_pb2.MsgGrant,
        context: grpc.ServicerContext,
    ) -> cosmos.authz.v1beta1.tx_pb2.MsgGrantResponse:
        """Grant grants the provided authorization to the grantee on the granter's
        account with the provided expiration time. If there is already a grant
        for the given (granter, grantee, Authorization) triple, then the grant
        will be overwritten.
        """
        pass

    @abc.abstractmethod
    def Exec(self,
        request: cosmos.authz.v1beta1.tx_pb2.MsgExec,
        context: grpc.ServicerContext,
    ) -> cosmos.authz.v1beta1.tx_pb2.MsgExecResponse:
        """Exec attempts to execute the provided messages using
        authorizations granted to the grantee. Each message should have only
        one signer corresponding to the granter of the authorization.
        """
        pass

    @abc.abstractmethod
    def Revoke(self,
        request: cosmos.authz.v1beta1.tx_pb2.MsgRevoke,
        context: grpc.ServicerContext,
    ) -> cosmos.authz.v1beta1.tx_pb2.MsgRevokeResponse:
        """Revoke revokes any authorization corresponding to the provided method name on the
        granter's account that has been granted to the grantee.
        """
        pass


def add_MsgServicer_to_server(servicer: MsgServicer, server: grpc.Server) -> None: ...