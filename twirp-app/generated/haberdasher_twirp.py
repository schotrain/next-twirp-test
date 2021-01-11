# -*- coding: utf-8 -*-
# Generated by https://github.com/verloop/twirpy/protoc-gen-twirpy.  DO NOT EDIT!
# source: haberdasher.proto

from google.protobuf import symbol_database as _symbol_database

from twirp.base import Endpoint
from twirp.server import TwirpServer
from twirp.client import TwirpClient

_sym_db = _symbol_database.Default()

class HaberdasherServer(TwirpServer):

	def __init__(self, *args, service, server_path_prefix="/twirp"):
		super().__init__(service=service)
		self._prefix = F"{server_path_prefix}/twirp.example.haberdasher.Haberdasher"
		self._endpoints = {
			"MakeHat": Endpoint(
				service_name="Haberdasher",
				name="MakeHat",
				function=getattr(service, "MakeHat"),
				input=_sym_db.GetSymbol("twirp.example.haberdasher.Size"),
				output=_sym_db.GetSymbol("twirp.example.haberdasher.Hat"),
			),
		}

class HaberdasherClient(TwirpClient):

	def MakeHat(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
		return self._make_request(
			url=F"{server_path_prefix}/twirp.example.haberdasher.Haberdasher/MakeHat",
			ctx=ctx,
			request=request,
			response_obj=_sym_db.GetSymbol("twirp.example.haberdasher.Hat"),
			**kwargs,
		)
