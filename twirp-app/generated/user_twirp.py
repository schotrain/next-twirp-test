# -*- coding: utf-8 -*-
# Generated by https://github.com/verloop/twirpy/protoc-gen-twirpy.  DO NOT EDIT!
# source: user.proto

from google.protobuf import symbol_database as _symbol_database

from twirp.base import Endpoint
from twirp.server import TwirpServer
from twirp.client import TwirpClient

_sym_db = _symbol_database.Default()

class UserServer(TwirpServer):

	def __init__(self, *args, service, server_path_prefix="/twirp"):
		super().__init__(service=service)
		self._prefix = F"{server_path_prefix}/nextTwirpTest.user.User"
		self._endpoints = {
			"Login": Endpoint(
				service_name="User",
				name="Login",
				function=getattr(service, "Login"),
				input=_sym_db.GetSymbol("nextTwirpTest.user.LoginRequest"),
				output=_sym_db.GetSymbol("nextTwirpTest.user.LoginResponse"),
			),
		}

class UserClient(TwirpClient):

	def Login(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/nextTwirpTest.user.User/Login",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("nextTwirpTest.user.LoginResponse"),
			**kwargs,
		)
