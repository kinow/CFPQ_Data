#!/usr/bin/python3

import argparse
import os

from src.tools.base import Tool
from src.tools.redis_rdf.src.redis_loader.loader import load


class RedisRDFTool(Tool):
    def init_parser(self, parser: argparse.ArgumentParser):
        parser.add_argument('--host', help='redis host name', default='localhost')
        parser.add_argument('--port', help='redis port', default=6379)

        subparsers = parser.add_subparsers()

        parser_file = subparsers.add_parser('file')
        parser_file.add_argument('RDF_PATH', help='rdf graph path')
        parser_file.add_argument('GRAPH_NAME', help='redis graph name')

        parser_dir = subparsers.add_parser('dir')
        parser_dir.add_argument('DIR_PATH')
        # logging.disable(logging.WARNING)

    def eval(self, args: argparse.Namespace):
        if 'DIR_PATH' in args:
            for file in os.listdir(args.dir_path):
                load(f'{args.dir_path}/{file}', file, args.host, args.port)
        else:
            load(args.RDF_PATH, args.GRAPH_NAME, args.host, args.port)
