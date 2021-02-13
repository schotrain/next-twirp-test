import { Intent, Position, Toaster } from "@blueprintjs/core";

/** Singleton toaster instance. Create separate instances for different options. */
let appToaster;

export const getAppToaster = () => {
    if (!appToaster) {
        appToaster = Toaster.create({
            className: "notification-toaster",
            position: Position.TOP,
        });
    }
    return appToaster
}

export const showToasterErrorMessage = (message: string, exception: any) => {
    getAppToaster().show({
        intent: Intent.DANGER,
        icon: "error",
        message: message
    })
    console.error(exception)
}

export const showToasterSuscessMessage = (message: string) => {
    getAppToaster().show({
        intent: Intent.SUCCESS,
        icon: "tick",
        message: message
    })
}

