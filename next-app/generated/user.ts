// @generated by protobuf-ts 1.0.12
// @generated from protobuf file "user.proto" (package "nextTwirpTest.user", syntax proto3)
// tslint:disable
import { RpcTransport } from "@protobuf-ts/runtime-rpc";
import { MethodInfo } from "@protobuf-ts/runtime-rpc";
import { BinaryWriteOptions } from "@protobuf-ts/runtime";
import { IBinaryWriter } from "@protobuf-ts/runtime";
import { WireType } from "@protobuf-ts/runtime";
import { BinaryReadOptions } from "@protobuf-ts/runtime";
import { IBinaryReader } from "@protobuf-ts/runtime";
import { UnknownFieldHandler } from "@protobuf-ts/runtime";
import { PartialMessage } from "@protobuf-ts/runtime";
import { reflectionMergePartial } from "@protobuf-ts/runtime";
import { MessageType } from "@protobuf-ts/runtime";
import { stackIntercept } from "@protobuf-ts/runtime-rpc";
import { UnaryCall } from "@protobuf-ts/runtime-rpc";
import { RpcOptions } from "@protobuf-ts/runtime-rpc";
/**
 * @generated from protobuf message nextTwirpTest.user.UserInfo
 */
export interface UserInfo {
    /**
     * @generated from protobuf field: string id = 1;
     */
    id: string;
    /**
     * @generated from protobuf field: string email = 2;
     */
    email: string;
    /**
     * @generated from protobuf field: string givenName = 3;
     */
    givenName: string;
    /**
     * @generated from protobuf field: string familyName = 4;
     */
    familyName: string;
    /**
     * @generated from protobuf field: string imageUrl = 5;
     */
    imageUrl: string;
}
/**
 * @generated from protobuf message nextTwirpTest.user.GetAccessTokenRequest
 */
export interface GetAccessTokenRequest {
    /**
     * @generated from protobuf field: nextTwirpTest.user.IdentityProvider identityProvider = 1;
     */
    identityProvider: IdentityProvider;
    /**
     * @generated from protobuf field: string identityProviderId = 2;
     */
    identityProviderId: string;
    /**
     * @generated from protobuf field: string hmac = 3;
     */
    hmac: string;
}
/**
 * @generated from protobuf message nextTwirpTest.user.GetAccessTokenResponse
 */
export interface GetAccessTokenResponse {
    /**
     * @generated from protobuf field: string accessToken = 1;
     */
    accessToken: string;
}
/**
 * @generated from protobuf message nextTwirpTest.user.GetUserInfoRequest
 */
export interface GetUserInfoRequest {
}
/**
 * @generated from protobuf message nextTwirpTest.user.GetUserInfoResponse
 */
export interface GetUserInfoResponse {
    /**
     * @generated from protobuf field: nextTwirpTest.user.UserInfo userInfo = 1;
     */
    userInfo?: UserInfo;
}
/**
 * @generated from protobuf message nextTwirpTest.user.SaveUserInfoRequest
 */
export interface SaveUserInfoRequest {
    /**
     * @generated from protobuf field: string givenName = 1;
     */
    givenName: string;
    /**
     * @generated from protobuf field: string familyName = 2;
     */
    familyName: string;
    /**
     * @generated from protobuf field: string email = 3;
     */
    email: string;
    /**
     * @generated from protobuf field: string imageUrl = 4;
     */
    imageUrl: string;
}
/**
 * @generated from protobuf message nextTwirpTest.user.SaveUserInfoResponse
 */
export interface SaveUserInfoResponse {
    /**
     * @generated from protobuf field: nextTwirpTest.user.UserInfo userInfo = 1;
     */
    userInfo?: UserInfo;
}
/**
 * @generated from protobuf enum nextTwirpTest.user.IdentityProvider
 */
export enum IdentityProvider {
    /**
     * @generated from protobuf enum value: GOOGLE = 0;
     */
    GOOGLE = 0,
    /**
     * @generated from protobuf enum value: OKTA = 1;
     */
    OKTA = 1
}
/**
 * @generated from protobuf service nextTwirpTest.user.User
 */
export interface IUserClient {
    /**
     * @generated from protobuf rpc: getAccessToken(nextTwirpTest.user.GetAccessTokenRequest) returns (nextTwirpTest.user.GetAccessTokenResponse);
     */
    getAccessToken(input: GetAccessTokenRequest, options?: RpcOptions): UnaryCall<GetAccessTokenRequest, GetAccessTokenResponse>;
    /**
     * @generated from protobuf rpc: getUserInfo(nextTwirpTest.user.GetUserInfoRequest) returns (nextTwirpTest.user.GetUserInfoResponse);
     */
    getUserInfo(input: GetUserInfoRequest, options?: RpcOptions): UnaryCall<GetUserInfoRequest, GetUserInfoResponse>;
    /**
     * @generated from protobuf rpc: saveUserInfo(nextTwirpTest.user.SaveUserInfoRequest) returns (nextTwirpTest.user.SaveUserInfoResponse);
     */
    saveUserInfo(input: SaveUserInfoRequest, options?: RpcOptions): UnaryCall<SaveUserInfoRequest, SaveUserInfoResponse>;
}
/**
 * Type for protobuf message nextTwirpTest.user.UserInfo
 */
class UserInfo$Type extends MessageType<UserInfo> {
    constructor() {
        super("nextTwirpTest.user.UserInfo", [
            { no: 1, name: "id", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "email", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "givenName", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 4, name: "familyName", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 5, name: "imageUrl", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<UserInfo>): UserInfo {
        const message = { id: "", email: "", givenName: "", familyName: "", imageUrl: "" };
        if (value !== undefined)
            reflectionMergePartial<UserInfo>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: UserInfo): UserInfo {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string id */ 1:
                    message.id = reader.string();
                    break;
                case /* string email */ 2:
                    message.email = reader.string();
                    break;
                case /* string givenName */ 3:
                    message.givenName = reader.string();
                    break;
                case /* string familyName */ 4:
                    message.familyName = reader.string();
                    break;
                case /* string imageUrl */ 5:
                    message.imageUrl = reader.string();
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: UserInfo, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string id = 1; */
        if (message.id !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.id);
        /* string email = 2; */
        if (message.email !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.email);
        /* string givenName = 3; */
        if (message.givenName !== "")
            writer.tag(3, WireType.LengthDelimited).string(message.givenName);
        /* string familyName = 4; */
        if (message.familyName !== "")
            writer.tag(4, WireType.LengthDelimited).string(message.familyName);
        /* string imageUrl = 5; */
        if (message.imageUrl !== "")
            writer.tag(5, WireType.LengthDelimited).string(message.imageUrl);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
export const UserInfo = new UserInfo$Type();
/**
 * Type for protobuf message nextTwirpTest.user.GetAccessTokenRequest
 */
class GetAccessTokenRequest$Type extends MessageType<GetAccessTokenRequest> {
    constructor() {
        super("nextTwirpTest.user.GetAccessTokenRequest", [
            { no: 1, name: "identityProvider", kind: "enum", T: () => ["nextTwirpTest.user.IdentityProvider", IdentityProvider] },
            { no: 2, name: "identityProviderId", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "hmac", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<GetAccessTokenRequest>): GetAccessTokenRequest {
        const message = { identityProvider: 0, identityProviderId: "", hmac: "" };
        if (value !== undefined)
            reflectionMergePartial<GetAccessTokenRequest>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: GetAccessTokenRequest): GetAccessTokenRequest {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* nextTwirpTest.user.IdentityProvider identityProvider */ 1:
                    message.identityProvider = reader.int32();
                    break;
                case /* string identityProviderId */ 2:
                    message.identityProviderId = reader.string();
                    break;
                case /* string hmac */ 3:
                    message.hmac = reader.string();
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: GetAccessTokenRequest, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* nextTwirpTest.user.IdentityProvider identityProvider = 1; */
        if (message.identityProvider !== 0)
            writer.tag(1, WireType.Varint).int32(message.identityProvider);
        /* string identityProviderId = 2; */
        if (message.identityProviderId !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.identityProviderId);
        /* string hmac = 3; */
        if (message.hmac !== "")
            writer.tag(3, WireType.LengthDelimited).string(message.hmac);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
export const GetAccessTokenRequest = new GetAccessTokenRequest$Type();
/**
 * Type for protobuf message nextTwirpTest.user.GetAccessTokenResponse
 */
class GetAccessTokenResponse$Type extends MessageType<GetAccessTokenResponse> {
    constructor() {
        super("nextTwirpTest.user.GetAccessTokenResponse", [
            { no: 1, name: "accessToken", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<GetAccessTokenResponse>): GetAccessTokenResponse {
        const message = { accessToken: "" };
        if (value !== undefined)
            reflectionMergePartial<GetAccessTokenResponse>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: GetAccessTokenResponse): GetAccessTokenResponse {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string accessToken */ 1:
                    message.accessToken = reader.string();
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: GetAccessTokenResponse, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string accessToken = 1; */
        if (message.accessToken !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.accessToken);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
export const GetAccessTokenResponse = new GetAccessTokenResponse$Type();
/**
 * Type for protobuf message nextTwirpTest.user.GetUserInfoRequest
 */
class GetUserInfoRequest$Type extends MessageType<GetUserInfoRequest> {
    constructor() {
        super("nextTwirpTest.user.GetUserInfoRequest", []);
    }
    create(value?: PartialMessage<GetUserInfoRequest>): GetUserInfoRequest {
        const message = {};
        if (value !== undefined)
            reflectionMergePartial<GetUserInfoRequest>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: GetUserInfoRequest): GetUserInfoRequest {
        return target ?? this.create();
    }
    internalBinaryWrite(message: GetUserInfoRequest, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
export const GetUserInfoRequest = new GetUserInfoRequest$Type();
/**
 * Type for protobuf message nextTwirpTest.user.GetUserInfoResponse
 */
class GetUserInfoResponse$Type extends MessageType<GetUserInfoResponse> {
    constructor() {
        super("nextTwirpTest.user.GetUserInfoResponse", [
            { no: 1, name: "userInfo", kind: "message", T: () => UserInfo }
        ]);
    }
    create(value?: PartialMessage<GetUserInfoResponse>): GetUserInfoResponse {
        const message = {};
        if (value !== undefined)
            reflectionMergePartial<GetUserInfoResponse>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: GetUserInfoResponse): GetUserInfoResponse {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* nextTwirpTest.user.UserInfo userInfo */ 1:
                    message.userInfo = UserInfo.internalBinaryRead(reader, reader.uint32(), options, message.userInfo);
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: GetUserInfoResponse, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* nextTwirpTest.user.UserInfo userInfo = 1; */
        if (message.userInfo)
            UserInfo.internalBinaryWrite(message.userInfo, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
export const GetUserInfoResponse = new GetUserInfoResponse$Type();
/**
 * Type for protobuf message nextTwirpTest.user.SaveUserInfoRequest
 */
class SaveUserInfoRequest$Type extends MessageType<SaveUserInfoRequest> {
    constructor() {
        super("nextTwirpTest.user.SaveUserInfoRequest", [
            { no: 1, name: "givenName", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 2, name: "familyName", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 3, name: "email", kind: "scalar", T: 9 /*ScalarType.STRING*/ },
            { no: 4, name: "imageUrl", kind: "scalar", T: 9 /*ScalarType.STRING*/ }
        ]);
    }
    create(value?: PartialMessage<SaveUserInfoRequest>): SaveUserInfoRequest {
        const message = { givenName: "", familyName: "", email: "", imageUrl: "" };
        if (value !== undefined)
            reflectionMergePartial<SaveUserInfoRequest>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: SaveUserInfoRequest): SaveUserInfoRequest {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* string givenName */ 1:
                    message.givenName = reader.string();
                    break;
                case /* string familyName */ 2:
                    message.familyName = reader.string();
                    break;
                case /* string email */ 3:
                    message.email = reader.string();
                    break;
                case /* string imageUrl */ 4:
                    message.imageUrl = reader.string();
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: SaveUserInfoRequest, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* string givenName = 1; */
        if (message.givenName !== "")
            writer.tag(1, WireType.LengthDelimited).string(message.givenName);
        /* string familyName = 2; */
        if (message.familyName !== "")
            writer.tag(2, WireType.LengthDelimited).string(message.familyName);
        /* string email = 3; */
        if (message.email !== "")
            writer.tag(3, WireType.LengthDelimited).string(message.email);
        /* string imageUrl = 4; */
        if (message.imageUrl !== "")
            writer.tag(4, WireType.LengthDelimited).string(message.imageUrl);
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
export const SaveUserInfoRequest = new SaveUserInfoRequest$Type();
/**
 * Type for protobuf message nextTwirpTest.user.SaveUserInfoResponse
 */
class SaveUserInfoResponse$Type extends MessageType<SaveUserInfoResponse> {
    constructor() {
        super("nextTwirpTest.user.SaveUserInfoResponse", [
            { no: 1, name: "userInfo", kind: "message", T: () => UserInfo }
        ]);
    }
    create(value?: PartialMessage<SaveUserInfoResponse>): SaveUserInfoResponse {
        const message = {};
        if (value !== undefined)
            reflectionMergePartial<SaveUserInfoResponse>(this, message, value);
        return message;
    }
    internalBinaryRead(reader: IBinaryReader, length: number, options: BinaryReadOptions, target?: SaveUserInfoResponse): SaveUserInfoResponse {
        let message = target ?? this.create(), end = reader.pos + length;
        while (reader.pos < end) {
            let [fieldNo, wireType] = reader.tag();
            switch (fieldNo) {
                case /* nextTwirpTest.user.UserInfo userInfo */ 1:
                    message.userInfo = UserInfo.internalBinaryRead(reader, reader.uint32(), options, message.userInfo);
                    break;
                default:
                    let u = options.readUnknownField;
                    if (u === "throw")
                        throw new globalThis.Error(`Unknown field ${fieldNo} (wire type ${wireType}) for ${this.typeName}`);
                    let d = reader.skip(wireType);
                    if (u !== false)
                        (u === true ? UnknownFieldHandler.onRead : u)(this.typeName, message, fieldNo, wireType, d);
            }
        }
        return message;
    }
    internalBinaryWrite(message: SaveUserInfoResponse, writer: IBinaryWriter, options: BinaryWriteOptions): IBinaryWriter {
        /* nextTwirpTest.user.UserInfo userInfo = 1; */
        if (message.userInfo)
            UserInfo.internalBinaryWrite(message.userInfo, writer.tag(1, WireType.LengthDelimited).fork(), options).join();
        let u = options.writeUnknownFields;
        if (u !== false)
            (u == true ? UnknownFieldHandler.onWrite : u)(this.typeName, message, writer);
        return writer;
    }
}
export const SaveUserInfoResponse = new SaveUserInfoResponse$Type();
/**
 * @generated from protobuf service nextTwirpTest.user.User
 */
export class UserClient implements IUserClient {
    readonly typeName = "nextTwirpTest.user.User";
    readonly methods: MethodInfo[] = [
        { service: this, name: "getAccessToken", I: GetAccessTokenRequest, O: GetAccessTokenResponse },
        { service: this, name: "getUserInfo", I: GetUserInfoRequest, O: GetUserInfoResponse },
        { service: this, name: "saveUserInfo", I: SaveUserInfoRequest, O: SaveUserInfoResponse }
    ];
    constructor(private readonly _transport: RpcTransport) {
    }
    getAccessToken(input: GetAccessTokenRequest, options?: RpcOptions): UnaryCall<GetAccessTokenRequest, GetAccessTokenResponse> {
        const method = this.methods[0], opt = this._transport.mergeOptions(options), i = method.I.create(input);
        return stackIntercept<GetAccessTokenRequest, GetAccessTokenResponse>("unary", this._transport, method, opt, i);
    }
    getUserInfo(input: GetUserInfoRequest, options?: RpcOptions): UnaryCall<GetUserInfoRequest, GetUserInfoResponse> {
        const method = this.methods[1], opt = this._transport.mergeOptions(options), i = method.I.create(input);
        return stackIntercept<GetUserInfoRequest, GetUserInfoResponse>("unary", this._transport, method, opt, i);
    }
    saveUserInfo(input: SaveUserInfoRequest, options?: RpcOptions): UnaryCall<SaveUserInfoRequest, SaveUserInfoResponse> {
        const method = this.methods[2], opt = this._transport.mergeOptions(options), i = method.I.create(input);
        return stackIntercept<SaveUserInfoRequest, SaveUserInfoResponse>("unary", this._transport, method, opt, i);
    }
}
